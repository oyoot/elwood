from tools.read import READ_TOOL, read_file
from tools.write import WRITE_TOOL, write_file
from tools.bash import BASH_TOOL, run_command

TOOLS = {
    "Read": {
        "schema": READ_TOOL,
        "handler": read_file
    },
    "Write": {
        "schema": WRITE_TOOL,
        "handler": write_file
    },
    "Bash": {
        "schema": BASH_TOOL,
        "handler": run_command
    }
}
