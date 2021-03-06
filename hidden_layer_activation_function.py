'''
Majorly there are 3 most used activation functions:-
            1. Step Function (if inp < 0 then 0 else 1)
            2. Sigmoid Function (y = (1 /1 + e^(-x)))
            3. ReLU Function (if input < 0 then 0 else x)

Q- Why do we even need activation functions?
Ans- Let's say we are not using any activation function then we will be having by default linear activation function (y = x) 
which will be giving simply input without altering it, but this is not ideal for fitting those data points which are not 
speaded linearly. For that,  we have to use some non linear activation function so that we can alter the input values accordingly.
Ex- You can take an example by trying to fit linear line into sine function.

- If we will have more neuron in activation layers then it will be more effective and will be able to fit into data points much more easily than with less neurons activation layers
- In order to non-linear equation we need to have more hidden layers than usual.
'''

# ReLU (Rectified Linear Unit)

import numpy as np
np.random.seed(0)

inputs = [0 , 2 , -1 , 3.3 , -2.7 , 1.1 , 2.2 , -100]
outputs = []

for i in inputs:
    # if i > 0:
    #     outputs.append(i)
    # else:
    #     outputs.append(0)

    '''
    We can also use max function
    '''
    outputs.append(max(0 , i))
    
print(outputs)

inputs = []