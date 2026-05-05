from abc import ABC, abstractmethod
from typing import Any
from .utils import timer

class Target(ABC):
    def __init__(self, target_id: str, distance: float) -> None:
        self.target_id = target_id
        self._distance = distance
        
    @property
    def distance(self) -> float:
        return self._distance
        
    @distance.setter
    def distance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Distance cannot be negative")
        self._distance = value

    @abstractmethod
    def classify(self) -> str:
        pass

class StealthTrait:
    def detection_modifier(self) -> float:
        return 0.5 # 50% harder to detect

    def classify(self) -> str:
        return "Stealth Target"

class UAV(Target):
    def classify(self) -> str:
        return "UAV - Hostile Recon"

class StealthUAV(StealthTrait, UAV):
    """
    Demonstrates Multiple Inheritance and MRO.
    Method Resolution Order will look at StealthTrait first for classify().
    """
    @timer
    def classify(self) -> str:
        # Resolves to StealthTrait.classify() if super() is called
        return f"{super().classify()} - Fast Moving"

class ArmoredVehicle(Target):
    def classify(self) -> str:
        return "Armored Vehicle - Heavy Threat"
