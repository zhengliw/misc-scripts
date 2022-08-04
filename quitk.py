from tkinter import *
class Quitk(Tk):
    def __init__(self, title="Tk", appBgColor = "#000000", appFgColor = "#FFFFFF"):
        super().__init__()
        self.config(bg=appBgColor)
        self.geometry("600x450")
        self.title(title)
        self.bgcolor = appBgColor
        self.fgcolor = appFgColor
        self.entrylist = list()
    def quickButton(self, text, action):
        btn = Button(self ,text=text, command=action, bg = self.bgcolor, fg = self.fgcolor)
        btn.pack()
        return btn
    def quickText(self, text):
        lbl = Label(self, text=text, bg=self.bgcolor, fg=self.fgcolor)
        lbl.pack()
        return lbl
    def quickEntry(self):
        entry = Entry(self)
        self.entrylist.append(entry)
        entry.pack()
        return entry
    def focusNextEntry(self, event, this_index):
        entry_list = self.entrylist
        next_index = (this_index + 1) % len(entry_list)
        entry_list[next_index].focus_set()
    def run(self):

        entries = [child for child in self.winfo_children()
            if isinstance(child, Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Return>', lambda e, idx=idx: self.focusNextEntry(e, idx))
        
        self.mainloop()