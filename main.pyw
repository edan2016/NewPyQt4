__author__ = 'edward'

from PyQt4.QtGui import QApplication, QMainWindow
from test import Ui_Form
# ------------------------------

# -------------------------------
if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	Form = QMainWindow()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
