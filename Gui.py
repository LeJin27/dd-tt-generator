import tkinter as tk
from tkinter import filedialog
from Generator import Generator


class GeneratorGui:
    def __init__(self):
        self.generator = Generator()
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

    def clear_file(self, label, file_type: str):
        label.config(text=f"No file selected")
        self.files[file_type] = ''

    def confirm_file_changes(self, txt1, txt2, txt3):


        skill_name = txt1.get("1.0", "end-1c")
        tooltip_ext = txt2.get("1.0", "end-1c")
        description = txt3.get("1.0", "end-1c")

        if skill_name != '' and tooltip_ext != '':
            effect_file = self.files['effect_file']
            buff_file = self.files['buff_file']
            loc_file = self.files['loc_file']


            if effect_file != '': 
                self.generator.effect_file(skill_name, tooltip_ext, effect_file)

            if buff_file != '': 
                self.generator.buff_file(skill_name, tooltip_ext, buff_file)
            if loc_file != '': 
                self.generator.loc_file(skill_name, tooltip_ext, description, loc_file)

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

    # Skill Name
    frame0 = tk.Frame(window)
    tk.Label(frame0, text="Description:").pack(side="left")
    txt0 = tk.Text(frame0, height=1, width=90)
    txt0.pack(side="left")
    frame0.pack(pady=2)

    # Effect File Selector
    frame3 = tk.Frame(window)
    remove_3 = tk.Button(frame3, text="x", command=lambda: gi.clear_file(effect_label, 'effect_file'))
    remove_3.pack(side="left")
    effect_button = tk.Button(frame3, text="Select Effects File", command=lambda: gi.select_file(effect_label, 'effect_file'))
    effect_button.pack(side="left")
    effect_label = tk.Label(frame3, text="No file selected", anchor="w", width=60)
    effect_label.pack(side="left", padx=10)

    frame3.pack(pady=2)

    # Buffs File Selector
    frame4 = tk.Frame(window)
    remove_4 = tk.Button(frame4, text="x", command=lambda: gi.clear_file(buff_label, 'effect_file'))
    remove_4.pack(side="left")
    buff_button = tk.Button(frame4, text="Select Buffs File", command=lambda: gi.select_file(buff_label, 'buff_file'))
    buff_button.pack(side="left")
    buff_label = tk.Label(frame4, text="No file selected", anchor="w", width=60)
    buff_label.pack(side="left", padx=10)
    frame4.pack(pady=2)

    # Localization File Selector
    frame5 = tk.Frame(window)
    remove_5 = tk.Button(frame5, text="x", command=lambda: gi.clear_file(loc_label, 'effect_file'))
    remove_5.pack(side="left")
    loc_button = tk.Button(frame5, text="Select Localization File", command=lambda: gi.select_file(loc_label, 'loc_file'))
    loc_button.pack(side="left")
    loc_label = tk.Label(frame5, text="No file selected", anchor="w", width=60)
    loc_label.pack(side="left", padx=10)
    frame5.pack(pady=2)


    frame6 = tk.Frame(window)
    remove_6 = tk.Button(frame6, text="x", command=lambda: gi.select_file(effect_label, 'effect_file'))
    remove_6.pack(side="left")
    confirm_button = tk.Button(frame6, text="Confirm", command=lambda: gi.confirm_file_changes(txt1, txt2, txt0))
    confirm_button.pack(side="left")
    confirm_label = tk.Label(frame6, text="No file selected", anchor="w", width=60)
    confirm_label.pack(side="left", padx=10)
    frame6.pack(pady=2)
  




    # Start the GUI loop
    window.mainloop()


if __name__ == "__main__":
    main()
