class CustomXMLDecoder:
    """ Custom XML decoder to decode a XML string into a Python dictionary. """

    def __init__(self):
        ...

    def __call__(self, data: str):
        return self.file_decoder(data)

    def file_decoder(self, data: str):
        if "<" not in data:
            data = data.strip()
            value = None if len(data) == 0 else data
            return value
        result = {}
        while "<" in data:
            tag = data[data.find("<")+1:data.find(">")]
            list_data = data.split(tag)
            tag_data = list_data[1]
            data = list_data[-1][1:]
            result[tag] = self.file_decoder(tag_data[1:-2])
        return result


if __name__ == "__main__":
    with open("../../../data/working/cust.xml", "r") as f:
        xml_data_str = f.read()
    decoder = CustomXMLDecoder()
    xml_dict = decoder(xml_data_str)
    print(xml_dict)
