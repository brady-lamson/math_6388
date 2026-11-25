import torch.nn as nn
from sklearn.metrics import precision_score, recall_score, f1_score, log_loss, confusion_matrix
from torchmetrics.classification import BinaryCalibrationError
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Taken for course notebook 3 ---
class BinaryMLP(nn.Module):
    def __init__(self, input_dim=10, width=32):
        super().__init__()
        self.layers = nn.Sequential(nn.Linear(input_dim, width), nn.ReLU(),
                                    nn.Linear(width, width), nn.ReLU(),
                                    nn.Linear(width, 1))
    def forward(self, x):
        return self.layers(x).squeeze(-1) # remove the last dimension when its size is 1


# Taken and modified from course notebook 3 ---
def three_way_indices(y, stratify_column=None, train_size=0.5, seed: int=100):
    idx = np.arange(len(y))
    test_size = 1 - train_size
    if stratify_column is None:
        stratify_column = y
    train, rest = train_test_split(idx, test_size=test_size, stratify=stratify_column, random_state=seed)
    cal, test = train_test_split(rest, test_size=.5, stratify=stratify_column[rest], random_state=seed+2)
    groups = {"train": train, "cal": cal, "test": test}
    assert len(np.unique(np.concatenate(list(groups.values())))) == len(y)
    return groups


def evaluate_binary_classifier(test_probabilities, y_test, prob_cutoff=0.5):
    test_predictions = (test_probabilities >= prob_cutoff).float()
    precision = precision_score(y_test, test_predictions)
    recall = recall_score(y_test, test_predictions)
    f1 = f1_score(y_test, test_predictions)
    nll = log_loss(y_test, y_proba=test_probabilities)
    conf_mat = confusion_matrix(y_test, test_predictions)
    ece = BinaryCalibrationError(n_bins=15)
    if test_probabilities.ndim == 1:
        y_test = y_test.squeeze()
    ece_value = ece(test_probabilities, y_test)
    accuracy = (test_predictions == y_test).float().mean()

    print("CUTOFF:", prob_cutoff)
    print(f"ACCURACY: {accuracy.item():.2%}")
    print(f"PRECISION: {precision:.2%}")
    print(f"RECALL: {recall:.2%}")
    print(f"F1-SCORE: {f1:.2%}")
    print(f"CONFUSION MATRIX:\n{conf_mat}")
    print(f"NLL: {round(nll, 5)}")
    print(f"ECE: {ece_value.item():.5f}")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1-score": f1,
        "confusion_matrix": conf_mat,
        "nll": nll,
        "ece_value": ece_value,
    }


def plot_reliability(probs, labels, n_bins=10, ax=None,
                    title="Reliability diagram"):
    """
    probs:  NumPy array with shape [N], predicted probabilities for class 1.
    labels: NumPy array with shape [N], containing binary labels (0 or 1).
    """
    probs = np.asarray(probs).reshape(-1)
    labels = np.asarray(labels).reshape(-1)

    # Divide [0, 1] into equally spaced probability bins.
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    bin_ids = np.digitize(probs, edges[1:-1])

    mean_probability = []
    observed_frequency = []
    counts = []
    ece = 0.0

    for m in range(n_bins):
        in_bin = (bin_ids == m)
        count = in_bin.sum()

        if count == 0:
            continue

        bin_probability = probs[in_bin].mean()
        bin_frequency = labels[in_bin].mean()

        mean_probability.append(bin_probability)
        observed_frequency.append(bin_frequency)
        counts.append(count)

        # Weight the calibration gap by the fraction of observations.
        ece += (count / len(labels)) * abs(
            bin_frequency - bin_probability
        )

    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))

    ax.plot([0, 1], [0, 1], "k--", label="Perfect calibration")
    ax.plot(mean_probability, observed_frequency, "o-", label="Model")

    # Annotate each point with the number of observations in its bin.
    for x, y, count in zip(mean_probability, observed_frequency, counts):
        ax.annotate(f"n={count}", (x, y),
                    xytext=(5, 5), textcoords="offset points", fontsize=8)

    ax.set(
        xlabel="Mean predicted probability (class 1)",
        ylabel="Observed positive frequency",
        title=f"{title}\nECE = {ece:.3f}",
        xlim=(0, 1),
        ylim=(0, 1),
    )
    ax.set_aspect("equal")
    ax.grid(alpha=0.2)
    ax.legend()

    return ece
