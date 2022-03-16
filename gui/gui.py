from tkinter import *
import gui.constants as cnst
import pyperclip

class Gui():
	def __init__(self, name, geometry_x, geometry_y):
		self.root = Tk()
		self.root.title(name)
		self.root.geometry(f"{geometry_x}x{geometry_y}")
		self.root.configure(bg=cnst.BG_COLOR)

	def refresh(self):
		self.entry.delete(0, END)
		self.entry.insert(0, pyperclip.paste())

	def pl_number_frame(self):
		self.nb_frame = Frame(master=self.root, borderwidth=5)
		self.nb_frame.configure(bg=cnst.BG_COLOR)
		self.nb_frame.pack(pady=20)

		self.nb_label = Label(master=self.nb_frame, text=" To ")
		self.nb_label.grid(padx=5, row=0, column=1)

		self.fst_entry = Entry(master=self.nb_frame, width=10)
		self.fst_entry.grid(row=0, column=0)
		
		self.scnd_entry = Entry(master=self.nb_frame, width=10)
		self.scnd_entry.grid(row=0, column=2)

		return (self.fst_entry, self.scnd_entry)

	def res_frame(self):
		self.r_frame = Frame(master=self.root, borderwidth=5)
		self.r_frame.configure(bg=cnst.BG_COLOR)
		self.r_frame.pack(pady=10)

		self.label = Label(master=self.r_frame, text=" Resolution:  ")
		self.label.grid(row=0, column=0)

		self.in_value = StringVar(self.r_frame)
		self.in_value.set(cnst.OPMENU_LIST[5])
		self.res_opmenu = OptionMenu(self.r_frame, self.in_value, *cnst.OPMENU_LIST)
		self.res_opmenu.grid(padx=5, row=0, column=1)

		return self.in_value

	def down_button(self, download):
		self.down_button = Button(master=self.r_frame, text=" Download ", font=cnst.DOWN_BTN_FONT, command=lambda: download(self.entry.get()))
		self.down_button.grid(row=0, column=2)

	def url_frame(self):
		self.u_frame = Frame(master=self.root, borderwidth=5)
		self.u_frame.configure(bg=cnst.BG_COLOR)
		self.u_frame.pack(pady=(50,10))

		self.label = Label(master=self.u_frame, text=" URL: ")
		self.label.grid(row=0, column=0)

		self.entry = Entry(master=self.u_frame, width=50)
		self.entry.insert(0, pyperclip.paste())
		self.entry.grid(padx=5, row=0, column=1)

		self.ref_button = Button(master=self.u_frame, text=" Refresh ", command=lambda: self.refresh(), borderwidth=2)
		self.ref_button.grid(row=0, column=2)
		
		return self.entry

	def loop(self):
		self.root.mainloop()