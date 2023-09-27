from tkinter import Toplevel, Label, Radiobutton, Button, StringVar


class SaveFileDialog:
    def __init__(self, parent, label, options):
        self.parent = parent
        self.result: str = ""

        self.dialog = Toplevel(parent)
        self.selected_option = StringVar()

        parent_x = parent.winfo_rootx()  # X coordinate of the parent's top-left corner
        parent_y = parent.winfo_rooty()  # Y coordinate of the parent's top-left corner
        parent_width = parent.winfo_width()  # Width of the parent window
        parent_height = parent.winfo_height()  # Height of the parent window

        # Calculate the position of the dialog at the center of the parent
        self.dialog_x = parent_x + (parent_width - 190) // 2
        self.dialog_y = parent_y + (parent_height - 210) // 2

        label = Label(self.dialog, text=label)
        label.pack(padx=10, pady=5)

        for text, value in options:
            button = Radiobutton(self.dialog, text=text, variable=self.selected_option, value=value)
            button.pack(padx=10, pady=5)

        confirm_button = Button(self.dialog, text="Confirm", command=self.confirm_choice)
        confirm_button.pack(padx=10, pady=5)

    def confirm_choice(self):
        self.result = self.selected_option.get()
        self.dialog.destroy()


class FormatChoiceDialog(SaveFileDialog):
    title = "File Format"
    geometry = "190x135"
    options = [
        ("JSON", ".json"),
        ("XML", ".xml")
    ]
    default_option = "json"
    label = "Choose file format:"

    def __init__(self, parent):
        super().__init__(parent=parent, label=self.label, options=self.options)

        self.dialog.title(self.title)
        self.dialog.geometry(self.geometry)
        self.dialog.geometry(f"{self.geometry}+{self.dialog_x}+{self.dialog_y}")

        self.selected_option.set(self.default_option)


class OptionalParamChoiceDialog(SaveFileDialog):
    title = "Option Choice"
    geometry = "190x210"
    options = [
        ("ZIP", "zip"),
        ("Encrypt", "encrypt"),
        ("ZIP -> Encrypt", "zip-encrypt"),
        ("Encrypt -> ZIP", "encrypt-zip")
    ]
    default_option = ""
    label = "Choose extra parameter"

    def __init__(self, parent):
        super().__init__(parent=parent, label=self.label, options=self.options)

        self.dialog.title(self.title)
        self.dialog.geometry(self.geometry)
        self.dialog.geometry(f"{self.geometry}+{self.dialog_x}+{self.dialog_y}")

        self.selected_option.set(self.default_option)

