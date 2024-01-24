from network import network
from enums import *
from dataclasses import dataclass, field
from itertools import product


@dataclass
class BNRun:
    evidence: dict[str, str]
    results: dict[str, float] = field(default_factory=dict)


@dataclass
class BNExperiment:
    evidence_nodes: list[str]
    node_of_interest: list[str]


def format_evidence(evidence: dict):
    """Reformat the evidence dict to pomegranate's format"""
    return [[evidence.get(node.name, None) for node in network.states]]


def conduct_experiment(exp: BNExperiment):
    possible_evidence_node_vals = [enum_values_from_string[ev] for ev in exp.evidence_nodes]
    possible_evidence_combinations = list(product(*possible_evidence_node_vals))
    for combination in possible_evidence_combinations:
        evidence = {exp.evidence_nodes[i]: combination[i] for i in range(len(exp.evidence_nodes))}
        run = BNRun(evidence)
        # todo: calculate values of nodes of interest


# Evidence
evidence = {
    "weather": Weather.HARSH.value,
    "car_maintenance": Maintenance.POORLY_MAINTAINED.value,
    "battery_age": BatteryAge.OLD.value,
    "electrical_system": ElectricalSystem.FAULTY.value
}

# Format the evidence
observations = [[evidence.get(node.name, None) for node in network.states]]

# Query the network
predictions = network.predict_proba(observations)

sample_predictions = predictions[0]

# Get specific node distribution (e.g., for 'engine_start')
engine_start_index = next(i for i, node in enumerate(network.states) if node.name == "engine_start")
engine_start_distribution = sample_predictions[engine_start_index]

# Print the distribution
print(engine_start_distribution)
