from tools.base import tool

READ_TOOL = tool(
    "Read",
    "Read and return the contents of a file",
    {
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "The path to the file to read",
            }
        },
        "required": ["file_path"],
    },
)

def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
