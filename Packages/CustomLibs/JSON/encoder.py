class CustomJsonEncoder:
    def __init__(self): ...

    def __call__(self, data):
        """ Custom JSON encoder to encode a Python dictionary as a JSON string. """
        if isinstance(data, dict):
            json_str = "{"
            for key, value in data.items():
                json_str += f'"{key}": {self(value)}, '
            # Remove the trailing comma and add the closing curly brace
            json_str = json_str[:-2] + "}"
        elif isinstance(data, str):
            json_str = f'"{data}"'
        elif isinstance(data, bool):
            json_str = "true" if data else "false"
        elif isinstance(data, (int, float)):
            json_str = str(data)
        elif data is None:
            json_str = "null"
        else:
            raise TypeError(f"Unsupported data type: {type(data)}")
        return json_str
