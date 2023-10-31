import unittest

import re
import json
from xmltodict import parse
from dicttoxml import dicttoxml

from Packages.CustomLibs import CustomJsonDecoder, CustomJsonEncoder, CustomXMLDecoder, CustomXMLEncoder
from Packages.expression import Expression as Expression


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

