import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
from PyQt5.QtCore import Qt
from microscope_system.microscope_control.microscope import Microscope
from microscope_system.autofocus.amplitude_autofocus import AmplitudeAutofocus
from microscope_system.autofocus.phase_autofocus import PhaseAutofocus

class MicroscopeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.microscope = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Microscope Control')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.config_label = QLabel('No configuration file selected', self)
        layout.addWidget(self.config_label)

        self.config_button = QPushButton('Select Configuration File', self)
        self.config_button.clicked.connect(self.select_config)
        layout.addWidget(self.config_button)

        self.capture_button = QPushButton('Capture Image', self)
        self.capture_button.clicked.connect(self.capture_image)
        self.capture_button.setEnabled(False)
        layout.addWidget(self.capture_button)

        self.autofocus_button = QPushButton('Auto Focus', self)
        self.autofocus_button.clicked.connect(self.auto_focus)
        self.autofocus_button.setEnabled(False)
        layout.addWidget(self.autofocus_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def select_config(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Configuration File", "",
                                                  "Configuration Files (*.cfg);;All Files (*)", options=options)
        if fileName:
            self.config_label.setText(f'Selected: {fileName}')
            self.microscope = Microscope(fileName)
            self.capture_button.setEnabled(True)
            self.autofocus_button.setEnabled(True)

    def capture_image(self):
        if self.microscope:
            image = self.microscope.capture_image()
            # Add code to display or save the image
            print("Image captured")

    def auto_focus(self):
        if self.microscope:
            result = self.microscope.auto_focus(strategy=AmplitudeAutofocus, start=1350, end=1400)
            print(f"Autofocus result: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MicroscopeGUI()
    ex.show()
    sys.exit(app.exec_())