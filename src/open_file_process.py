from CustomLibs.JSON.decoder import CustomJsonDecode
from CustomLibs.XML.decoder import CustomXMLDecode

from json import loads
from xmltodict import parse

from src.expression import Expression
from src.file_crypt import decrypt
from src.file_zip import unzip_file


class FileProcess:
    TYPE_TO_DECODER = {
        "json": {"standard": loads, "custom": CustomJsonDecode()},
        "xml": {"standard": parse, "custom": CustomXMLDecode()},
    }
    SCENARIO_TO_FUNC = {
        "decrypt": decrypt,
        "unzip-decrypt": lambda file_path, key: unzip_file(decrypt(file_path, key)),
        "decrypt-unzip": lambda file_path, key: decrypt(unzip_file(file_path), key),
    }

    def __init__(self, file_path: str, use_custom_lib=False, open_scenario="", key=None):
        self.file_path = file_path
        self.file_name = file_path.split("/")[-1]
        self._use_custom_lib = use_custom_lib
        self._data: dict = {}

    def decode(self) -> list[Expression]:
        file_type = self.file_name.split(".")[-1]
        if file_type not in self.TYPE_TO_DECODER.keys():
            raise ValueError(f"Invalid file type: {file_type}")

        with open(self.file_path, "r") as f:
            data = f.read()

        if self._use_custom_lib:
            file_decoder = self.TYPE_TO_DECODER[file_type]["custom"]
        else:
            file_decoder = self.TYPE_TO_DECODER[file_type]["standard"]

        self._data = file_decoder(data)
        self._data = self._data["Expressions"]

        expression_list = []
        for title, expression_data in self._data.items():
            expression_list.append(Expression(title, expression_data["expression"], expression_data["args"]))

        return expression_list

