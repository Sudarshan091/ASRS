import time
import logging
from typing import Type, Optional
from types import TracebackType

# Setup logging configuration
logging.basicConfig(
    filename='mission_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CriticalSystemFailure(Exception):
    """Custom exception for critical failures."""
    pass

class MissionAuditLog:
    """
    Custom context manager that automatically logs the start/end time of a mission
    and handles 'Critical System Failures' without crashing the entire program.
    """
    def __init__(self, mission_name: str) -> None:
        self.mission_name = mission_name
        self.start_time: float = 0.0

    def __enter__(self) -> 'MissionAuditLog':
        self.start_time = time.time()
        logging.info(f"MISSION START: {self.mission_name}")
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], 
                 exc_val: Optional[BaseException], 
                 exc_tb: Optional[TracebackType]) -> bool:
        
        end_time = time.time()
        duration = end_time - self.start_time
        
        if exc_type is not None:
            if issubclass(exc_type, CriticalSystemFailure):
                logging.error(f"CRITICAL SYSTEM FAILURE during {self.mission_name}: {exc_val}")
                # Suppress the exception so program doesn't crash
                logging.info(f"MISSION ABORTED: {self.mission_name} (Duration: {duration:.2f}s)")
                return True
            else:
                logging.exception(f"UNHANDLED EXCEPTION during {self.mission_name}")
                # Do not suppress other exceptions
                return False
                
        logging.info(f"MISSION SUCCESS: {self.mission_name} (Duration: {duration:.2f}s)")
        return True
