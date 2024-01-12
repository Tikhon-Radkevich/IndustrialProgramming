from tkinter import filedialog, messagebox, simpledialog
import tkinter as tk

from src.file_process import OpenFileProcess, SaveFileProcess
from GUI.process_dialog import SaveFormatChoiceDialog, SaveOptionalParamChoiceDialog, OpenOptionalParamChoiceDialog, \
    CopyKyeDialog
from config import EXAMPLE_FILES_PATH, CACHE_DIR, WORKING_PATH


class RootWin:
    width = 400
    height = 600
    min_width = 300
    min_height = 400

    background_color = "#f0f0f0"
    text_color = "black"
    button_bg = "#4caf50"
    button_fg = "white"

    info_text = """
        Application to extract expressions data 
        from files with extension: json, xml.
        With option zip and crypt.
        """

    def __init__(self):
        self.root = tk.Tk()
        self._win_initialization()

        self.info_button = None
        self.open_button = None
        self.save_button = None
        self.custom_lib_checkbutton = None
        self.custom_lib_var = tk.IntVar()
        self._button_initialization()

        self.description_text = tk.Text(self.root, wrap=tk.WORD, width=60, height=20, bg=self.background_color,
                                        fg=self.text_color)
        self.description_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.root, command=self.description_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.description_text.config(yscrollcommand=self.scrollbar.set)
        self.expressions_data: dict = {"Expressions": {}}

    def run(self):
        """ Start the main event loop """
        self.root.mainloop()

    def open_file_dialog(self):
        self.description_text.delete("1.0", tk.END)
        file_path = filedialog.askopenfilename(title="Select a File", initialdir=EXAMPLE_FILES_PATH)
        if not file_path:
            ...
        option_dialog = OpenOptionalParamChoiceDialog(self.root)
        self.root.wait_window(option_dialog.dialog)
        open_scenario = option_dialog.result
        key = None
        if len(open_scenario) != 0 and open_scenario != "unzip":
            key = simpledialog.askstring("Key", "Enter the key:", parent=self.root)
        f_process = OpenFileProcess(
            file_path, use_custom_lib=bool(self.custom_lib_var.get()), open_scenario=open_scenario, key=key)
        expressions = f_process.decode()
        self.expressions_data["Expressions"].clear()

        for ex in expressions:
            try:
                ex.calculate()
                description = ex.get_description()
                self.description_text.insert(tk.END, description + "\n\n")
                ex_dict_data = ex.get_dict()
                for key, data in ex_dict_data.items():
                    self.expressions_data["Expressions"][key] = data
            except Exception as e:
                messagebox.showerror("Error", f"{e}")

    def save_file_dialog(self):
        format_choice_dialog = SaveFormatChoiceDialog(self.root)
        self.root.wait_window(format_choice_dialog.dialog)
        format_choice = format_choice_dialog.result

        option_choice_dialog = SaveOptionalParamChoiceDialog(self.root)
        self.root.wait_window(option_choice_dialog.dialog)
        options = option_choice_dialog.result

        file_path = filedialog.asksaveasfilename(title="Save File", defaultextension="", initialdir=WORKING_PATH)
        file_path += format_choice

        use_custom_lib = bool(self.custom_lib_var.get())

        f_process = SaveFileProcess(options, file_path, format_choice, use_custom_lib)
        key = f_process.save(self.expressions_data)

        if key is not None:
            copy_key_dialog = CopyKyeDialog(key, self.root)
            self.root.wait_window(copy_key_dialog.dialog)
        return

    def show_project_info(self):
        messagebox.showinfo("Project Information", self.info_text)

    def _win_initialization(self):
        self.root.title("Industrial Programming")
        self.root.minsize(self.min_width, self.min_height)
        x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.configure(bg=self.background_color)

    def _button_initialization(self):

        self.info_button = tk.Button(self.root, text="Info", command=self.show_project_info, bg=self.button_bg,
                                     fg=self.button_fg)
        self.info_button.pack(padx=10, pady=5, anchor="ne")

        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=0, pady=10)

        self.open_button = tk.Button(button_frame, text="Open File", command=self.open_file_dialog, bg=self.button_bg,
                                     fg=self.button_fg)
        self.open_button.pack(side=tk.LEFT, padx=0, pady=0)

        self.save_button = tk.Button(button_frame, text="Save", command=self.save_file_dialog, bg=self.button_bg,
                                     fg=self.button_fg)
        self.save_button.pack(side=tk.RIGHT, padx=0)

        self.custom_lib_checkbutton = tk.Checkbutton(self.root, text="Use Custom Library", variable=self.custom_lib_var,
                                                     bg=self.background_color, fg=self.text_color)
        self.custom_lib_checkbutton.pack(pady=10)


def main():
    root = RootWin()
    root.run()


if __name__ == "__main__":
    main()
