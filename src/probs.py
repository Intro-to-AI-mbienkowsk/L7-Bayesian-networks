from enums import *

weather_probs = {Weather.NORMAL.value: 0.7, Weather.HARSH.value: 0.3}
maintenance_probs = {Maintenance.WELL_MAINTAINED.value: 0.6, Maintenance.POORLY_MAINTAINED.value: 0.4}
battery_age_probs = {BatteryAge.NEW.value: 0.5, BatteryAge.OLD.value: 0.5}

electrical_system_cpt_entries = [
    [Maintenance.WELL_MAINTAINED.value, ElectricalSystem.FUNCTIONAL.value, 0.9],
    [Maintenance.WELL_MAINTAINED.value, ElectricalSystem.FAULTY.value, 0.1],
    [Maintenance.POORLY_MAINTAINED.value, ElectricalSystem.FUNCTIONAL.value, 0.6],
    [Maintenance.POORLY_MAINTAINED.value, ElectricalSystem.FAULTY.value, 0.4]
]

engine_noise_cpt_entries = [
    [Maintenance.WELL_MAINTAINED.value, EngineNoise.NORMAL.value, 0.85],
    [Maintenance.WELL_MAINTAINED.value, EngineNoise.NOISY.value, 0.15],
    [Maintenance.POORLY_MAINTAINED.value, EngineNoise.NORMAL.value, 0.6],
    [Maintenance.POORLY_MAINTAINED.value, EngineNoise.NOISY.value, 0.4]
]

engine_start_cpt_entries = [
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.95],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.05],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.95],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.05],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.8],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.6],
    [Weather.NORMAL.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.4],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.8],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.6],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.4],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.8],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.6],
    [Weather.NORMAL.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.4],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.8],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.6],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.4],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.8],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.6],
    [Weather.HARSH.value, BatteryAge.NEW.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.4],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.8],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.6],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FUNCTIONAL.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.4],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.STARTS.value, 0.2],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NORMAL.value,
     EngineStart.DOES_NOT_START.value, 0.8],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.STARTS.value, 0.2],
    [Weather.HARSH.value, BatteryAge.OLD.value, ElectricalSystem.FAULTY.value, EngineNoise.NOISY.value,
     EngineStart.DOES_NOT_START.value, 0.8]
]
