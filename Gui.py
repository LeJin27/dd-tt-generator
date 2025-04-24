import tkinter as tk
from tkinter import filedialog
from Generator import Generator


class GeneratorGui:
    def __init__(self):
        self.files = {
            'effect': '',
            'buff': '',
            'loc': ''
        }

    def select_file(self, label, file_type: str):
        file_selected = filedialog.askopenfile(mode='r')
        if file_selected:
            file_path = file_selected.name
            label.config(text=f"Selected file: {file_path}")
            self.files[file_type] = file_path
            file_selected.close()

    '''
    def select_effect_file(self, label):
        self.select_file(label, 'effect')

    def select_buff_file(self, label):
        self.select_file(label, 'buff')

    def select_loc_file(self, label):
        self.select_file(label, 'loc')
    '''


def main():
    # initalize generator instance
    gi = GeneratorGui()

    # Create the main window
    window = tk.Tk()
    window.title("Select Folders")

    effects_label = tk.Label(window, text="No folder selected")
    effects_button = tk.Button(
        window, text="Select Effects File", command=lambda: gi.select_effect_file(effects_label))

    frame1 = tk.Frame(window)
    txt1_label = tk.Label(frame1, text="Skill Name:")
    txt1 = tk.Text(frame1, height=1, width=90)
    txt1_label.pack(side="left")
    txt1.pack(side="left")
    frame1.pack()

    frame2 = tk.Frame(window)
    txt2_label = tk.Label(frame2, text="Count:")
    txt2 = tk.Text(frame2, height=1, width=90)
    txt2_label.pack(side="left")
    txt2.pack(side="left")
    frame2.pack()

    # Pack everything
    effects_button.pack()
    effects_label.pack()

    # Start the GUI loop
    window.mainloop()


if __name__ == "__main__":
    main()
