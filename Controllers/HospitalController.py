from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from Views.hospital_info import Dialog


class HospitalController(QWidget, Dialog):

	def __init__(self, hospital, parent=None):
		super().__init__(parent)
		self.parent = parent
		self.setupUi(self)
		self.setWindowFlag(Qt.Window)
		self.acceptButton.clicked.connect(self.close)
		self.hospitalId.setText(str(hospital[0]))
		self.hospitalName.setText(hospital[1])
