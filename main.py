import numpy as np
from network import NeuralNetwork

# XOR Problem data
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_output = np.array([[0], [1], [1], [0]])

# Initialize Neural Network
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Train
print("Training...")
nn.train(inputs, expected_output, epochs=10000)

# Verify
print("\nPredictions after training:")
for i in range(len(inputs)):
    prediction = nn.forward(inputs[i:i+1])
    print(f"Input: {inputs[i]} - Prediction: {prediction[0][0]:.4f} - Expected: {expected_output[i][0]}")
