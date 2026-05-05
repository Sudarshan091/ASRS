<div align="center">
  <h1>🛡️ ASSRS</h1>
  <h3>Advanced Sensor & Strategy Response System</h3>
  <p><i>A full-stack, real-time telemetry and threat classification web application built to demonstrate advanced Python concepts.</i></p>

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
  ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
  ![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)

</div>

---

## 📖 Overview

**ASSRS** (Advanced Sensor & Strategy Response System) is a powerful simulation architecture. Originally designed to test deep Python proficiencies, it has evolved into a fully-fledged web application. 

The backend acts as a high-performance **Mission Control Engine**, ingesting raw simulated drone data, filtering noise, and asynchronously classifying active threats using a hierarchical Object-Oriented engine. The frontend is a visually stunning, glassmorphic React dashboard that displays the telemetry and threat classifications in real time.

---

## ⚡ Features

- **Asynchronous Telemetry:** Processes hundreds of sensor readings concurrently without blocking the main thread.
- **Dynamic Threat Engine:** Uses advanced Object-Oriented Programming (MRO, multiple inheritance, ABCs) to classify incoming entities (e.g., *Stealth UAVs*, *Armored Vehicles*).
- **Automated Data Cleansing:** Raw sensor inputs are aggressively filtered using complex list comprehensions, sets, and double-ended queues (`deque`).
- **Secure Mock Protocol:** Implements cryptographic token generation and SHA-256 payload hashing for secure mock communication.
- **Premium User Interface:** A modern, highly responsive React frontend featuring dynamic micro-animations, glassmorphism, and neon-themed UI elements.

---

## 🧠 Core Architecture & Python Concepts

The backend is modularized to strictly test and implement advanced Python mechanics:

| Module | Core Responsibility | Advanced Concepts Utilized |
| :--- | :--- | :--- |
| **`sensor_core.py`** | Raw data ingestion and noise filtration. | `List comprehensions`, `Dicts`, `Sets`, `collections.deque` |
| **`threat_engine.py`** | Threat categorization and classification. | `Classes`, `ABC`, `@property`, `Multiple Inheritance`, `MRO` |
| **`mission_control.py`** | Handling massive parallel sensor reports. | `asyncio`, `asyncio.gather`, `Coroutines` |
| **`comms_protocol.py`** | Encrypting and validating data integrity. | `hashlib`, `secrets`, `Socket` architecture design |
| **`audit_log.py`** | System logging and critical failure handling. | `Context Managers (with)`, `Custom Exceptions`, `logging` |
| **`telemetry.py`** | Streaming massive datasets efficiently. | `Generators (yield)`, File I/O |
| **`utils.py`** | Functional operations and performance metrics. | `Decorators (@timer)`, `map`, `filter`, `lambda` |

> *Note: The entire Python codebase is strictly typed to be compatible with `mypy` static type checking.*

---

## 🚀 Getting Started

Follow these instructions to get the full-stack system running on your local machine.

### Prerequisites
- Python 3.8+
- Node.js & npm

### 1. Start the Backend (FastAPI Engine)
The backend requires a virtual environment and standard Python dependencies.

```bash
# Clone the repository
git clone https://github.com/Sudarshan091/ASRS.git
cd ASRS

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn api_app:app --host 0.0.0.0 --port 8000
```
*The backend API will now be running on `http://localhost:8000`.*

### 2. Start the Frontend (React Dashboard)
Open a **new terminal window/tab**, and navigate into the `frontend` directory.

```bash
cd ASRS/frontend

# Install Node modules
npm install

# Start the Vite development server
npm run dev
```
*The React dashboard will now be running on `http://localhost:5173`.*

---

## 🌐 API Endpoints

The FastAPI backend exposes the following endpoints to power the dashboard:
- `GET /api/status`: Returns current system uptime, encryption status, and active sensor count.
- `GET /api/mission`: Asynchronously fires off `collect_all_sensors()` and returns the cleansed telemetry data.
- `GET /api/threats`: Invokes the OOP Threat Engine to generate, classify, and sort current threats dynamically.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! If you want to expand the Threat Engine classes or improve the React dashboard UI, feel free to fork the repository and submit a Pull Request.
