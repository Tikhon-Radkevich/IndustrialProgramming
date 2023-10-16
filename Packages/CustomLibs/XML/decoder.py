class CustomXMLDecoder:
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
