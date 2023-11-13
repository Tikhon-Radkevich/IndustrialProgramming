import unittest

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

    def test_scenario_1(self):
        self._test_scenario(0)

    def test_scenario_2(self):
        self._test_scenario(1)

    def test_scenario_3(self):
        self._test_scenario(2)

    def test_scenario_4(self):
        self._test_scenario(3)

    def _test_scenario(self, index):
        file_path, open_scenario, key, result_file_path = self.file_scenario_key_result[index]
        custom_f_process = OpenFileProcess(file_path, use_custom_lib=True, open_scenario=open_scenario, key=key)
        std_f_process = OpenFileProcess(file_path, use_custom_lib=False, open_scenario=open_scenario, key=key)
        custom_expressions = custom_f_process.decode()
        std_expressions = std_f_process.decode()
        self.assertEqual(custom_expressions, std_expressions)
