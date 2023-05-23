from PySide6.QtWidgets import QSpinBox

def h_m_s_to_seconds(h: int, m: int, s: int) -> int:
    """Convert hours, minutes and seconds to seconds.
    
    Args:
        h (int): Hours.
        m (int): Minutes.
        s (int): Seconds.
    
    Returns:
        int: Seconds.
    """
    return h * 3600 + m * 60 + s

def seconds_to_h_m_s(seconds: int) -> str:
    """Convert seconds to hours, minutes and seconds.
    
    Args:
        seconds (int): Seconds.
        
    Returns:
        str: Hours, minutes and seconds in format HH:MM:SS.
    """
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def seconds_to_time_ui(seconds: int, sp_h: QSpinBox, sp_m: QSpinBox, sp_s: QSpinBox):
    """Convert seconds to hours, minutes and seconds and set the values in the UI.
    
    Args:
        seconds (int): Seconds.
        sp_h (QSpinBox): Hours spin box.
        sp_m (QSpinBox): Minutes spin box.
        sp_s (QSpinBox): Seconds spin box.
    """

    h, m, s = seconds_to_h_m_s(seconds).split(":")
    
    sp_h.setValue(int(h))
    sp_m.setValue(int(m))
    sp_s.setValue(int(s))

def time_ui_to_seconds(sp_h: QSpinBox, sp_m: QSpinBox, sp_s: QSpinBox) -> int:
    """Convert hours, minutes and seconds from the UI to seconds.
    
    Args:
        sp_h (QSpinBox): Hours spin box.
        sp_m (QSpinBox): Minutes spin box.
        sp_s (QSpinBox): Seconds spin box.
    
    Returns:
        int: Total seconds.
    """
    h = sp_h.value()
    m = sp_m.value()
    s = sp_s.value()
    return h_m_s_to_seconds(h, m, s)

