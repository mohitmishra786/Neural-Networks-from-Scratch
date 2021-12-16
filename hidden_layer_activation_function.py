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
'''