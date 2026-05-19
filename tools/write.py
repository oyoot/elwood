from tools.base import tool

WRITE_TOOL = tool(
    "Write",
    "Write content to a file",
    {
      "type": "object",
      "required": ["file_path", "content"],
      "properties": {
        "file_path": {
          "type": "string",
          "description": "The path of the file to write to"
        },
        "content": {
          "type": "string",
          "description": "The content to write to the file"
        }
      }
    }
)

def write_file(file_path: str, content: str) -> str:
    with open(file_path, "w") as f:
        f.write(content)
    return f"File {file_path} written successfully"