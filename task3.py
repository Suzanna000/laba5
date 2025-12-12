import tkinter as tk


class Calculator(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Калькулятор')
		self.resizable(False, False)
		self._expr = ''
		self._create_widgets()

	def _create_widgets(self):
		self.display = tk.Entry(self, justify='right', font=('Arial', 18))
		self.display.grid(row=0, column=0, columnspan=4, sticky='nsew')
		buttons = [
			('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
			('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
			('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
			('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
		]
		for (text, r, c) in buttons:
			btn = tk.Button(self, text=text, width=4, height=2,
							font=('Arial', 14), command=lambda t=text: self._on_press(t))
			btn.grid(row=r, column=c, padx=2, pady=2)
		clear = tk.Button(self, text='C', width=18, height=2,
						  font=('Arial', 14), command=self._clear)
		clear.grid(row=5, column=0, columnspan=4, padx=2, pady=2)

	def _on_press(self, char):
		if char == '=':
			self._calculate()
			return
		self._expr += char
		self.display.delete(0, tk.END)
		self.display.insert(0, self._expr)

	def _calculate(self):
		try:
			result = str(eval(self._expr))
		except Exception:
			result = 'Ошибка'
		self._expr = '' if result == 'Ошибка' else result
		self.display.delete(0, tk.END)
		self.display.insert(0, result)

	def _clear(self):
		self._expr = ''
		self.display.delete(0, tk.END)


if __name__ == '__main__':
	app = Calculator()
	app.mainloop()

