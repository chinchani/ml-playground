from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.utils import plot_model
#from sklearn.cross_validation import StratifiedKFold
from sklearn.model_selection import StratifiedKFold

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# create model with 3 layers
# input layer
model = Sequential()
# add fully connected (2->4, uniform rng weigts, relu activation
model.add(Dense(4, input_dim=2, init='uniform', activation='relu'))
# add fully connected hidden (4->4, uniform rng weigts, relu activation
model.add(Dense(4, init='uniform', activation='relu'))
# output (4->1 neurons, sigmoid activation
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Plot the model
plot_model(model, to_file='model.png')

""" load data and plot """
#f = open("/mnt/zram/ratings.csv")
f = open("r.csv")
f.readline()        # skip the header
data = np.loadtxt(f, delimiter=',')
X = data[:,0:2]
Y = data[:,2]
# Fit the model
h = model.fit(X, Y, epochs=150, batch_size=10,  verbose=2, validation_split=0.2)
print(h.history)
# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
