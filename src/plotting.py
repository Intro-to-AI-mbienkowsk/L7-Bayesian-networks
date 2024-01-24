import matplotlib.pyplot as plt
from src.experiments import BNExperiment


def generate_description(exp: BNExperiment):
    description = "Network parameters:\n"
    for k, v in exp.concrete_evidence.items():
        description += f"{k}: {v if v is not None else "randomized"}\n"
    return description


def plot_results(engine_start_probs, exp: BNExperiment):
    labels = list(engine_start_probs.keys())
    values = list(engine_start_probs.values())
    fig = plt.figure(figsize=(12, 6))
    fig.set_facecolor('#f8e5ad')
    plt.subplots_adjust(right=.67, left=.075)
    bars = plt.bar(labels, values, color='#76b5c5')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval / 2, round(yval, 2), va='center', ha='center', fontsize=12,
                 fontweight='bold')
    plt.xlabel('Engine Start States')
    plt.ylabel('Probabilities')
    plt.title('Engine Start Probability Distribution')
    plt.text(1.1, 0.5, generate_description(exp), transform=plt.gca().transAxes, va='center', fontsize=12)
    plt.show()
