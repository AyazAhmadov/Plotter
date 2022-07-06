from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

import numpy as np

from functions import csv_to_array
from widgets.plot_widget import PlotWidget

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.main_frame = QWidget()
        self.setCentralWidget(self.main_frame)
        self.layout = QGridLayout(self.main_frame)

        self.file_button = QPushButton(self)
        self.file_button.clicked.connect(self.save_window)
        self.layout.addWidget(self.file_button, 0, 0)

        self.show()

        # self.figure_canvas = FigureCanvas(Figure(figsize=(8, 9)))
        # self.layout.addWidget(self.figure_canvas, 0, 0)

        # self.ax = self.figure_canvas.figure.subplots()
        # t = np.linspace(0, 10, 501)
        # self.line, = self.ax.plot(t, np.sin(t))

    def save_window(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', filter='Text File (*.csv)')
        filename = 'china/data/pulse_1.csv'
        if filename:
            data = csv_to_array(filename)
            print(data)

            self.main_frame.deleteLater()
            self.plot_frame = PlotWidget(data, parent=self)
            self.layout.addWidget(self.plot_frame, 0, 0)