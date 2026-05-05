import time
from typing import Callable, Any, List, Dict

def timer(func: Callable) -> Callable:
    """Decorator to measure how fast the AI classifies a threat."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def sort_threats_by_distance(threats: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """Use map, filter, and lambda to quickly sort threats by distance."""
    # Filter only valid threats (e.g., positive distance) using filter and lambda
    valid_threats = filter(lambda t: t.get('distance', -1) >= 0, threats)
    # Sort by distance
    return sorted(valid_threats, key=lambda t: t['distance'])
