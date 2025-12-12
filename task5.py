import tkinter as tk
from tkinter import ttk


class NotebookApp(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Программа со вкладками')
		self.resizable(False, False)
		self._create_widgets()

	def _create_widgets(self):
		nb = ttk.Notebook(self)
		frame1 = ttk.Frame(nb)
		frame2 = ttk.Frame(nb)
		nb.add(frame1, text='Форма')
		nb.add(frame2, text='Текст')
		nb.grid(row=0, column=0, padx=8, pady=8)
		lbl = ttk.Label(frame1, text='Введите текст:')
		lbl.grid(row=0, column=0, padx=6, pady=6, sticky='w')
		self.entry = ttk.Entry(frame1, width=30)
		self.entry.grid(row=1, column=0, padx=6, pady=6)
		btn = ttk.Button(frame1, text='Показать', command=self._show)
		btn.grid(row=2, column=0, padx=6, pady=6)
		self.text = tk.Text(frame2, width=40, height=10)
		self.text.grid(row=0, column=0, padx=6, pady=6)

	def _show(self):
		value = self.entry.get()
		self.text.insert(tk.END, value + '\n')


if __name__ == '__main__':
	app = NotebookApp()
	app.mainloop()

