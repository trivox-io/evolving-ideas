"""
evolving_ideas.common.logger
"""

import sys
import logging

class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors to log messages.
    """
    
    COLORS = {
        "DEBUG": "\033[94m",  # Blue
        "INFO": "\033[92m",   # Green
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[95m"  # Magenta
    }
    
    RESET = "\033[0m"  # Reset color
    
    def format(self, record):
        log_fmt = self._style._fmt  # Save format string
        color = self.COLORS.get(record.levelname, self.RESET)
        self._style._fmt = f"{color}{log_fmt}{self.RESET}"
        formatted = super().format(record)
        self._style._fmt = log_fmt  # Restore original format
        return formatted


def setup_logging(level=logging.DEBUG, silence_third_party: bool = True):
    """
    Initialize logging with color formatter and dynamic module names.
    Call once during startup.
    """
    format_ = "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s (%(filename)s:%(lineno)d)"
    formatter = ColorFormatter(format_)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()
    root.addHandler(handler)

    if silence_third_party:
        # Common noisy libraries
        noisy_loggers = [
            "httpcore",
            "openai",
            "httpx",
        ]
        for name in noisy_loggers:
            logging.getLogger(name).setLevel(logging.WARNING)
            logging.getLogger(name).propagate = False
