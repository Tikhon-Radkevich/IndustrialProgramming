import unittest
from unittest.mock import patch
from tkinter import Tk
from GUI.main import RootWin  # Assuming your GUI class is in a separate file called root_win.py


class TestRootWin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Tk()
        cls.app = RootWin(cls.root)

    def setUp(self):
        self.app.expressions_data = {"Expressions": {}}

    def test_open_file_dialog_no_file_selected(self):
        with patch('tkinter.filedialog.askopenfilename', return_value=''):
            self.app.open_file_dialog()
            self.assertEqual(self.app.description_text.get("1.0", "end-1c"), '')

    def test_open_file_dialog_unzip_scenario(self):
        file_path = "path/to/test_file.zip"
        with patch('tkinter.filedialog.askopenfilename', return_value=file_path), \
             patch('GUI.root_win.OpenOptionalParamChoiceDialog', return_value=MockOptionDialog("unzip")), \
             patch('tkinter.simpledialog.askstring', return_value=None):
            self.app.open_file_dialog()
            self.assertNotEqual(self.app.description_text.get("1.0", "end-1c"), '')

    def test_save_file_dialog(self):
        with patch('GUI.root_win.SaveFormatChoiceDialog', return_value=MockOptionDialog(".txt")), \
             patch('GUI.root_win.SaveOptionalParamChoiceDialog', return_value=MockOptionDialog("options")), \
             patch('tkinter.filedialog.asksaveasfilename', return_value="path/to/save_file.txt"), \
             patch('GUI.root_win.SaveFileProcess') as mock_save_process, \
             patch('tkinter.messagebox.showinfo') as mock_showinfo:
            mock_save_process.return_value.save.return_value = "test_key"
            self.app.save_file_dialog()
            mock_save_process.assert_called_with("options", "path/to/save_file.txt", ".txt", True)
            mock_showinfo.assert_called_with("Key Copied", "The key has been copied to the clipboard.")

    def test_show_project_info(self):
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.app.show_project_info()
            mock_showinfo.assert_called_with("Project Information", self.app.info_text)


class MockOptionDialog:
    def __init__(self, result):
        self.result = result


if __name__ == '__main__':
    unittest.main()
