# pyqt_simulation.py
from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QColor

class SimulationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolpath Simulation")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

    def add_toolpath(self, toolpath):
        pen = QPen(QColor(255, 0, 0))
        for path in toolpath:
            self.scene.addLine(path['start'][0], path['start'][1], path['end'][0], path['end'][1], pen)
