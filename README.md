# ASSRS (Advanced Sensor & Strategy Response System)

This project architecture implements various core Python concepts designed to test advanced proficiency.

## Modules

### Module A: The Sensor Core (`assrs/sensor_core.py`)
Handles raw data coming from drones.
- **Concepts**: List comprehensions, Dictionary mapping, Sets for unique ID tracking, `collections.deque` for real-time data buffers.

### Module B: The Threat Classification Engine (`assrs/threat_engine.py`)
Defense systems hierarchical logic.
- **Concepts**: Classes, Abstract Base Classes (ABC), Property Decorators (`@property`), Multiple Inheritance, Method Resolution Order (MRO).

### Module C: Mission Control Center (`assrs/mission_control.py`)
Asynchronous task management.
- **Concepts**: `asyncio.gather`, asynchronous functions.

### Module D: Secure Communication Protocol (`assrs/comms_protocol.py`)
Data encryption and secure sockets mapping.
- **Concepts**: Socket programming layout, `hashlib` for data integrity, `secrets` module for secure tokens.

### Module E: Strategic Audit Log (`assrs/audit_log.py`)
Logging framework.
- **Concepts**: Context Managers (`with` statement), Custom Exception handling, `logging` module.

### Utilities (`assrs/utils.py` & `assrs/telemetry.py`)
- **Decorators**: `@timer` to measure threat classification speed.
- **Generators**: `yield` statement to stream large telemetry files.
- **Type Hinting**: Strict `mypy` type hints used across all modules.
- **Functional Programming**: Uses `filter`, `lambda`, and built-ins to sort threats by distance.
- **Packaging**: Structured with `setup.py`, `requirements.txt`, and proper `__init__.py` files.
