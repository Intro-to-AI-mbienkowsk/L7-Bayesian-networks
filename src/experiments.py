from src.network import network
from src.enums import *
from dataclasses import dataclass, field
from itertools import product


@dataclass
class BNRun:
    """Single run of the bayesian network - contains the evidence and a dictionary with the results for each node"""
    evidence: dict[str, str]
    results: dict[str, float] = field(default_factory=dict)


@dataclass
class BNExperiment:
    """Represents a bayesian network experiment given the evidence (nodes with a single, set value),
    list of nodes to permutate the values of and also pass as evidence to the network (to check how their values
    affect the nodes of interest) and nodes of interest, the probabilities of which should be returned when running
     the experiment"""
    concrete_evidence: dict
    nodes_to_permutate: list[str]
    nodes_of_interest: list[str]


def format_evidence(evidence: dict) -> list[list[dict]]:
    """Reformat the evidence dict to pomegranate's format"""
    return [[evidence.get(node.name, None) for node in network.states]]


def create_runs(exp: BNExperiment) -> list[BNRun]:
    """Create all the runs for the given experiments before running them"""
    possible_evidence_node_vals = [enum_values_from_string[ev] for ev in exp.nodes_to_permutate]
    possible_evidence_combinations = list(product(*possible_evidence_node_vals))
    runs = list()

    for combination in possible_evidence_combinations:
        # single run with the network's evidence being constructed from conc_evidence and a permutation of nodes_to_iter
        permutated_evidence = {
            exp.nodes_to_permutate[i]: combination[i]
            for i in range(len(exp.nodes_to_permutate))
        }
        final_evidence = {**exp.concrete_evidence, **permutated_evidence}
        runs.append(BNRun(final_evidence))
    return runs


def extract_relevant_nodes(exp: BNExperiment, network_output: list):
    """Extracts from the network output a dictionary with keys being the node names
    and values being their probability distributions only for the nodes relevant for
    the experiment - named in the conc_evidence, nodes_to_permutate or nodes_of_interest"""
    result = {**exp.concrete_evidence}
    for node_name in exp.nodes_to_permutate + exp.nodes_of_interest:
        node_idx = next(i for i, node in enumerate(network.states) if node.name == node_name)
        # extract either a string - the state if the node is proof or the probs from a distribution object
        result[node_name] = network_output[0][node_idx] \
            if node_name in exp.nodes_to_permutate + list(exp.concrete_evidence.keys()) else network_output[0][node_idx].parameters[0]
    return result


def conduct_experiment(exp: BNExperiment) -> list[BNRun]:
    """"Conduct an entire experiment, returning the list of runs with their results filled out"""
    runs = create_runs(exp)
    for run in runs:
        formatted_evidence = format_evidence(run.evidence)
        network_output = network.predict_proba(formatted_evidence)
        run.results = extract_relevant_nodes(exp, network_output)
    return runs


evidence_nodes = ["weather", "engine_noise"]
nodes_of_interest = ["electrical_system"]
conduct_experiment(BNExperiment({"battery_age": "Old"}, evidence_nodes, nodes_of_interest))
