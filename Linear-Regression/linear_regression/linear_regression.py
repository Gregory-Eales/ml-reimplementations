import numpy as np
from matplotlib import pyplot as plt

class LinearRegressor(object):

    def __init__(self, input_size):
        self.w = np.zeros([input_size, 1])
        self.b = np.zeros([1, 1])
        self.historical_error = []

    def mean_squared_error(self, prediction, y):
        return 0.5*np.sum((prediction - y))**2 / y.shape[0]

    def mse_prime(self, prediction, y):
        return np.sum(prediction-y) / y.shape[0]

    def loss(self, x, prediction, y):
        loss = self.mse_prime(prediction, y)
        delta_w = loss*np.sum(x, axis=0)
        delta_b = loss
        return delta_w, delta_b

    def predict(self, x):
        return np.dot(x, self.w) + self.b

    def train(self, x, y, iter, alpha):

        for i in range(iter):
            prediction = self.predict(x)
            error = self.mean_squared_error(prediction, y)
            self.historical_error.append(error)
            delta_w, delta_b = self.loss(x, prediction, y)
            self.w = self.w - alpha*delta_w
            self.b = self.b - alpha*delta_b

def main():
    x = np.random.random([10, 2])
    y = np.random.random([10, 1])
    lr = LinearRegressor(2)
    print(lr.w)
    lr.train(x, y, iter=5000, alpha=0.0001)
    plt.plot(lr.historical_error)
    plt.show()


if __name__ == "__main__":
    main()