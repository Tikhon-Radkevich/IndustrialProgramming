from tkinter import filedialog, messagebox, simpledialog
import tkinter as tk

from src.file_process import FileProcess
from src.file_crypt import encrypt_and_get_key, decrypt
from GUI.save_file_process import FormatChoiceDialog, OptionalParamChoiceDialog


class RootWin:
    width = 400  # Increased the width
    height = 600  # Increased the height
    min_width = 300  # Increased the minimum width
    min_height = 400  # Increased the minimum height

    # Define a color theme
    background_color = "#f0f0f0"  # Light gray background
    text_color = "black"  # Black text
    button_bg = "#4caf50"  # Green button background
    button_fg = "white"  # White button text

    info_text = """
        Project Name: Your Project Name
        University: Your University Name
        Description: This is a project for the university.
        """

    def __init__(self):
        self.root = tk.Tk()
        self._win_initialization()

        # buttons
        self.info_button = None
        self.open_button = None
        self.save_button = None
        self.custom_lib_checkbutton = None
        self.custom_lib_var = tk.IntVar()
        self._button_initialization()

        # Create a Text widget for displaying descriptions
        self.description_text = tk.Text(self.root, wrap=tk.WORD, width=60, height=20, bg=self.background_color, fg=self.text_color)
        self.description_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)  # Fill the available space

        # Create a vertical scrollbar for the Text widget
        self.scrollbar = tk.Scrollbar(self.root, command=self.description_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Text widget to work with the scrollbar
        self.description_text.config(yscrollcommand=self.scrollbar.set)
        self.expressions_data: dict = {"Expressions": {}}

    def run(self):
        """ Start the main event loop """
        self.root.mainloop()

    def open_file_dialog(self):
        self.description_text.delete("1.0", tk.END)
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
            f_process = FileProcess(file_path, use_custom_lib=bool(self.custom_lib_var.get()))
            expressions = f_process.decode()
            self.expressions_data["Expressions"].clear()

            # Calculate and append description for each Expression to the Text widget
            for ex in expressions:
                ex.calculate()  # Calculate the result
                description = ex.get_description()  # Get the description
                self.description_text.insert(tk.END, description + "\n\n")  # Append to the Text widget
                ex_dict_data = ex.get_dict()
                for key, data in ex_dict_data.items():
                    self.expressions_data["Expressions"][key] = data

            print(self.expressions_data)

            # print("Selected file:", file_path)

    def save_file_dialog(self):

        format_choice_dialog = FormatChoiceDialog(self.root)
        self.root.wait_window(format_choice_dialog.dialog)
        format_choice = format_choice_dialog.result

        option_choice_dialog = OptionalParamChoiceDialog(self.root)
        self.root.wait_window(option_choice_dialog.dialog)
        options = option_choice_dialog.result
        if len(options) == 0:
            options = []
        else:
            options = options.split("-") if "-" in options else [options]

        file_path = filedialog.asksaveasfilename(title="Save File", defaultextension="")
        file_path += format_choice


        print(file_path)


        print(format_choice)
        print(options)
        return

        file_path = filedialog.asksaveasfilename(title="Save File", defaultextension="")
        if file_path:
            format_choice = simpledialog.askstring("File Format", "Choose file format (json or xml):", parent=self.root)
            if format_choice and format_choice.lower() in ["json", "xml"]:
                format_choice = format_choice.lower()
                options = simpledialog.askstring("Options", "Choose options (comma-separated):", parent=self.root)
                if options:
                    options_list = options.split(",")
                    if "zip" in options_list:
                        # Implement ZIP functionality here
                        pass
                    if "encrypt" in options_list:
                        # Implement encryption functionality here
                        pass
                    # Save the file with chosen format and options
                    with open(file_path, "w") as file:
                        file.write(f"Format: {format_choice}\n")
                        file.write(f"Options: {', '.join(options_list)}\n")
                        file.write(self.description_text.get("1.0", tk.END))
                    messagebox.showinfo("File Saved", "File saved successfully.")
                else:
                    messagebox.showwarning("Options", "No options selected.")
            else:
                messagebox.showwarning("File Format", "Invalid file format choice.")

    def show_project_info(self):
        messagebox.showinfo("Project Information", self.info_text)

    def _win_initialization(self):
        self.root.title("Industrial Programming")
        self.root.minsize(self.min_width, self.min_height)
        x = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.height // 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.root.configure(bg=self.background_color)  # Set the background color

    def _button_initialization(self):

        self.info_button = tk.Button(self.root, text="Info", command=self.show_project_info, bg=self.button_bg,fg=self.button_fg)
        self.info_button.pack(padx=10, pady=5, anchor="ne")

        # Create a frame for the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=0, pady=10)

        self.open_button = tk.Button(button_frame, text="Open File", command=self.open_file_dialog, bg=self.button_bg, fg=self.button_fg)
        self.open_button.pack(side=tk.LEFT, padx=0, pady=0)

        self.save_button = tk.Button(button_frame, text="Save", command=self.save_file_dialog, bg=self.button_bg, fg=self.button_fg)
        self.save_button.pack(side=tk.RIGHT, padx=0)

        # Create a check button for custom libraries
        self.custom_lib_checkbutton = tk.Checkbutton(self.root, text="Use Custom Library", variable=self.custom_lib_var, bg=self.background_color, fg=self.text_color)
        self.custom_lib_checkbutton.pack(pady=10)


def main():
    r_win = RootWin()
    r_win.run()


if __name__ == "__main__":
    main()
