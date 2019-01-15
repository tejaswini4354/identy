import numpy as np
x_train=np.random.rand(9000,size = (1,2))
y_train=x_train[0]*(0.12)-x_train[1]*(0.45)


x_train=np.random.rand(9000,size = (1,2))
y_train=x_train[0]*(0.12)-x_train[1]*(0.45)

x_train =x_train[1000:]
y_train = y_train[1000:]
y_test=x_train[0:1000]
x_test=x_train[0:1000]


model = Sequential()
model.add(Dense(units=200, input_dim=1))
model.add(Activation('relu'))
model.add(Dense(units=45))
model.add(Activation('relu'))
model.add(Dense(units=1))

model.compile(loss='mean_squared_error',
              optimizer='rmsprop')

model.fit(x_train, y_train, epochs=40, batch_size=50, verbose=1)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=100)

classes = model.predict(x_test, batch_size=1)

test=x_test.reshape(-1)
plt.plot(test,classes,c='r')
plt.plot(test,y_test,c='b')
plt.show()