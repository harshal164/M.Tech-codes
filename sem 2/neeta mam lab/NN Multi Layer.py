# Without base signal
import numpy as np
import matplotlib.pyplot as plt

# Using Logistic model
def sigmoid(x):
    return 1/(1+np.exp(-x))

# as  derivation = a*(1-a) Mathematical proven
def derivation(x):
    return sigmoid(x)*(1-sigmoid(x))

def forward_propagation(x, w, predict=False):
    a, z = [], []
    for i in range(number_of_hl+1):
        zz = x if i == 0 else z[i-1]
        a.append(np.matmul(zz, w[i]))
        z.append(sigmoid(a[i]))
    # bias = np.ones((len(z1), 1))
    # Adding bias
    # z1 = np.concatenate((bias, z1), axis=1)
    # a.append(np.matmul(z[0], w[1]))
    # z.append(sigmoid(a[1]))
    if predict:
        return z[number_of_hl]
    return a, z

def backward_propagation(a, x, z, y):
    d, D = [0]*(number_of_hl+1), [0]*(number_of_hl+1)
    for i in range(number_of_hl,-1,-1):
        d[i] = z[i] - y if i == number_of_hl else (d[i+1].dot(w[i+1].T))*derivation(a[i])
        D[i] = np.matmul(x.T, d[i]) if i == 0 else np.matmul(z[i-1].T, d[i])
    # like e3 = (theta3)T e4 * derivation(a3)
    return d, D

if __name__ == "__main__":

    m = "Enter the number of hidden layer you want : "
    while(True):
        number_of_hl = int(input(m))
        if 0 < number_of_hl < 10:
            break
        m = "Wrong input input should be between 1 to 9 : "
    # Input[Bias, X1, X2]
    x = np.array([[1, 1, 0],
                 [1, 0, 1],
                 [1, 0, 0],
                 [1, 1, 1]])

    y = np.array([[1], [1], [0], [0]])

    # Initial Weight
    w = []
    for i in range(number_of_hl+1):
        if i == 0:
            w.append(np.random.randn(3, 5))
        if 0 < i < number_of_hl:
            w.append(np.random.randn(5, 5))
        if i == number_of_hl:
            w.append(np.random.randn(5, 1))

    # Learning rate
    lr = 0.09
    costs = []
    m = len(x)
    epochs = 15000

    for i in range(epochs):
        a, z = forward_propagation(x, w)
        d, D = backward_propagation(a, x, z, y)

        # weight = weight - learning rate * 1/m * derivation(j(cost))
        # derivation(j(cost)) = error [error term = D]
        for j in range(len(w)):
            w[j] = w[j] - lr*(1/m)*D[j]

        c = np.mean(np.abs(d[number_of_hl]))
        costs.append(c)

        if i % 1000 == 0:
            print(f"Iteration: {i}. Error: {c}")
    print("\n\nTraining complete\n\n")
    print(w)
    # Testing Model
    z3 = forward_propagation(x, w, True)
    # print(f"Percentages = {z3}")
    z3 = np.round(z3)
    print("Prediction = ")
    print(*z3)

    plt.plot(costs)
    plt.ylabel("Error")
    plt.xlabel("Epochs")
    plt.title("Error VS Epochs")
    plt.show()
