# we are having batches because of parallelization as it increases efficiency and speed of our program
# batches inputs are mainly preferrable in GPU due to it's high amount of core
# batch size of 32 is pretty common 

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

# for setting default datatype, as numpy messes it up sometime
nnfs.init() 

# INPUTS
X = [[1 , 2 , 3 , 2.5],
     [2.0 , 5.0 , -1.0 , 2.0],
     [-1.5 , 2.7 , 3.3 , -0.8]]

'''
1. The way we tend to initialise weight are via randomly generated number between -1 to 1
2. Smaller the range of weight better it will be for us (moer tider more better)
3. It's quite intuitive that we will use smaller value of weights as if we will not then 
   as soon we will get deeper and deeper into layers then the values of neurons will start 
   exploding and we will have a memory shortage or our code will be highly memory intensive
4. So according to point 3, it's always better to normalize and scale the dataset before 
   performing operation on it.
'''

# making datasets
X , y = spiral_data(100 , 3) # 100 features set for 3 classes

# Lets make object of layers
class Layer_Dense:
    
    def __init__(self , n_inputs , n_neurons):
        '''
        np.zeros() function has the first paramter as a shape so we need to pass our shape as a tuple input
        np.random.randn() has all the parameter as shape
        '''
        self.weights = 0.1 * np.random.randn(n_inputs , n_neurons)
        self.biases = np.zeros((1 , n_neurons))

    def forward(self , inputs):
        self.output = np.dot(inputs , self.weights) + self.biases

class Activation_ReLU:
    def forward(self , inputs):
        self.output = np.maximum(0 , inputs)
        
layer1 = Layer_Dense(2 , 5)
layer2 = Layer_Dense(5, 2)
activation_1 = Activation_ReLU()
layer1.forward(X)
activation_1.forward(layer1.output)
layer2.forward(activation_1.output)
print(layer2.output)
