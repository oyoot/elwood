import subprocess

from tools.base import tool

BASH_TOOL = tool(
    "Bash",
    "Execute a shell command",
    {
        "type": "object",
        "required": ["command"],
        "properties": {
            "command": {
                "type": "string",
                "description": "The command to execute"
            }
        }
    }
)

def run_command(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr