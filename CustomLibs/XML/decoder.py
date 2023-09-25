class CustomXMLDecode:
    """ Custom XML decoder to decode a XML string into a Python dictionary. """

    def __init__(self):
        ...

    def __call__(self, data: str):
        return self.file_decoder(data)

    def file_decoder(self, data: str):
        if "<" not in data:
            value = None if "None" in data else data.strip()
            return value
        result = {}
        while "<" in data:
            tag = data[data.find("<")+1:data.find(">")]
            list_data = data.split(tag)
            tag_data = list_data[1]
            data = list_data[-1][1:-1]
            result[tag] = self.file_decoder(tag_data[1:-2])
        return result


def main():
    xml_file_path = "../../data/Example.xml"
    decoder = CustomXMLDecode()
    with open(xml_file_path, "r") as f:
        data = f.read()
    data_dict = decoder.file_decoder(data)
    print(data_dict)


if __name__ == "__main__":
    main()
