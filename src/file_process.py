import shutil
from json import loads, dumps
from xmltodict import parse

from Packages.CustomLibs import CustomJsonDecoder, CustomJsonEncoder, CustomXMLDecoder

from src.expression import Expression
from src.file_crypt import decrypt, encrypt_and_get_key
from src.file_zip import unzip_file, zip_file

from config import CACHE_DIR


class OpenFileProcess:
    TYPE_TO_DECODER = {
        "json": {"standard": loads, "custom": CustomJsonDecoder()},
        "xml": {"standard": parse, "custom": CustomXMLDecoder()},
    }
    SCENARIO_TO_FUNC = {
        "unzip": unzip_file,
        "decrypt": lambda file_path, key: decrypt(file_path, key),
        "decrypt-unzip": lambda file_path, key: unzip_file(decrypt(file_path, key)),
        "unzip-decrypt": lambda file_path, key: decrypt(unzip_file(file_path), key),
    }

    def __init__(self, file_path: str, use_custom_lib=False, open_scenario="", key=None):
        self.file_path = file_path
        self.file_name = file_path.split("/")[-1]
        self.open_scenario = open_scenario
        self.key = key
        self._use_custom_lib = use_custom_lib
        self._data: dict = {}

    def decode(self) -> list[Expression]:

        file_in_cache = f"{CACHE_DIR}/{self.file_name}"
        if self.file_path != file_in_cache:
            shutil.copy(self.file_path, file_in_cache)

        options = []
        if len(self.open_scenario) != 0:
            options = self.open_scenario.split("-") if "-" in self.open_scenario else [self.open_scenario]

        for option in options:
            if option == "unzip":
                file_in_cache = self.SCENARIO_TO_FUNC[option](file_in_cache)
                self.file_name = file_in_cache.split("/")[-1]
            elif option == "decrypt":
                self.SCENARIO_TO_FUNC[option](file_in_cache, self.key)

        file_type = self.file_name.split(".")[-1]
        if file_type not in self.TYPE_TO_DECODER.keys():
            raise ValueError(f"Invalid file type: {file_type}")

        with open(file_in_cache, "r") as f:
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


class SaveFileProcess:
    TYPE_TO_ENCODER = {
        ".json": {"standard": dumps, "custom": CustomJsonEncoder()},
        # ".xml": {"standard": parse, "custom": CustomXMLDecode()},
    }
    SCENARIO_TO_FUNC = {
        "zip": zip_file,
        "encrypt": encrypt_and_get_key,
    }

    def __init__(self, option, file_path, format_choice, use_custom_lib):
        self.options = option
        self.file_path = file_path
        self.format_choice = format_choice
        self.use_custom_lib = use_custom_lib

    def save(self, expressions_data):
        if len(self.options) != 0:
            self.options = self.options.split("-") if "-" in self.options else [self.options]

        if self.use_custom_lib:
            data_encoder = self.TYPE_TO_ENCODER[self.format_choice]["custom"]
        else:
            data_encoder = self.TYPE_TO_ENCODER[self.format_choice]["standard"]

        f_name = self.file_path.split("/")[-1]
        file_in_cache = f"{CACHE_DIR}/{f_name}"

        with open(file_in_cache, "w") as file:
            file.write(data_encoder(expressions_data))

        key = None
        for option in self.options:
            if option == "zip":
                file_in_cache = self.SCENARIO_TO_FUNC[option](file_in_cache)
                self.file_path = self.file_path.split(".")[0] + ".zip"
                print(self.file_path)
            elif option == "encrypt":
                key = self.SCENARIO_TO_FUNC[option](file_in_cache)
                print(key)

        if self.file_path != file_in_cache:
            shutil.copy(file_in_cache, self.file_path)

        return key

