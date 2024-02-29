import pandas as pd
import numpy as np

from tests import X, y


class MyLineReg():

    def __init__(self, n_iter=100, learning_rate=0.1, weights=None):
        self.n_iter = n_iter
        self.learning_rate = learning_rate
        self.weight = weights

    def __repr__(self):
        return f"MyLineReg class:" \
               f"n_iter={self.n_iter}, " \
               f"learning_rate={self.learning_rate}, "

    def fit(self, X: pd.DataFrame, y: pd.Series, verbose=False) -> None:
        X = X.to_numpy()
        X = np.hstack((np.ones((X.shape[0], 1)), X))
        y = y.to_numpy()
        self.weight = np.full(X.shape[1], 1.0)

        for i in range(self.n_iter):

            y_predicted = X @ self.weight
            gradient = (2 / X.shape[0]) * (y_predicted - y) @ X  # градиент
            self.weight -= self.learning_rate * gradient  # веса
            mse = np.mean((y_predicted - y) ** 2)  # ошибка

            if verbose is not False and i % verbose == 0:
                print(f'{i} | loss: {mse}')

    def get_coef(self):
        return self.weight[1:]


model = MyLineReg(50, 0.1)
print(model)

model.fit(pd.DataFrame(X), pd.Series(y), 10)
print(model.get_coef())
