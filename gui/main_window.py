# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel
# from PyQt5.QtCore import Qt
# from microscope_system.microscope_control.microscope import Microscope
# from microscope_system.autofocus.amplitude_autofocus import AmplitudeAutofocus
# from microscope_system.autofocus.phase_autofocus import PhaseAutofocus

# class MicroscopeGUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.microscope = None
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Microscope Control')
#         self.setGeometry(100, 100, 400, 300)

#         layout = QVBoxLayout()

#         self.config_label = QLabel('No configuration file selected', self)
#         layout.addWidget(self.config_label)

#         self.config_button = QPushButton('Select Configuration File', self)
#         self.config_button.clicked.connect(self.select_config)
#         layout.addWidget(self.config_button)

#         self.capture_button = QPushButton('Capture Image', self)
#         self.capture_button.clicked.connect(self.capture_image)
#         self.capture_button.setEnabled(False)
#         layout.addWidget(self.capture_button)

#         self.autofocus_button = QPushButton('Auto Focus', self)
#         self.autofocus_button.clicked.connect(self.auto_focus)
#         self.autofocus_button.setEnabled(False)
#         layout.addWidget(self.autofocus_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def select_config(self):
#         options = QFileDialog.Options()
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select Configuration File", "",
#                                                   "Configuration Files (*.cfg);;All Files (*)", options=options)
#         if fileName:
#             self.config_label.setText(f'Selected: {fileName}')
#             self.microscope = Microscope(fileName)
#             self.capture_button.setEnabled(True)
#             self.autofocus_button.setEnabled(True)

#     def capture_image(self):
#         if self.microscope:
#             image = self.microscope.capture_image()
#             # Add code to display or save the image
#             print("Image captured")

#     def auto_focus(self):
#         if self.microscope:
#             result = self.microscope.auto_focus(strategy=AmplitudeAutofocus, start=1350, end=1400)
#             print(f"Autofocus result: {result}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MicroscopeGUI()
#     ex.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, 
                             QFileDialog, QLabel, QComboBox, QHBoxLayout, QGroupBox)
from PyQt5.QtCore import Qt
from microscope_system.microscope_control.microscope import Microscope
from microscope_system.microscope_control.strategy_registry import strategy_registry

class MicroscopeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.microscope = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Microscope Control')
        self.setGeometry(100, 100, 500, 400)

        main_layout = QVBoxLayout()

        # Configuration file selection
        config_layout = QHBoxLayout()
        self.config_label = QLabel('No configuration file selected', self)
        self.config_button = QPushButton('Select Configuration File', self)
        self.config_button.clicked.connect(self.select_config)
        config_layout.addWidget(self.config_label)
        config_layout.addWidget(self.config_button)
        main_layout.addLayout(config_layout)

        # Strategy selection
        strategy_group = QGroupBox("Strategy Selection")
        strategy_layout = QVBoxLayout()

        self.autofocus_combo = QComboBox()
        self.autofocus_combo.addItems(strategy_registry.get_autofocus_names())
        self.autofocus_combo.currentTextChanged.connect(self.change_autofocus)
        strategy_layout.addWidget(QLabel("Autofocus Strategy:"))
        strategy_layout.addWidget(self.autofocus_combo)

        self.cell_identifier_combo = QComboBox()
        self.cell_identifier_combo.addItems(strategy_registry.get_cell_identifier_names())
        self.cell_identifier_combo.currentTextChanged.connect(self.change_cell_identifier)
        strategy_layout.addWidget(QLabel("Cell Identifier Strategy:"))
        strategy_layout.addWidget(self.cell_identifier_combo)

        self.cell_selector_combo = QComboBox()
        self.cell_selector_combo.addItems(strategy_registry.get_cell_selector_names())
        self.cell_selector_combo.currentTextChanged.connect(self.change_cell_selector)
        strategy_layout.addWidget(QLabel("Cell Selector Strategy:"))
        strategy_layout.addWidget(self.cell_selector_combo)

        self.cell_processor_combo = QComboBox()
        self.cell_processor_combo.addItems(strategy_registry.get_cell_processor_names())
        self.cell_processor_combo.currentTextChanged.connect(self.change_cell_processor)
        strategy_layout.addWidget(QLabel("Cell Processor Strategy:"))
        strategy_layout.addWidget(self.cell_processor_combo)

        strategy_group.setLayout(strategy_layout)
        main_layout.addWidget(strategy_group)

        # Action buttons
        self.capture_button = QPushButton('Capture Image', self)
        self.capture_button.clicked.connect(self.capture_image)
        self.capture_button.setEnabled(False)
        main_layout.addWidget(self.capture_button)

        self.autofocus_button = QPushButton('Auto Focus', self)
        self.autofocus_button.clicked.connect(self.auto_focus)
        self.autofocus_button.setEnabled(False)
        main_layout.addWidget(self.autofocus_button)

        self.run_button = QPushButton('Run Analysis', self)
        self.run_button.clicked.connect(self.run_analysis)
        self.run_button.setEnabled(False)
        main_layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(main_layout)
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
            self.run_button.setEnabled(True)

    def capture_image(self):
        if self.microscope:
            image = self.microscope.capture_image()
            # Add code to display or save the image
            print("Image captured")

    def auto_focus(self):
        if self.microscope and self.microscope.autofocus:
            result = self.microscope.auto_focus(start=1350, end=1400)
            print(f"Autofocus result: {result}")
        else:
            print("Autofocus strategy not set or microscope not initialized")

    def change_autofocus(self, strategy_name):
        if self.microscope:
            self.microscope.set_autofocus(strategy_name)

    def change_cell_identifier(self, strategy_name):
        if self.microscope:
            self.microscope.set_cell_identifier(strategy_name)

    def change_cell_selector(self, strategy_name):
        if self.microscope:
            self.microscope.set_cell_selector(strategy_name)

    def change_cell_processor(self, strategy_name):
        if self.microscope:
            self.microscope.set_cell_processor(strategy_name)

    def run_analysis(self):
        if self.microscope:
            try:
                results = self.microscope.run_analysis()
                print("Analysis completed. Results:", results)
            except ValueError as e:
                print(f"Error during analysis: {str(e)}")
        else:
            print("Microscope not initialized")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MicroscopeGUI()
    ex.show()
    sys.exit(app.exec_())