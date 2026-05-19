from tools.read import READ_TOOL, read_file
from tools.write import WRITE_TOOL, write_file

TOOLS = {
    "Read": {
        "schema": READ_TOOL,
        "handler": read_file
    },
    "Write": {
        "schema": WRITE_TOOL,
        "handler": write_file
    }
}
