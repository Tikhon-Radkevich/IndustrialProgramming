import unittest
from tkinter import Tk
from unittest.mock import patch
from GUI.process_dialog import (
    CopyKyeDialog,
    SaveFormatChoiceDialog,
    SaveOptionalParamChoiceDialog,
    OpenOptionalParamChoiceDialog,
)


class TestCustomDialogs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()

    def test_copy_key_dialog(self):
        key = "test_key"
        with patch("pyperclip.copy") as mock_copy:
            dialog = CopyKyeDialog(key, self.root)
            dialog()
            mock_copy.assert_called_once_with(key)

    def test_save_format_choice_dialog(self):
        with patch.object(SaveFormatChoiceDialog, "__call__", return_value=None) as mock_call:
            dialog = SaveFormatChoiceDialog(self.root)
            dialog()
            mock_call.assert_called_once()

    def test_save_optional_param_choice_dialog(self):
        with patch.object(SaveOptionalParamChoiceDialog, "__call__", return_value=None) as mock_call:
            dialog = SaveOptionalParamChoiceDialog(self.root)
            dialog()
            mock_call.assert_called_once()

    def test_open_optional_param_choice_dialog(self):
        with patch.object(OpenOptionalParamChoiceDialog, "__call__", return_value=None) as mock_call:
            dialog = OpenOptionalParamChoiceDialog(self.root)
            dialog()
            mock_call.assert_called_once()


if __name__ == "__main__":
    unittest.main()
