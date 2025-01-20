# toolpath_view.py
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPen, QColor

class ToolpathView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
    
    def draw_toolpath(self, toolpath):
        pen = QPen(QColor(0, 0, 255))
        for path in toolpath:
            self.scene.addLine(
                path['start'][0], path['start'][1],
                path['end'][0], path['end'][1],
                pen
            )
