from argparse import ArgumentParser
from src.enums import *
from src.experiments import BNExperiment, conduct_experiment
from src.plotting import plot_results


def map_ternary_to_enum(ternary_value, positive_enum, negative_enum):
    return None if ternary_value == -1 else positive_enum if ternary_value == 1 else negative_enum


def get_evidence():
    parser = ArgumentParser(description="Bayesian Network for Car Engine Problem Diagnosis")
    parser.add_argument("--weather", type=int, choices=[0, 1, -1], default=-1,
                        help="Set the weather condition: 0 for harsh, 1 for normal, -1 for randomized")
    parser.add_argument("--car_maintenance", type=int, choices=[0, 1, -1], default=-1,
                        help="Set the car maintenance status: 0 for poorly maintained, "
                             "1 for well maintained, -1 for randomized")
    parser.add_argument("--battery_age", type=int, choices=[0, 1, -1], default=-1,
                        help="Set the battery age: 0 for old, 1 for new, -1 for randomized")
    parser.add_argument("--electrical_system", type=int, choices=[0, 1, -1], default=-1,
                        help="Set the electrical system status: 0 for faulty, 1 for functional, -1 for randomized")
    parser.add_argument("--engine_noise", type=int, choices=[0, 1, -1], default=-1,
                        help="Set the engine noise level: 0 for noisy, 1 for normal, -1 for randomized")

    args = parser.parse_args()

    weather = map_ternary_to_enum(args.weather, Weather.NORMAL.value, Weather.HARSH.value)
    car_maintenance = map_ternary_to_enum(args.car_maintenance, Maintenance.WELL_MAINTAINED.value,
                                          Maintenance.POORLY_MAINTAINED.value)
    battery_age = map_ternary_to_enum(args.battery_age, BatteryAge.NEW.value, BatteryAge.OLD.value)
    electrical_system = map_ternary_to_enum(args.electrical_system, ElectricalSystem.FUNCTIONAL.value,
                                            ElectricalSystem.FAULTY.value)
    engine_noise = map_ternary_to_enum(args.engine_noise, EngineNoise.NORMAL.value, EngineNoise.NOISY.value)

    return {
        "weather": weather,
        "car_maintenance": car_maintenance,
        "battery_age": battery_age,
        "electrical_system": electrical_system,
        "engine_noise": engine_noise
    }


def main():
    evidence = get_evidence()
    experiment = BNExperiment(evidence, [], ["engine_start"])
    experiment_results = conduct_experiment(experiment)
    plot_results(experiment_results[0].results["engine_start"], experiment)


if __name__ == "__main__":
    main()
