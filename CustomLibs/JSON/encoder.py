def custom_json_encode(data):
    """ Custom JSON encoder to encode a Python dictionary as a JSON string. """
    if isinstance(data, dict):
        json_str = "{"
        for key, value in data.items():
            json_str += f'"{key}": {custom_json_encode(value)}, '
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


def main():
    # Example dictionary
    data = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": False,
        # "grades": [95, 88, 72],
        "address": {
            "street": "123 Main St",
            "zip": "10001"
        }
    }

    # Encode the dictionary as a JSON string using the custom encoder
    json_string = custom_json_encode(data)

    # Save the JSON string to a file
    with open("../../data/output.json", "w") as json_file:
        json_file.write(json_string)

    print("JSON data has been saved to output.json")


if __name__ == "__main__":
    main()


