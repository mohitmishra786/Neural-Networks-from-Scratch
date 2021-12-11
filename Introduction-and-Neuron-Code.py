# Every neuron has a unique connection to the previous neuron.
inputs = [3.1 , 2.5 , 5.4]

# Every input is going to have a unique weight 
weights = [4.5 , 7.6 , 2.4]

# Every neuron is going to have a unique bias
bias = 3

# Now let's check the output from the neuron
output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias

# Now let's print the output
print(output)

