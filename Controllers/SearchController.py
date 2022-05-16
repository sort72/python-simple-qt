from Controllers.DoctorController import DoctorController
from Controllers.HospitalController import HospitalController
from PySide2.QtWidgets import QWidget
from Views.main_window import AdministrationForm
from Controllers.NotFoundController import NotFoundController

class SearchController(QWidget,AdministrationForm):
	def __init__(self, persistence):
		super().__init__()
		self.persistence = persistence
		self.setupUi(self)
		self.searchDoctorButton.clicked.connect(self.search_doctor)
		self.searchHospitalButton.clicked.connect(self.search_hospital)

	def search_doctor(self):
		dni = self.dniDoctorEdit.text()
		if self.is_int(dni):		
			doctor = self.persistence.get_by_id(int(dni))
			if doctor:
				window = DoctorController(doctor, self)
				window.show()
			else:
				window = NotFoundController(self)
				window.show()

	def search_hospital(self):
		name = self.hospitalNameEdit.text()
		hospital = self.persistence.get_by_name(name)
		if hospital:
			window = HospitalController(hospital, self)
			window.show()
		else:
			window = NotFoundController(self)
			window.show()

	def is_int(self, val):
		try:
			num = int(val)
		except ValueError:
			return False
		return True
