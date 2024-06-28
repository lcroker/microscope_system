# microscope_system/microscope_control/exceptions.py

class MicroscopeError(Exception):
    """Base exception class for microscope-related errors."""
    pass

class CameraError(MicroscopeError):
    """Exception raised for camera-related errors."""
    pass

class StageError(MicroscopeError):
    """Exception raised for stage-related errors."""
    pass

class LampError(MicroscopeError):
    """Exception raised for lamp-related errors."""
    pass