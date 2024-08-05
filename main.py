from tkinter import ttk  # install this (how: pip install tkinter)
import ttkbootstrap

root = ttkbootstrap.Window(themename='cyborg')
root.title("Calendar")


def see_date():
    date = cal.entry.get()
    date_label.config(text=date)


cal = ttkbootstrap.DateEntry(root, dateformat='%d/%m/%Y', bootstyle="info")
cal.pack(padx=40, pady=40)


btn = ttk.Button(root, text='Show Date',
                 bootstyle="light-outline", command=see_date)
btn.pack(padx=40, pady=45)
date_label = ttk.Label(root, text="No date selected")
date_label.pack(padx=40, pady=50)

root.mainloop()
