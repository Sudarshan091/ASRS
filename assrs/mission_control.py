import asyncio
import random
from typing import List, Dict

async def fetch_sensor_data(sensor_id: int) -> Dict[str, float]:
    """Simulate fetching data from a single sensor asynchronously."""
    # Simulate network delay for CPU-bound or network tasks
    await asyncio.sleep(random.uniform(0.01, 0.1))
    return {
        "sensor_id": float(sensor_id),
        "x": random.uniform(0, 100),
        "y": random.uniform(0, 100)
    }

async def collect_all_sensors(num_sensors: int = 100) -> List[Dict[str, float]]:
    """Simulates multiple sensors reporting simultaneously using asyncio.gather."""
    tasks = [fetch_sensor_data(i) for i in range(num_sensors)]
    results = await asyncio.gather(*tasks)
    return results

def run_mission_control() -> None:
    print("Starting Mission Control...")
    # asyncio.run is the entry point for the async program
    results = asyncio.run(collect_all_sensors(100))
    print(f"Collected data from {len(results)} sensors simultaneously without blocking.")
