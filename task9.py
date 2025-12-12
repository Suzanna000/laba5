import tkinter as tk
import random


class ColorPanel(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Цветная панель')
		self.resizable(False, False)
		self._create_widgets()

	def _create_widgets(self):
		self.panel = tk.Frame(self, width=300, height=200, bg='#ffffff')
		self.panel.grid(row=0, column=0, columnspan=2, padx=8, pady=8)
		self.label = tk.Label(self, text='#ffffff', font=('Arial', 12))
		self.label.grid(row=1, column=0, padx=8, pady=4, sticky='w')
		btn = tk.Button(self, text='Сменить цвет', command=self._change_color)
		btn.grid(row=1, column=1, padx=8, pady=4, sticky='e')

	def _change_color(self):
		color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
		self.panel.configure(bg=color)
		self.label.configure(text=color)


if __name__ == '__main__':
	app = ColorPanel()
	app.mainloop()

