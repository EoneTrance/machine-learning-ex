import numpy as np

x_data = np.array([ [2, 4], [4, 11], [6, 6], [8, 5], [10, 7], [12, 16], [14, 8], [16, 3], [18, 7] ])
t_data = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1]).reshape(9, 1)

W = np.random.rand(2, 1)
b = np.random.rand(1)

print("W: ", W, " W.shape: ", W.shape)
print("b: ", b, " b.shape: ", b.shape)


def sigmoid(x):
    return 1 / (1+np.exp(-x))


def loss_func(x, t):
    delta = 1e-7 # log 무한대 발산 방지

    z = np.dot(x,W) + b
    y = sigmoid(z)

    # cross-entropy
    return -np.sum(t*np.log(y+delta) + (1-t)*np.log((1-y)+delta))


def numerical_derivative(f, x):
    delta_x = 1e-4
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]

        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x) # f(x+delta_x)

        x[idx] = tmp_val - delta_x
        fx2 = f(x) # f(x-delta_x)

        grad[idx] = (fx1 - fx2) / (2*delta_x)

        x[idx] = tmp_val

        it.iternext()

    return grad


def error_val(x, t):
    delta = 1e-7 # log 무한대 발산 방지

    z = np.dot(x,W) + b
    y = sigmoid(z)

    # cross-entropy
    return -np.sum(t*np.log(y+delta) + (1-t)*np.log((1-y)+delta))


def predict(x):
    z = np.dot(x,W) + b
    y = sigmoid(z)

    if y > 0.5:
        result = 1 # True
    else:
        result = 0 # False

    return y, result


learning_rate = 1e-2 # 발산하는 경우, 1e-3 ~ 1e-6 등으로 바꾸어서 실행

f = lambda x : loss_func(x_data, t_data) # f(x) = loss_func(x_data, t_data)

print("Initial error value: ", error_val(x_data, t_data))
print("Initial W: ", W, " b: ", b)

for step in range(80001):
    W -= learning_rate * numerical_derivative(f, W)
    b -= learning_rate * numerical_derivative(f, b)

    if step % 400 == 0:
        print("step: ", step, "error value: ", error_val(x_data, t_data), "W: ", W, "b: ", b)


real_val, logical_val = predict([3, 17])
print(real_val, logical_val)

real_val, logical_val = predict([5, 8])
print(real_val, logical_val)

real_val, logical_val = predict([7, 21])
print(real_val, logical_val)

real_val, logical_val = predict([12, 0])
print(real_val, logical_val)
