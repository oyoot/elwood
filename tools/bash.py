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
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout