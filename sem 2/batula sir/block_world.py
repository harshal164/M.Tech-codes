import numpy as np

BOARD_ROWS = 3
BOARD_COLS = 4
WIN_STATE = (0, 3)
LOSE_STATE = (1, 3)
START = (2, 0)
DETERMINISTIC = True

class State:
    def __init__(self,state=START):
        self.board=np.zeros([BOARD_ROWS,BOARD_COLS])
        self.board[1,1]=-1
        self.state=state
        self.isEnd=False
        self.determine=DETERMINISTIC



    def giveReward(self):
        if self.state==WIN_STATE:
            return 1
        elif self.state==LOSE_STATE:
            return -1
        else:
            return 0

    def giveReward(self):
        if self.state==WIN_STATE:
            return 1
        elif self.state==LOSE_STATE:
            return -1
        else:
            return 0
    
    def isEndFunc(self):
        if (self.state==WIN_STATE) or (self.state==LOSE_STATE):
            self.isEnd=True




    def nxtPosition(self,action):
        if self.determine:
            if action=="up":
                nxtState=(self.state[0]-1,self.state[1])
            elif action=="down":
                nxtState=(self.state[0]+1,self.state[1])
            elif action=="left":
                nxtState=(self.state[0],self.state[1]-1)
            else:

                nxtState=(self.state[0],self.state[1]+1)
            if( nxtState[0]>=0 and nxtState[0]<=2):
                if (nxtState[1]>=0 and nxtState[1]<=3):
                    if nxtState!=(1,1):
                        return nxtState
        return self.state


    
    def showBoard(self):
        self.board[self.state]=1
        for i in range(BOARD_ROWS):
            print('----------------------------')
            out="|"
            for j in range(BOARD_COLS):
                            
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')




class Agent:
    def __init__(self):
        self.states=[]
        self.actions=["up","down","left","right"]
        self.State=State()
        self.lr=0.2
        self.exp_rate=0.3

        self.state_values={}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.state_values[(i,j)]=0
    

    def chooseAction(self):
        mx_nxt_reward=0
        action=""
        
        if np.random.uniform(0,1)<=self.exp_rate:
            action=np.random.choice(self.actions)
        else:
            for a in self.actions:
                nxt_reward=self.state_values[self.State.nxtPosition(a)]
                if nxt_reward>=mx_nxt_reward:
                    action=a
                    mx_nxt_reward=nxt_reward
        return action
    
    def takeAction(self,action):
        position=self.State.nxtPosition(action)
        return State(state=position)
    
    def reset(self):
        self.states=[]
        self.State=State()



    def play(self,rounds=10):
        i=0
        while i<rounds:
            if self.State.isEnd:
                reward=self.State.giveReward()
                self.state_values[self.State.state]=reward
                print("game end reward",reward)
                for s in reversed(self.states):
                    reward=self.state_values[s]+self.lr*(reward-self.state_values[s])
                    self.state_values[s]=round(reward,3)
                    self.reset()
                    i+=1
            else:
                action=self.chooseAction()
                self.states.append(self.State.nxtPosition(action))
                print("current position {} action {} ".format(self.State.state,action))
                self.State=self.takeAction(action)
                self.State.isEndFunc()
                print("nxt state ",self.State.state)
                print("---------------")


    def showValues(self):
        for i in range(BOARD_ROWS):
            print("-----------------------")
            out="|"
            for j in range(BOARD_COLS):
                out+=str(self.state_values[(i,j)]).ljust(6)+"|"
            print(out)
        print("---------------------------------")




if __name__=="__main__":
    ag=Agent()
    ag.play(50)
    print(ag.showValues())