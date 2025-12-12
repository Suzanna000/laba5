import os
import sqlite3
import sys

try:
	from PyQt5 import QtWidgets, QtCore
except Exception:
	from PyQt5 import QtWidgets, QtCore


class DatabaseApp(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('SQLite GUI')
		self.db_path = os.path.join(os.getcwd(), 'data.db')
		self._ensure_db()
		self._create_widgets()
		self._load_data()

	def _ensure_db(self):
		conn = sqlite3.connect(self.db_path)
		cur = conn.cursor()
		cur.execute('''CREATE TABLE IF NOT EXISTS people
					   (id INTEGER PRIMARY KEY AUTOINCREMENT,
						name TEXT NOT NULL,
						age INTEGER NOT NULL)''')
		conn.commit()
		conn.close()

	def _create_widgets(self):
		layout = QtWidgets.QVBoxLayout(self)
		form = QtWidgets.QHBoxLayout()
		self.name_edit = QtWidgets.QLineEdit()
		self.name_edit.setPlaceholderText('Name')
		self.age_edit = QtWidgets.QSpinBox()
		self.age_edit.setRange(0, 200)
		add_btn = QtWidgets.QPushButton('Add')
		add_btn.clicked.connect(self._add_record)
		form.addWidget(self.name_edit)
		form.addWidget(self.age_edit)
		form.addWidget(add_btn)
		layout.addLayout(form)
		self.table = QtWidgets.QTableWidget()
		self.table.setColumnCount(3)
		self.table.setHorizontalHeaderLabels(['id', 'name', 'age'])
		self.table.horizontalHeader().setSectionResizeMode(
			QtWidgets.QHeaderView.Stretch)
		layout.addWidget(self.table)
		refresh_btn = QtWidgets.QPushButton('Refresh')
		refresh_btn.clicked.connect(self._load_data)
		layout.addWidget(refresh_btn)

	def _add_record(self):
		name = self.name_edit.text().strip()
		age = int(self.age_edit.value())
		if not name:
			return
		conn = sqlite3.connect(self.db_path)
		cur = conn.cursor()
		cur.execute('INSERT INTO people(name, age) VALUES(?, ?)', (name, age))
		conn.commit()
		conn.close()
		self.name_edit.clear()
		self._load_data()

	def _load_data(self):
		conn = sqlite3.connect(self.db_path)
		cur = conn.cursor()
		cur.execute('SELECT id, name, age FROM people')
		rows = cur.fetchall()
		conn.close()
		self.table.setRowCount(len(rows))
		for r, row in enumerate(rows):
			for c, val in enumerate(row):
				item = QtWidgets.QTableWidgetItem(str(val))
				self.table.setItem(r, c, item)


def main():
	app = QtWidgets.QApplication(sys.argv)
	win = DatabaseApp()
	win.resize(480, 320)
	win.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

