import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_input_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_hidden_output = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        # Forward pass
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_hidden_output
        self.predicted_output = self.sigmoid(self.output_layer_input)
        return self.predicted_output

    def backward(self, inputs, expected_output, output):
        # Backpropagation
        error = expected_output - output
        d_predicted_output = error * self.sigmoid_derivative(output)
        
        error_hidden_layer = d_predicted_output.dot(self.weights_hidden_output.T)
        d_hidden_layer = error_hidden_layer * self.sigmoid_derivative(self.hidden_layer_output)

        # Update weights and biases
        self.weights_hidden_output += self.hidden_layer_output.T.dot(d_predicted_output)
        self.bias_hidden_output += np.sum(d_predicted_output, axis=0, keepdims=True)
        self.weights_input_hidden += inputs.T.dot(d_hidden_layer)
        self.bias_input_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True)

    def train(self, inputs, expected_output, epochs):
        for epoch in range(epochs):
            output = self.forward(inputs)
            self.backward(inputs, expected_output, output)
