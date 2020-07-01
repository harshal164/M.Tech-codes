import matplotlib.pyplot as plt
import numpy as np
import math
def gaussian(x,mu,sigmasq):
        return 1.0/np.sqrt(2*np.pi*sigmasq)*np.exp(((x-mu)**2)*(-1.0)/(2*sigmasq))
def genuine(x):
        return gaussian(x,20,5)
def imposter(x):
        return gaussian(x,60,15)
def main():
        ns = 3000
        plt.rcParams['lines.linewidth']=2
        s = np.random.normal(50,6,ns)
        print(s)

        x = np.arange(0,100,0.1)
        
        y_g = [genuine(x[i]) for i in range(len(x))]
        y_i = [imposter(x[i]) for i in range(len(x))]
        tpr=[]
        fpr=[]
        fnr=[]
        for n in np.arange(1,100,1):
                tp = 0
                fn = 0
                fp = 0
                tn = 0
                for i in range(len(s)):
                        if s[i] > n:
                                if genuine(s[i]) < imposter(s[i]):
                                        tn = tn+1
                                else:
                                        fn = fn+1
                        else:
                                if genuine(s[i]) < imposter(s[i]):
                                        fp = fp+1
                                else:
                                        tp = tp+1
                d1=tp+fn+0.000001
                d2=fp+tn+0.000001
                tpr.append(tp*1.0/d1)
                # print("tp= {} fp={} tn={} fn={} n={}".format(tp,fp,tn,fn,n))
                fpr.append(fp*1.0/d2)
                fnr.append(fn*1.0/d1)


        tp=0.00001
        tn=0.00001
        fp=0.00001
        fn=0.00001
        thr=float(input("enter threshold value: "))
        for i in range(len(s)):
                if s[i] > thr:
                        if genuine(s[i]) < imposter(s[i]):
                                tn = tn+1
                        else:
                                fn = fn+1
                else:
                        if genuine(s[i]) < imposter(s[i]):
                                fp = fp+1
                        else:
                                tp = tp+1
        print(tp,tn,fp,fn)
        def recall(tp,fn):
                return tp/(tp+fn)
        def precision(tp,fp):
                return tp/(tp+fp)
        def mcc(tp,tn,fp,fn):
                return ((tp*tn-fp*fn) / np.sqrt((tp+fn)*(tp+fp)*(tn+fp)*(tn+fn)))
        def f1_score(tp,fp,tn):
                return (2*tp/(2*tp+fp+fn))
        
        print("for threshold= ",int(thr),"\n tp: ",int(tp)," fp: ",int(fp)," tn: ",int(tn)," fn: ",int(fn))
        print("recall:",recall(tp,fn))
        print("precision: ",precision(tp,fp))
        print("MCC: ",mcc(tp,tn,fp,fn))
        print("f1 score: ",f1_score(tp,fp,tn))
       

        # print(tpr)
        fig,axs = plt.subplots(nrows=2,ncols=3)
        




        axs[0][0].plot(x,y_g,'b',label='Genuine')
        axs[0][0].plot(x,y_i,'r',label='Imposter')
        axs[0][0].title.set_text('Genuine and Imposter')
        axs[0][0].legend()
        


        # axs[0][1].plot(fpr,tpr,'b',label='TPR vs FPR')
        # axs[0][1].title.set_text('ROC plot')
        # axs[0][1].legend()
        
        axs[0][2].plot(fpr,fnr,'r',label='FNR vs FPR')
        axs[0][2].title.set_text('DET plot')
        axs[0][2].legend()


        fpr.insert(0,0) 
        tpr.insert(0,0) 
        fpr.append(1)
        tpr.append(1)

        axs[0][1].plot(fpr,tpr,'r',label='FNR vs FPR')
        axs[0][1].title.set_text('ROC plot')
        axs[0][1].legend()
        

        axs[1][1].plot(s,'r,')
        axs[1][1].title.set_text("value distribution for ROC curve")

        # temp=[i for i in range(ns)]
        # s.sort()
        # axs[1][1].plot(temp,s,'r',label="samplw")
        plt.show()




if __name__=="__main__":
	main()
