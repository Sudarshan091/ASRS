from collections import deque
from typing import List, Dict, Set, Any

class SensorCore:
    def __init__(self) -> None:
        self.seen_ids: Set[str] = set()
        self.data_buffer: deque = deque(maxlen=1000)

    def cleanse_data(self, raw_data_stream: List[Dict[str, Any]]) -> List[Dict[str, float]]:
        """
        Data-cleansing pipeline filtering out 'noise' (sensor errors).
        Demonstrates list comprehensions, dictionary mapping, sets for unique IDs, and deque.
        """
        cleansed_data = []
        for data in raw_data_stream:
            # Check for missing coordinates or noise
            if 'x' not in data or 'y' not in data or 'id' not in data:
                continue
            
            # Type checking (simulating strict types)
            if not isinstance(data['x'], (int, float)) or not isinstance(data['y'], (int, float)):
                continue

            # Check unique ID tracking via sets
            if data['id'] in self.seen_ids:
                continue # Skip duplicate readings
            
            self.seen_ids.add(data['id'])
            
            cleansed_point = {
                'id': data['id'],
                'x': float(data['x']),
                'y': float(data['y'])
            }
            
            # Use deque for real-time data buffers
            self.data_buffer.append(cleansed_point)
            cleansed_data.append(cleansed_point)
            
        # Using list comprehension for returning positive quadrant only as an example of filtering
        return [point for point in cleansed_data if point['x'] >= 0 and point['y'] >= 0]
