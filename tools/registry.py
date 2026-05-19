from tools.read import READ_TOOL, read_file

TOOLS = {
    "Read": {
        "schema": READ_TOOL,
        "handler": read_file
    }
}
