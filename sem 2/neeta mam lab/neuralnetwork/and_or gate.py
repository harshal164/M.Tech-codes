import numpy as np

class neural_network:
    def __init__(self, w, a):
        self.w = np.array(w)
        self.a = a
        self.is_trained = False
        self.threshold = 0
    def train(self, train_set, thr):
        self.thr = thr
        x,y = train_set
        x = np.array(x)
        y = np.array(y)
        while True:
            flag = True
            for i in range(len(y)):
                w_prev = self.w
                d = np.matmul(np.transpose(self.w),x[i])
                if d <= thr:
                    d = 0
                else:
                    d = 1
                tmp = -1*self.a*(d-y[i])*np.array(x[i])
                self.w = np.add(self.w,tmp)
                if list(w_prev) != list(self.w):
                    flag = False
            if flag:
                break
        self.is_trained = True
    def classify(self,tst_data):
        if self.is_trained:
            d = np.matmul(np.transpose(self.w),tst_data)
            if d <= self.thr:
                d = 0
            else:
                d = 1
            return d
        else:
            print("Train the model")
            return -1

def main():
    or_nn = neural_network([0.2,0.3],0.1)
    and_nn = neural_network([0.2,0.3],0.1)
    
    or_train_set = [[[1,1],[0,1],[1,0],[0,0]],[1,1,1,0]]
    and_train_set = [[[1,1],[0,1],[1,0],[0,0]],[1,0,0,0]]

    or_nn.train(or_train_set,0.6)
    and_nn.train(and_train_set,0.6)

    c = 0
    while c < 3:
        print("1.OR gate2) AND gate 3) Exit\n")
        c = float(input())
        if c >= 3:
            print("bye bye")
            exit(0)
        tst_data = []
        tst_data.append(float(input("1st input:")))
        tst_data.append(float(input("2nd input")))
        
        if c == 1:
            print(or_nn.classify(tst_data))
        else:
            print(and_nn.classify(tst_data))

if __name__ == "__main__":
    main()
