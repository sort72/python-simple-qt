from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from Views.doctor_info import Dialog


class DoctorController(QWidget, Dialog):

	def __init__(self, doctor, parent=None):
		super().__init__(parent)
		self.parent = parent
		self.setupUi(self)
		self.setWindowFlag(Qt.Window)
		self.acceptButton.clicked.connect(self.close)
		self.doctorName.setText(doctor[1])
		self.doctorDni.setText(str(doctor[0]))
		self.hospitalName.setText(doctor[3])
		self.doctorSpeciality.setText(doctor[2])
