# we are having batches because of parallelization as it increases efficiency and speed of our program
# batches inputs are mainly preferrable in GPU due to it's high amount of core
# batch size of 32 is pretty common 

import numpy as np

# INPUTS
inputs = [[1 , 2 , 3 , 2.5],
          [2.0 , 5.0 , -1.0 , 2.0],
          [-1.5 , 2.7 , 3.3 , -0.8]]

# WEIGHTS
weights = [[0.2 , 0.8 , -0.5 , 1.0],
        [0.5 , -0.91 , 0.26 , -0.5],
        [-0.26 , -0.27 , 0.17 , 0.87]]

# BIASES
biases = [2, 3, 0.5] 

# OUTPUT
layer1_output = np.dot(inputs , np.array(weights).T) + biases

# Now this output from layer 1 will become input for layer 2

weights2 = [[0.1 , -0.14 , 0.5],
            [-0.5 , 0.12 , -0.33],
            [-0.44 , 0.73 , -0.13]]

biases2 = [-1 , 2 , -0.5]

layer2_output  = np.dot(layer1_output , np.array(weights2).T) + biases2

print(layer2_output)



