import unittest

import json

from src.file_process import OpenFileProcess


class FileProcessUnitTest(unittest.TestCase):
    test_xml_crypt_key = "p_QL47TnLzu8R5o9MDfWn2TVQ4RJZY6kHaDSjD0f5rg="
    test_json_zip_crypt_key = "lV7KOSGLk9QmB1Lp0-O_LyPDOzioNO_x8eWhff6TLUM="
    test_xml_crypt_zip_key = "X_xDTbZjR8E0R_6mOdVtmRKZaKpAVI2cvnN7n69X9Qs="

    test_xml_crypt_path = "data/input/test_xml_crypt.xml"
    test_json_zip_crypt_path = "data/input/test_json_zip_crypt.zip"
    test_xml_crypt_zip_path = "data/input/test_xml_crypt_zip.zip"
    test_json_zip_path = "data/input/test_json_zip.zip"

    xml_expression_result_path = "data/input/test_xml_expression_result.xml"
    json_expression_result_path = "data/input/test_json_expression_result.json"

    file_scenario_key_result = (
        (test_json_zip_path, "unzip", None, json_expression_result_path),
        (test_xml_crypt_path, "decrypt", test_xml_crypt_key, xml_expression_result_path),
        (test_json_zip_crypt_path, "decrypt-unzip", test_json_zip_crypt_key, json_expression_result_path),
        (test_xml_crypt_zip_path, "unzip-decrypt", test_xml_crypt_zip_key, xml_expression_result_path)
    )

    def check_expressions_result(self, expressions, result_file_path):
        with open(result_file_path, "r") as f:
            result_data = f.read()
            print("result", result_data)
        for ex in expressions:
            ex.calculate()
            ex_dict_data = ex.get_dict()
            print(json.dumps(ex_dict_data))
            self.assertEqual(json.dumps(ex_dict_data), result_data)

    def test_open_file_process_with_custom_libs(self):
        use_custom_libs = True
        for file_path, open_scenario, key, result_file_path in self.file_scenario_key_result:
            f_process = OpenFileProcess(file_path, use_custom_lib=use_custom_libs, open_scenario=open_scenario, key=key)
            expressions = f_process.decode()
            self.check_expressions_result(expressions, result_file_path)
