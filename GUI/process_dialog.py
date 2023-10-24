from tkinter import Toplevel, Label, Radiobutton, Button, StringVar
import pyperclip


class CustomDialog:
    def __init__(self, parent, label, options, default_option, title, geometry, confirm_button_text):
        self.parent = parent
        self.title = title
        self.geometry = geometry
        self.result: str = ""

        self.dialog = Toplevel(parent)
        self.selected_option = StringVar()
        self.selected_option.set(default_option)

        parent_x = parent.winfo_rootx()  # X coordinate of the parent's top-left corner
        parent_y = parent.winfo_rooty()  # Y coordinate of the parent's top-left corner
        parent_width = parent.winfo_width()  # Width of the parent window
        parent_height = parent.winfo_height()  # Height of the parent window

        # Calculate the position of the dialog at the center of the parent
        self.dialog_x = parent_x + (parent_width - 190) // 2
        self.dialog_y = parent_y + (parent_height - 210) // 2

        self.dialog.geometry(f"{self.geometry}+{self.dialog_x}+{self.dialog_y}")

        label = Label(self.dialog, text=label)
        label.pack(padx=10, pady=5)

        for text, value in options:
            button = Radiobutton(self.dialog, text=text, variable=self.selected_option, value=value)
            button.pack(padx=10, pady=5)

        confirm_button = Button(self.dialog, text=confirm_button_text, command=self.__call__)
        confirm_button.pack(padx=10, pady=5)

    def __call__(self, *args, **kwargs):
        self.result = self.selected_option.get()
        self.dialog.destroy()


class CopyKyeDialog(CustomDialog):
    kwargs = dict(
        title="Copy Key",
        geometry="500x120",
        options=[],
        default_option="",
        label="Your key is: ",
        confirm_button_text="Copy"
    )

    def __init__(self, key, parent):
        self.kwargs["label"] += key
        self.key = key
        super().__init__(parent=parent, **self.kwargs)

    def __call__(self, *args, **kwargs):
        pyperclip.copy(self.key)
        self.dialog.destroy()


class SaveFormatChoiceDialog(CustomDialog):
    kwargs = dict(
        title="File Format",
        geometry="190x135",
        options=[
            ("JSON", ".json"),
            ("XML", ".xml")
        ],
        default_option="json",
        label="Choose file format:",
        confirm_button_text="Confirm"
    )

    def __init__(self, parent):
        super().__init__(parent=parent, **self.kwargs)


class SaveOptionalParamChoiceDialog(CustomDialog):
    kwargs = dict(
        title="Option Choice",
        geometry="190x210",
        options=[
            ("ZIP", "zip"),
            ("Encrypt", "encrypt"),
            ("ZIP -> Encrypt", "zip-encrypt"),
            ("Encrypt -> ZIP", "encrypt-zip")
        ],
        default_option="",
        label="Choose extra parameter",
        confirm_button_text="Confirm"
    )

    def __init__(self, parent):
        super().__init__(parent=parent, **self.kwargs)


class OpenOptionalParamChoiceDialog(CustomDialog):
    kwargs = dict(
        title="Option Choice",
        geometry="190x210",
        options=[
            ("Unzip", "unzip"),
            ("Decrypt", "decrypt"),
            ("Unzip -> Decrypt", "unzip-decrypt"),
            ("Decrypt -> Unzip", "decrypt-unzip")
        ],
        default_option="",
        label="Choose extra parameter",
        confirm_button_text="Confirm"
    )

    def __init__(self, parent):
        super().__init__(parent=parent, **self.kwargs)
