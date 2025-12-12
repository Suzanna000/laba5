import tkinter as tk


class Clicker(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Кликер')
		self.resizable(False, False)
		self._count = 0
		self._auto = False
		self._create_widgets()

	def _create_widgets(self):
		self.label = tk.Label(self, text='0', font=('Arial', 24))
		self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
		btn = tk.Button(self, text='Клик', width=12, height=2,
						command=self._click)
		btn.grid(row=1, column=0, padx=6, pady=6)
		reset = tk.Button(self, text='Сброс', width=12, height=2,
						  command=self._reset)
		reset.grid(row=1, column=1, padx=6, pady=6)
		self.auto_btn = tk.Button(self, text='Авто: Выкл', width=26,
								  command=self._toggle_auto)
		self.auto_btn.grid(row=2, column=0, columnspan=2, padx=6, pady=6)

	def _click(self):
		self._count += 1
		self.label.configure(text=str(self._count))

	def _reset(self):
		self._count = 0
		self.label.configure(text='0')

	def _toggle_auto(self):
		self._auto = not self._auto
		self.auto_btn.configure(text='Авто: Вкл' if self._auto else 'Авто: Выкл')
		if self._auto:
			self._auto_click()

	def _auto_click(self):
		if not self._auto:
			return
		self._click()
		self.after(200, self._auto_click)


if __name__ == '__main__':
	app = Clicker()
	app.mainloop()

