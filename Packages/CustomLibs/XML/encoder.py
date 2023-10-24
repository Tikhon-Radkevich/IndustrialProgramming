class CustomXMLEncoder:
    def __init__(self):
        self.tabs = []

    def __call__(self, data, root_name=None, level=0):
        if root_name is None:
            return self(data["Expressions"], root_name="Expressions")
        xml = "\t" * level + f"<{root_name}>\n"
        for key, value in data.items():
            if isinstance(value, dict):
                xml += self(value, key, level + 1)
            else:
                xml += "\t" * (level + 1) + f"<{key}>\n"
                xml += "\t" * (level + 2) + f"{value}\n"
                xml += "\t" * (level + 1) + f"</{key}>\n"
        xml += " " * level * 4 + f"</{root_name}>\n"
        return xml


def main():
    # Example dictionary
    data = {
        "person": {
            "name": "John",
            "age": "30",
            "city": "New York"
        }
    }
    encoder = CustomXMLEncoder()
    print(encoder(data, "Extencion"))


if __name__ == "__main__":
    main()
