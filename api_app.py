from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from assrs.mission_control import collect_all_sensors
from assrs.threat_engine import UAV, ArmoredVehicle, StealthUAV
import asyncio
import random

app = FastAPI(title="ASSRS Mission Control API")

# Allow all CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/mission")
async def run_mission():
    """Runs a simulated sensor collection mission"""
    sensors_data = await collect_all_sensors(50) # fetch from 50 sensors
    return {"status": "success", "data": sensors_data}

@app.get("/api/threats")
async def get_threats():
    """Returns some classified threats using the threat engine."""
    # Simulate dynamic threats
    threats = []
    num_threats = random.randint(3, 8)
    for i in range(num_threats):
        dist = random.uniform(10.0, 500.0)
        t_type = random.choice([
            UAV(f"T-{i}", dist), 
            ArmoredVehicle(f"T-{i}", dist), 
            StealthUAV(f"T-{i}", dist)
        ])
        
        threats.append({
            "id": f"T-{random.randint(1000, 9999)}",
            "type": t_type.classify(),
            "distance": round(t_type.distance, 2)
        })
        
    # Sort by distance using lambda
    threats.sort(key=lambda t: t['distance'])
    return {"status": "success", "data": threats}

@app.get("/api/status")
async def get_system_status():
    """Returns general system status."""
    return {
        "status": "online",
        "encryption": "AES-256",
        "active_sensors": random.randint(80, 100)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
