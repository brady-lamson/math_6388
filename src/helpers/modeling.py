import torch.nn as nn
import torch
from sklearn.metrics import precision_score, recall_score, f1_score, log_loss, confusion_matrix
from torchmetrics.classification import BinaryCalibrationError
import numpy as np
from sklearn.model_selection import train_test_split

# Taken for course notebook 3 ---
class BinaryMLP(nn.Module):
    def __init__(self, input_dim=10, width=32):
        super().__init__()
        self.layers = nn.Sequential(nn.Linear(input_dim, width), nn.ReLU(),
                                    nn.Linear(width, width), nn.ReLU(),
                                    nn.Linear(width, 1))
    def forward(self, x):
        return self.layers(x).squeeze(-1) # remove the last dimension when its size is 1


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

def evaluate_binary_classifier(model, x_test, y_test, prob_cutoff=0.5):
    test_logits = model(x_test)
    test_probabilities = torch.sigmoid(test_logits)
    test_predictions = (test_probabilities >= prob_cutoff).float()

    precision = precision_score(y_test, test_predictions)
    recall = recall_score(y_test, test_predictions)
    f1 = f1_score(y_test, test_predictions)
    nll = log_loss(y_test, test_predictions)
    conf_mat = confusion_matrix(y_test, test_predictions)
    ece = BinaryCalibrationError(n_bins=15)
    if test_probabilities.ndim == 1:
        y_test = y_test.squeeze()
    ece_value = ece(test_probabilities, y_test)
    accuracy = (test_predictions == y_test).float().mean()

    print(f"\nACCURACY: {accuracy.item():.2%}")
    print(f"PRECISION: {precision:.2%}")
    print(f"RECALL: {recall:.2%}")
    print(f"F1-SCORE: {f1:.2%}")
    print(f"CONFUSION MATRIX:\n{conf_mat}")
    print(f"NLL: {round(nll, 5)}")
    print(f"BCE: {ece_value.item():.5f}")

    return None