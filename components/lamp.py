from microscope_system.microscope_control.controller import Controller

# Class representing the microscope lamp.
class Lamp:
    def __init__(self, controller: Controller):
        self.controller = controller

    # Turn the lamp on.
    def set_on(self) -> None:
        self.controller.set_property("TransmittedLamp", "State", "On")
    
    # Turn the lamp off.
    def set_off(self) -> None:
        self.controller.set_property("TransmittedLamp", "State", "Off")

    # Get the current state of the lamp.
    def get_state(self) -> str:
        return self.controller.get_property("TransmittedLamp", "State")