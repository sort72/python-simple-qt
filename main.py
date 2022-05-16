import Models.Persistence
from PySide2.QtWidgets import QApplication
from Controllers.SearchController import SearchController

def main():
	persistence = Models.Persistence.Persistence()
	# print(persistence.get_by_id(1))
	# print(persistence.get_by_id(3))
	# print(persistence.get_by_name('Rosales'))
	# print(persistence.get_by_name('San Jorge'))

	app = QApplication()
	window = SearchController(persistence)
	window.show()
	app.exec_()

main()