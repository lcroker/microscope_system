from microscope_system.cell_processing.base_cell_processor import BaseCellProcessor

class RamanCellProcessor(BaseCellProcessor):
    def process_cell(self, microscope, cell_position):
        microscope.move_stage(x=cell_position[1], y=cell_position[0])
        
        # Perform autofocus
        focus_z = microscope.auto_focus(start=microscope.stage.z - 10, end=microscope.stage.z + 10, step=0.5)
        microscope.move_stage(z=focus_z)
        
        # Capture Raman spectrum
        spectrum = microscope.capture_raman_spectrum()
        
        return spectrum, cell_position, focus_z