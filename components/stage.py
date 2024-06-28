from microscope_system.microscope_control.controller import Controller

# Class representing the microscope stage.
class Stage:
    def __init__(self, controller: Controller):
        self.controller = controller
        self.focus_device = self.controller.get_focus_device()
        self.xy_stage_device = self.controller.get_xy_stage_device()
        self.x = self.controller.get_x_position()
        self.y = self.controller.get_y_position()
        self.z = self.controller.get_position()
    
    # Move the stage to the specified position.
    def move(self, x: float = None, y: float = None, z: float = None) -> None:
        if x is not None and y is not None:
            self.controller.set_xy_position(x, y)
            self.x, self.y = x, y
        if z is not None:
            self.controller.set_position(z)
            self.z = z

    # Get the current position of the stage.
    def get_position(self) -> tuple[float, float, float]:
        self.x = self.controller.get_x_position()
        self.y = self.controller.get_y_position()
        self.z = self.controller.get_position()
        return self.x, self.y, self.z