import argparse
import json
import os
import sys

from openai import OpenAI

from tools.registry import TOOLS

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    tools = [tool["schema"] for tool in TOOLS.values()]

    chat = client.chat.completions.create(
        model="anthropic/claude-haiku-4.5",
        messages=[{"role": "user", "content": args.p}],
        tools=tools,
    )

    if not chat.choices or len(chat.choices) == 0:
        raise RuntimeError("no choices in response")

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!", file=sys.stderr)

    for tool in chat.choices[0].message.tool_calls:
        tool_name = tool.function.name
        arguments = json.loads(tool.function.arguments)
        handler = TOOLS[tool_name]["handler"]
        result = handler(**arguments)

        print(result)

    # print(chat.choices[0].message.content)


if __name__ == "__main__":
    main()
