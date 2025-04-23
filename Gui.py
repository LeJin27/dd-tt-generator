import tkinter as tk
from tkinter import filedialog



class GeneratorGui:
    def __init__(self):
        self.effect = ''
        self.buff = ''
        self.loc = ''

    def select_file(label):
        file_selected = filedialog.askopenfile(mode='r')
        if file_selected:
            file_path = file_selected.name
            label.config(text=f"Selected folder: {file_path}")
            file_selected.close()


# Create the main window
window = tk.Tk()
window.title("Select Folders")

effects_label = tk.Label(window, text="No folder selected")
effects_button = tk.Button(window, text="Select Effects File", command=lambda: select_file(effects_label))

buffs_label = tk.Label(window, text="No folder selected")
buffs_button = tk.Button(window, text="Select Buffs File", command=lambda: select_file(buffs_label))





# Pack everything
effects_button.pack()
effects_label.pack()

buffs_button.pack()
buffs_label.pack()

# Start the GUI loop
window.mainloop()