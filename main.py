import json


def main():
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    with open("data/data.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()

