# now we are going to code a layer which has 3 neuron with 4 inputs
# so there will be 3 sets of weights and 3 unique biases for each neuron and each weight set will consists of 4 values

# INPUT
inputs = [1 , 2 , 3 , 2.5]

# WEIGHTS
weights = [[0.2 , 0.8 , -0.5 , 1.0],
        [0.5 , -0.91 , 0.26 , -0.5],
        [-0.26 , -0.27 , 0.17 , 0.87]]
# BIASES
biases = [2, 3, 0.5] 

# Now here we will have 3 different output for each neuron
neurons_output = []

for n_weights , n_biases in zip(weights , biases):
    output = 0
    for n_input , n_weight in zip(inputs , n_weights):
        output += n_input * n_weight
    output += n_biases

    neurons_output.append(output)

# We can also perform same stuff in one line using numpy
import numpy as np
outputs = np.dot(weights, inputs) + biases

# Let's print the output
print(outputs) # output by numpy method
print(neurons_output) # output by loop method