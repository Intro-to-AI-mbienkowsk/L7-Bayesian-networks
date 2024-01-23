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


class EngineProblem(Enum):
    PROBLEM = "Problem"
    NO_PROBLEM = "No Problem"
