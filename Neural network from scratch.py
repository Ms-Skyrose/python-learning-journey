import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

samples = 100
y = 3

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.outputs = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))
        probalities = exp_values / np.sum(exp_values, axis = 1, keepdims = True)
        self.output = probalities


class loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss
    

class Loss_CategoriticalCrossentropy(loss):
    def foward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if len(y_true.shape) ==1:
            correct_confidences = y_pred_clipped[range(samples), y_true]

        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis = 1)

        negative_log_likelihoods = np.log(correct_confidences)
        return negative_log_likelihoods



layer1 = Layer_Dense(4, 5)
activation1 = Activation_ReLU()

layer2 = Layer_Dense(5, 2)
activation2 = Activation_Softmax()


layer1.forward(X)
activation1.forward(layer1.outputs)

layer2.forward(activation1.output)
activation2.forward(layer2.outputs)

print(activation2.output[:5])

loss_function = Loss_CategoriticalCrossentropy()
#loss = loss_function.calculate(activation2.output, y)

#print("Loss:", loss)

#plt.scatter(X, y)
#plt.show()












