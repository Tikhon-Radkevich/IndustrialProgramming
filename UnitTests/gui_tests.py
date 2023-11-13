import unittest
from tkinter import Tk
from unittest.mock import patch
from GUI.main import RootWin


class MockOptionDialog:
    def __init__(self, result):
        self.result = result
        self.dialog = Tk()

    def destroy(self):
        self.dialog.destroy()


class TestRootWin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.app = RootWin(cls.root)

    def setUp(self):
        self.app.expressions_data = {"Expressions": {}}

    @patch('tkinter.messagebox.showinfo')
    def test_show_project_info(self, mock_showinfo):
        self.app.show_project_info()
        mock_showinfo.assert_called_with("Project Information", self.app.info_text)

    @patch('tkinter.simpledialog.askstring', return_value="test_key")
    @patch('tkinter.filedialog.askopenfilename', return_value="data/input/test_json.json")
    def test_open_file_dialog(self, mock_askopenfilename, mock_askstring):
        self.app.open_file_dialog()
        mock_askopenfilename.assert_called_with(title="Select a File", initialdir="")
        mock_askstring.assert_called_once_with("Key", "Enter the key:", parent=self.app.root)

    @patch('tkinter.filedialog.asksaveasfilename', return_value="test_save_file_path")
    @patch('GUI.main.SaveFormatChoiceDialog', return_value=MockOptionDialog(".json"))
    @patch('GUI.main.SaveOptionalParamChoiceDialog', return_value=MockOptionDialog("options"))
    @patch('GUI.main.CopyKyeDialog', return_value=MockOptionDialog("Copy"))
    def test_save_file_dialog(self, mock_asksaveasfilename, mock_format_dialog, mock_option_dialog,
                              mock_copy_key_dialog):
        self.app.save_file_dialog()
        mock_asksaveasfilename.assert_called_with(title="Save File", defaultextension="", initialdir="working_path")
        mock_format_dialog.assert_called_once_with(self.app.root)
        mock_option_dialog.assert_called_once_with(self.app.root)
        mock_copy_key_dialog.assert_called_once_with("test_key", self.app.root)


if __name__ == '__main__':
    unittest.main()
