import numpy as np


def predict_probabilities(X, w, b):
    """
    Compute the probabilities for each sample/class.

    Parameters:
    - X: Input data, np.array of shape (N, D), where N is the number of samples and D is the number of features.
    - w: Weight matrix, np.array of shape (D, C), where C is the number of classes.
    - b: Bias vector, np.array of shape (C,).

    Returns:
    - Probabilities: np.array of shape (N, C), containing the probabilities for each sample/class.
    """
    z = np.dot(X, w) + b
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # for numerical stability
    probabilities = exp_z / np.sum(exp_z, axis=1, keepdims=True)
    return probabilities


# Example usage:
N = 3  # Number of samples
D = 4  # Number of features
C = 2  # Number of classes

# Example input data, weights, and bias
X_example = np.random.rand(N, D)
w_example = np.random.rand(D, C)
b_example = np.random.rand(C, )

# Get the probabilities
probabilities_example = predict_probabilities(X_example, w_example, b_example)

print("Input data:")
print(X_example)
print("\nWeights:")
print(w_example)
print("\nBias:")
print(b_example)
print("\nProbabilities:")
print(probabilities_example)
