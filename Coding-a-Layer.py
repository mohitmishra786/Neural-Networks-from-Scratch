# now we are going to code a layer which has 3 neuron with 4 inputs
# so there will be 3 sets of weights and 3 unique biases for each neuron and each weight set will consists of 4 values

# INPUT
inputs = [1 , 2 , 3 , 2.5]

# WEIGHTS
weights1 = [0.2 , 0.8 , -0.5 , 1.0]
weights2 = [0.5 , -0.91 , 0.26 , -0.5]
weights3 = [-0.26 , -0.27 , 0.17 , 0.87]

# BIASES
bias1 = 2
bias2 = 3
bias3 = 0.5

# Now here we will have 3 different output for each neuron
output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
         inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights1[3] + bias2,
         inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights1[3] + bias3]

# Let's print the output
print(output)