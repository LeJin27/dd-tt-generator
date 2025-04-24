import tkinter as tk
from tkinter import filedialog
from Generator import Generator


class GeneratorGui:
    def __init__(self):
        self.files = {
            'effect_file': '',
            'buff_file': '',
            'loc_file': ''
        }

    def select_file(self, label, file_type: str):
        file_selected = filedialog.askopenfile(mode='r')
        if file_selected:
            file_path = file_selected.name
            label.config(text=f"Selected file: {file_path}")
            self.files[file_type] = file_path
            file_selected.close()

    def confirm_file_changes(self):
        if self.files['effect_file'] != '': 
            print(self.files['effect_file'])
        if self.files['buff_file'] != '': 
            print(self.files['buff_file'])
        if self.files['loc_file'] != '': 
            print(self.files['loc_file'])

    '''
    def select_effect_file(self, label):
        self.select_file(label, 'effect')

    def select_buff_file(self, label):
        self.select_file(label, 'buff')

    def select_loc_file(self, label):
        self.select_file(label, 'loc')
    '''


def main():
    gi = GeneratorGui()
    window = tk.Tk()
    window.title("Select Folders")

    # Skill Name
    frame1 = tk.Frame(window)
    tk.Label(frame1, text="Skill Name:").pack(side="left")
    txt1 = tk.Text(frame1, height=1, width=90)
    txt1.pack(side="left")
    frame1.pack(pady=2)

    # Tooltip Extension
    frame2 = tk.Frame(window)
    tk.Label(frame2, text="Tooltip Extension:").pack(side="left")
    txt2 = tk.Text(frame2, height=1, width=90)
    txt2.pack(side="left")
    frame2.pack(pady=2)

    # Effect File Selector
    frame3 = tk.Frame(window)
    effect_button = tk.Button(frame3, text="Select Effects File", command=lambda: gi.select_file(effect_label, 'effect_file'))
    effect_button.pack(side="left")
    effect_label = tk.Label(frame3, text="No file selected", anchor="w", width=60)
    effect_label.pack(side="left", padx=10)
    frame3.pack(pady=2)

    # Buffs File Selector
    frame4 = tk.Frame(window)
    buff_button = tk.Button(frame4, text="Select Buffs File", command=lambda: gi.select_file(buff_label, 'buff_file'))
    buff_button.pack(side="left")
    buff_label = tk.Label(frame4, text="No file selected", anchor="w", width=60)
    buff_label.pack(side="left", padx=10)
    frame4.pack(pady=2)

    # Localization File Selector
    frame5 = tk.Frame(window)
    loc_button = tk.Button(frame5, text="Select Localization File", command=lambda: gi.select_file(loc_label, 'loc_file'))
    loc_button.pack(side="left")
    loc_label = tk.Label(frame5, text="No file selected", anchor="w", width=60)
    loc_label.pack(side="left", padx=10)
    frame5.pack(pady=2)


    frame6 = tk.Frame(window)
    confirm_button = tk.Button(frame6, text="Confirm", command=lambda: gi.confirm_file_changes())
    confirm_button.pack(side="left")
    confirm_label = tk.Label(frame6, text="No file selected", anchor="w", width=60)
    confirm_label.pack(side="left", padx=10)
    frame6.pack(pady=2)
  




    # Start the GUI loop
    window.mainloop()


if __name__ == "__main__":
    main()
