from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

class PlotWidget(QWidget):
    def __init__(self, data, parent=None):
        QWidget.__init__(self)
        self.setParent(parent)

        x, *ys = data.transpose()

        self.layout = QGridLayout(self)

        self.figure_canvas = FigureCanvas(Figure(figsize=(8, 9)))
        self.layout.addWidget(self.figure_canvas, 0, 0)

        self.ax = self.figure_canvas.figure.subplots()
        for y in ys:
            self.ax.plot(x, y)

        self.xlabel = QLabel(self)
        self.xlabel.setText('xlabel')
        self.layout.addWidget(self.xlabel, 0, 1)

        self.xedit = QLineEdit(self)
        self.xedit.textChanged.connect(self.change_xlabel)
        self.layout.addWidget(self.xedit, 1, 1)

        self.ylabel = QLabel(self)
        self.ylabel.setText('ylabel')
        self.layout.addWidget(self.ylabel, 2, 1)
        
        self.yedit = QLineEdit(self)
        self.yedit.textChanged.connect(self.change_ylabel)
        self.layout.addWidget(self.yedit, 3, 1)

        self.title_label = QLabel()
        self.title_label.setText('Title')
        self.layout.addWidget(self.title_label, 4, 1)

        self.title_edit = QLineEdit()
        self.title_edit.textChanged.connect(self.change_title)
        self.layout.addWidget(self.title_edit, 5, 1)

        self.grid_button = QCheckBox(self)
        self.grid_button.setText('grid')
        self.grid_button.clicked.connect(self.toggle_grid)
        self.layout.addWidget(self.grid_button, 6, 1)

    def toggle_grid(self, checked):
        if checked:
            self.ax.grid(visible=True)
        else:
            self.ax.grid(visible=False)

        self.figure_canvas.figure.canvas.draw()

    def change_color(self):
        self.line.set_color('red')
        self.figure_canvas.figure.canvas.draw()

    def change_xlabel(self, string):
        self.ax.set_xlabel(string)
        self.figure_canvas.figure.canvas.draw()

    def change_ylabel(self, string):
        self.ax.set_ylabel(string)
        self.figure_canvas.figure.canvas.draw()

    def change_title(self, string):
        self.ax.set_title(string)
        self.figure_canvas.figure.canvas.draw()