# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:09:25 2020

@author: roy
"""


def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0
 
# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.3,0.8,0.7]#[0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		#print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights
 
# Calculate weights
dataset = [[2,2,0],
	[-2,2,0],
	[1,-2,1],
	[-1,1,1]]
l_rate = 0.5
n_epoch = 100
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)

y=.72-.38x
#1-.5x-1.5y
#y=2/3-0.33x

#1.8+0.09x-1.3y=0
#y=1.38+0.07x
#
#1.8+0.09y-1.3x=0
#
##
##y=-20+14x
#-0.2-0.4x-.8y
#y=-.25-.5x

    x=-2;y=1
    1.3-0.7*x-1.8*y
    
    
    0.9294y+.7757x+.48=0
    y=-.83x-.51