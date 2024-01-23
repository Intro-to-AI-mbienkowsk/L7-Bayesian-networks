from pomegranate import *
from enums import *

# Discrete distributions for root nodes
weather = DiscreteDistribution({Weather.NORMAL.value: 0.7, Weather.HARSH.value: 0.3})
car_maintenance = DiscreteDistribution({Maintenance.WELL_MAINTAINED.value: 0.6, Maintenance.POORLY_MAINTAINED.value: 0.4})
battery_age = DiscreteDistribution({BatteryAge.NEW.value: 0.5, BatteryAge.OLD.value: 0.5})

# Conditional Probability Tables (CPTs)
engine_start_cpt = ConditionalProbabilityTable([
    [Weather.NORMAL.value, BatteryAge.NEW.value, EngineStart.STARTS.value, 0.95],
    [Weather.NORMAL.value, BatteryAge.NEW.value, EngineStart.DOES_NOT_START.value, 0.05],
    [Weather.NORMAL.value, BatteryAge.OLD.value, EngineStart.STARTS.value, 0.7],
    [Weather.NORMAL.value, BatteryAge.OLD.value, EngineStart.DOES_NOT_START.value, 0.3],
    [Weather.HARSH.value, BatteryAge.NEW.value, EngineStart.STARTS.value, 0.8],
    [Weather.HARSH.value, BatteryAge.NEW.value, EngineStart.DOES_NOT_START.value, 0.2],
    [Weather.HARSH.value, BatteryAge.OLD.value, EngineStart.STARTS.value, 0.4],
    [Weather.HARSH.value, BatteryAge.OLD.value, EngineStart.DOES_NOT_START.value, 0.6]
], [weather, battery_age])

electrical_system_cpt = ConditionalProbabilityTable([
    [Maintenance.WELL_MAINTAINED.value, ElectricalSystem.FUNCTIONAL.value, 0.9],
    [Maintenance.WELL_MAINTAINED.value, ElectricalSystem.FAULTY.value, 0.1],
    [Maintenance.POORLY_MAINTAINED.value, ElectricalSystem.FUNCTIONAL.value, 0.6],
    [Maintenance.POORLY_MAINTAINED.value, ElectricalSystem.FAULTY.value, 0.4]
], [car_maintenance])

engine_noise_cpt = ConditionalProbabilityTable([
    [Maintenance.WELL_MAINTAINED.value, EngineNoise.NORMAL.value, 0.85],
    [Maintenance.WELL_MAINTAINED.value, EngineNoise.NOISY.value, 0.15],
    [Maintenance.POORLY_MAINTAINED.value, EngineNoise.NORMAL.value, 0.6],
    [Maintenance.POORLY_MAINTAINED.value, EngineNoise.NOISY.value, 0.4]
], [car_maintenance])

# Create the states
s1 = State(weather, name="weather")
s2 = State(car_maintenance, name="car_maintenance")
s3 = State(battery_age, name="battery_age")
s4 = State(engine_start_cpt, name="engine_start")
s5 = State(electrical_system_cpt, name="electrical_system")
s6 = State(engine_noise_cpt, name="engine_noise")

# Initialize the Bayesian Network
network = BayesianNetwork("Car Engine Problem Diagnosis")

# Add states and edges
network.add_states(s1, s2, s3, s4, s5, s6)
network.add_edge(s1, s4)
network.add_edge(s2, s5)
network.add_edge(s2, s6)
network.add_edge(s3, s4)

# Bake the network to finalize it
network.bake()
