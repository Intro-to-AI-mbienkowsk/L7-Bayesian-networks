from pomegranate import *
from probs import *

# root nodes
weather = DiscreteDistribution(weather_probs)
car_maintenance = DiscreteDistribution(maintenance_probs)
battery_age = DiscreteDistribution(battery_age_probs)

# non-root nodes
electrical_system = ConditionalProbabilityTable(
    electrical_system_cpt_entries, [car_maintenance])

engine_noise = ConditionalProbabilityTable(
    engine_noise_cpt_entries, [car_maintenance])

engine_start = ConditionalProbabilityTable(
    engine_start_cpt_entries, [weather, battery_age, electrical_system, engine_noise]
)

s1 = State(weather, name="weather")
s2 = State(car_maintenance, name="car_maintenance")
s3 = State(battery_age, name="battery_age")
s4 = State(engine_start, name="engine_start")
s5 = State(electrical_system, name="electrical_system")
s6 = State(engine_noise, name="engine_noise")

network = BayesianNetwork("Car Engine Problem Diagnosis")

network.add_states(s1, s2, s3, s4, s5, s6)
network.add_edge(s1, s4)
network.add_edge(s3, s4)
network.add_edge(s6, s4)
network.add_edge(s5, s4)
network.add_edge(s2, s5)
network.add_edge(s2, s6)

network.bake()
