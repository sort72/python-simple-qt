from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from Views.not_found import Dialog


class NotFoundController(QWidget, Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.acceptButton.clicked.connect(self.close)
