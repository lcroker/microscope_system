import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from microscope_system.gui.main_window import MicroscopeGUI
from PyQt5.QtWidgets import QApplication
from microscope_system.microscope_control.strategy_registry import strategy_registry
from microscope_system.autofocus.bright_spot_autofocus import BrightSpotAutofocus
from microscope_system.autofocus.bright_field_autofocus import BrightFieldAutofocus
from microscope_system.autofocus.laser_autofocus import LaserAutofocus
from microscope_system.autofocus.raman_spectra_autofocus import RamanSpectraAutofocus
from microscope_system.autofocus.phase_autofocus import PhaseAutofocus
from microscope_system.autofocus.amplitude_autofocus import AmplitudeAutofocus
from microscope_system.cell_processing.bright_spot_cell_identifier import BrightSpotCellIdentifier
from microscope_system.cell_processing.isolated_cell_selector import IsolatedCellSelector
from microscope_system.cell_processing.raman_cell_processor import RamanCellProcessor

def register_strategies():
    strategy_registry.register_autofocus("BrightSpot", BrightSpotAutofocus)
    strategy_registry.register_autofocus("BrightField", BrightFieldAutofocus)
    strategy_registry.register_autofocus("Laser", LaserAutofocus)
    strategy_registry.register_autofocus("RamanSpectra", RamanSpectraAutofocus)
    strategy_registry.register_autofocus("Phase", PhaseAutofocus)
    strategy_registry.register_autofocus("Amplitude", AmplitudeAutofocus)
    strategy_registry.register_cell_identifier("BrightSpot", BrightSpotCellIdentifier)
    strategy_registry.register_cell_selector("Isolated", IsolatedCellSelector)
    strategy_registry.register_cell_processor("Raman", RamanCellProcessor)

if __name__ == '__main__':
    register_strategies()
    app = QApplication(sys.argv)
    gui = MicroscopeGUI()
    gui.show()
    sys.exit(app.exec_())