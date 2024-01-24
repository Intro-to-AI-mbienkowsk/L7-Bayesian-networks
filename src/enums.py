from enum import Enum


class Weather(Enum):
    NORMAL = "Normal"
    HARSH = "Harsh"


class Maintenance(Enum):
    WELL_MAINTAINED = "Well-Maintained"
    POORLY_MAINTAINED = "Poorly-Maintained"


class BatteryAge(Enum):
    NEW = "New"
    OLD = "Old"


class EngineStart(Enum):
    STARTS = "Starts"
    DOES_NOT_START = "Does Not Start"


class ElectricalSystem(Enum):
    FUNCTIONAL = "Functional"
    FAULTY = "Faulty"


class EngineNoise(Enum):
    NORMAL = "Normal"
    NOISY = "Noisy"


enum_values_from_string = {
    "weather": [Weather.HARSH.value, Weather.NORMAL.value],
    "car_maintenance": [Maintenance.WELL_MAINTAINED.value, Maintenance.POORLY_MAINTAINED.value],
    "battery_age": [BatteryAge.NEW.value, BatteryAge.OLD.value],
    "engine_start": [EngineStart.STARTS.value, EngineStart.DOES_NOT_START.value],
    "electrical_system": [ElectricalSystem.FUNCTIONAL.value, ElectricalSystem.FAULTY.value],
    "engine_noise": [EngineNoise.NORMAL.value, EngineNoise.NOISY.value]
}
