from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TouchCheckbox(QCheckBox, QObject):
    # Signal is emitted once it has been selected
    pressed = pyqtSignal(bool, bool, name='clicked')

    def __init__(self, parent = None):
        super(TouchCheckbox, self).__init__(parent)

    def mousePressEvent(self, event):
        if self.hitButton(event.pos()):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                self.setDown(True)
                event.accept()

    def mouseReleaseEvent(self, event):
        if self.hitButton(event.pos()) and self.isDown():
            if event.button() == Qt.LeftButton:
                self.click()
                self.pressed.emit(self.isChecked(), False)
            elif event.button() == Qt.RightButton:
                self.click()
                self.pressed.emit(self.isChecked(), True)

            self.repaint()
        else:
            self.setDown(False)
