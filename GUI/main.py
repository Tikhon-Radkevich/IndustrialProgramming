from tkinter import filedialog, messagebox
import tkinter as tk

from src.file_process import FileProcess


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

    def run(self):
        """ Start the main event loop """
        self.root.mainloop()

    def open_file_dialog(self):
        # todo
        file_path = filedialog.askopenfilename(title="Select a File")

        custom_lib_state = self.custom_lib_var.get()
        if file_path:
            f_process = FileProcess(file_path)
            expressions = f_process.decode()

            # Calculate and append description for each Expression to the Text widget
            for ex in expressions:
                ex.calculate()  # Calculate the result
                description = ex.get_description()  # Get the description
                self.description_text.insert(tk.END, description + "\n\n")  # Append to the Text widget

            print("Selected file:", file_path)

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
        # Create an "Info" button in the top-right corner
        self.info_button = tk.Button(self.root, text="Info", command=self.show_project_info, bg=self.button_bg, fg=self.button_fg)
        self.info_button.pack(anchor="ne", padx=10, pady=10)

        # Create a button to open the file dialog
        self.open_button = tk.Button(self.root, text="Open File", command=self.open_file_dialog, bg=self.button_bg, fg=self.button_fg)
        self.open_button.pack(padx=20, pady=20)

        # Create a check button for custom libraries
        self.custom_lib_checkbutton = tk.Checkbutton(self.root, text="Use Custom Library", variable=self.custom_lib_var, bg=self.background_color, fg=self.text_color)
        self.custom_lib_checkbutton.pack()


def main():
    r_win = RootWin()
    r_win.run()


if __name__ == "__main__":
    main()
