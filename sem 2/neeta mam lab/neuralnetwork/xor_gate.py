import numpy as np

class Weights:
    def __init__(self, w_size):
        self.w_mat = 0.2*np.random.randn(w_size[0],w_size[1]) + (0.5*np.ones(w_size))
    def __str__(self):
        return str(self.w_mat)

def sigmoid(x):
    return 1./(1.+np.exp(-1*x))

def sig_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

class neural_network:
    def __init__(self, layer_conf):
        self.layer_conf = layer_conf
        weights = []
        biases = []

        for i in range(len(layer_conf) - 1):
            weights.append(Weights((layer_conf[i],layer_conf[i+1])))
            #print(Weights((layer_conf[i],layer_conf[i+1])))
            
            biases.append(Weights((layer_conf[i+1],1)))
        
        self.weights = weights
        self.biases = biases

    def classify(self, X):
        

        a = X
        a_list = [X]
        z_list = []

        for i in range(len(self.weights)):
            z = np.matmul(self.weights[i].w_mat.T,a)+self.biases[i].w_mat
            a = sigmoid(z)
            for i in range(len(a)):
                if a[i][0] < 0.5:
                    a[i][0] = 0
                else:
                    a[i][0] = 1
            a_list.append(a)
            z_list.append(z)

        return a[0][0]

    def train(self, train_set, alpha):
        X,Y = train_set
        epochs = 0
        while True:
            
            print("epoch:",epochs)
            print("after ",epochs," epoch weights are:")
            for w in self.weights:
                print(w)
            print("after ",epochs," epoch biases are:")
            for b in self.biases:
                print(b)
            
            for j in range(len(X)):
                x = np.asarray(X[j])


                A_list, Z_list = self.forwardpass(x)
                delta_w, delta_b = self.backpropagation(A_list, Z_list, Y[j])

                for i in range(len(self.weights)):
                    self.weights[i].w_mat = self.weights[i].w_mat - alpha * delta_w[i]

                for i in range(len(self.biases)):
                    self.biases[i].w_mat = self.biases[i].w_mat - alpha * delta_b[i]

            epochs = epochs + 1
            if epochs > 12000:
                break

    def backpropagation(self, a_list, z_list, Y):
        delta_w = [np.zeros(w.w_mat.shape) for w in self.weights]
        delta_b = [np.zeros(b.w_mat.shape) for b in self.biases]

        delta = np.multiply(a_list[-1] - Y,sig_prime(z_list[-1]))

        delta_w[-1] = np.matmul(a_list[-2],delta.T)
        delta_b[-1] = delta

        for l in range(2,len(self.layer_conf)):
            z = z_list[-l]
            delta = np.multiply(np.matmul(self.weights[-l+1].w_mat,delta), sig_prime(z))
            delta_b[-l] = delta
            delta_w[-l] = np.matmul(a_list[-l-1],delta.T)
        return delta_w, delta_b

    def forwardpass(self, X):
        A = X
        a_list = [X]
        z_list = []

        for i in range(len(self.weights)):
            Z = np.matmul(self.weights[i].w_mat.T,A)+self.biases[i].w_mat
            A = sigmoid(Z)
            for i in range(len(A)):
                if A[i][0] < 0.5:
                    A[i][0] = 0
                else:
                    A[i][0] = 1
            a_list.append(A)
            z_list.append(Z)

        return a_list, z_list


def main():

    nn = neural_network([2,2,1])
    trainingset = [[[[0],[0]],[[0],[1]],[[1],[0]],[[1],[1]]],[0,1,1,0]]
    nn.train(trainingset,0.1)
   


    n = 0
    while n < 2:
        print(" 1. XOR Gate 2. Exit")
        n = int(input())
        if n == 1:
            data = []
            data.append(int(input("1st value: ")))
            data.append(int(input("2nd value: ")))
            data = np.asarray(data)
            data = np.reshape(data,(2,1))
            print(int(nn.classify(data)))

if __name__=="__main__":
    main()
