import os
import unittest

import re
import json
from xmltodict import parse
from dicttoxml import dicttoxml

from Packages.CustomLibs import CustomJsonDecoder, CustomJsonEncoder, CustomXMLDecoder, CustomXMLEncoder
from Packages.expression import Expression as Expression
from Packages.cache import create_cache_dir, clear_cache_dir

from src import file_crypt, file_zip, file_process


class PackagesUnitTest(unittest.TestCase):
    def test_custom_json_decoder(self):
        with open("data/input/test_json.json", "r") as f:
            data_str = f.read()
        data_dict = json.loads(data_str)
        decoder = CustomJsonDecoder()
        self.assertEqual(decoder(data_str), data_dict)

    def test_custom_json_encoder(self):
        with open("data/input/test_json.json", "r") as f:
            data_str = f.read()
        data_dict = json.loads(data_str)
        encoder = CustomJsonEncoder()
        self.assertEqual(encoder(data_dict), data_str)

    def test_custom_xml_decoder(self):
        with open("data/input/test_xml.xml", "r") as f:
            data_str = f.read()
        data_dict = parse(data_str)
        decoder = CustomXMLDecoder()
        self.assertEqual(decoder(data_str), data_dict)

    def test_custom_xml_encoder(self):
        with open("data/input/test_json.json", "r") as f:
            data_str = f.read()
        data_dict = json.loads(data_str)
        data_xml = dicttoxml(obj=data_dict, root=False, return_bytes=False, attr_type=False)
        encoder = CustomXMLEncoder()
        self.assertEqual(re.sub(r'[\t\n]', '', encoder(data_dict)), data_xml)

    def test_expression(self): ...
    # todo test for expressions


class FileProcessUnitTest(unittest.TestCase):

    def open_file_process_test(self):
        test_xml_crypt_key = "p_QL47TnLzu8R5o9MDfWn2TVQ4RJZY6kHaDSjD0f5rg="
        test_json_zip_crypt_key = "lV7KOSGLk9QmB1Lp0-O_LyPDOzioNO_x8eWhff6TLUM="
        test_xml_crypt_zip_key = "X_xDTbZjR8E0R_6mOdVtmRKZaKpAVI2cvnN7n69X9Qs="
        test_xml_crypt_path = "data/input/test_xml_crypt.xml"
        test_json_zip_crypt_path = "data/input/test_json_zip_crypt.zip"
        test_xml_crypt_zip_path = "data/input/test_xml_crypt_zip.zip"
        test_json_zip_path = "data/input/test_json_zip.zip"
        file_scenario_key = (
            (test_json_zip_path, "unzip", None),
            (test_xml_crypt_path, "decrypt", test_xml_crypt_key),
            (test_json_zip_crypt_path, "decrypt-unzip", test_json_zip_crypt_key),
            (test_xml_crypt_zip_path, "unzip-decrypt", test_xml_crypt_zip_key)
        )

        file_path = "data/input/test_json.json"
        f_process = file_process.OpenFileProcess(
            file_path, use_custom_lib=bool(self.custom_lib_var.get()), open_scenario=open_scenario, key=key)
        expressions = f_process.decode()
        pass
    def test_file_crypt(self):
        file_path = "data/input/test_json.json"
        key = file_crypt.encrypt_and_get_key(file_path)
        file_crypt.decrypt(file_path, key)
        with open(file_path, "r") as f:
            self.assertEqual(f.read(), "test")
        os.remove(file_path)

    def test_file_zip(self):
        file_path = "test_file.txt"
        with open(file_path, "w") as f:
            f.write("test")
        file_zip.zip_file(file_path)
        file_zip.unzip_file(file_path + ".zip")
        with open(file_path, "r") as f:
            self.assertEqual(f.read(), "test")
        os.remove(file_path)
        os.remove(file_path + ".zip")


