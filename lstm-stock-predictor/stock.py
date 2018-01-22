from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time


# Step 1: load data
X_train, y_train, X_test, y_test = lstm.load_data('close.csv', 50, True)

# Step 2: build model
model = Sequential()

model.add(LSTM(input_dim=1, output_dim=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(100, return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(output_dim=1))
model.add(Activation('linear'))

start = time.time()
model.compile(loss='mse', optimizer='rmsprop')
print('compilation time : %f\n' % (time.time() - start))

# Step 3: train the model
model.fit(X_train, y_train, batch_size=128, nb_epoch=1, validation_split=0.05)
#model.fit(X_train, y_train, batch_size=512, nb_epoch=1, validation_split=0.05)

# Step 4: plot the predictions
predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
lstm.plot_results_multiple(predictions, y_test, 50)

