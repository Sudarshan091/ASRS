from typing import Generator, Dict, Any
import json
import os

def stream_telemetry(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """
    Use yield to stream large telemetry files without loading them into RAM.
    Assumes a JSON-lines format (one JSON object per line).
    """
    if not os.path.exists(file_path):
        yield {"error": f"File {file_path} not found"}
        return

    # Use context manager for file I/O
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                # Yielding one chunk/record at a time (Generator concept)
                yield json.loads(line)
            except json.JSONDecodeError:
                # Skip invalid JSON (noise)
                pass
