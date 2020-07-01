import matplotlib.pyplot as plt
import numpy as np
def gaussian(x,mu,sigmasq):
        return 1.0/np.sqrt(2*np.pi*sigmasq)*np.exp(((x-mu)**2)*(-1.0)/(2*sigmasq))
def genuine(x):
        return gaussian(x,15,15)
def imposter(x):
        return gaussian(x,20,15)
def main():
        ns = 3000
        plt.rcParams['lines.linewidth']=2
        s = np.random.normal(0,100,ns)

        x = np.arange(0,100,0.1)
        
        y_g = [genuine(x[i]) for i in range(len(x))]
        y_i = [imposter(x[i]) for i in range(len(x))]
        tpr=[]
        fpr=[]
        fnr=[]
        for n in np.arange(0,100,1):
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
                print("tp= {} fp={} tn={} fn={} n={}".format(tp,fp,tn,fn,n))
                fpr.append(fp*1.0/d2)
                fnr.append(fn*1.0/d1)






       


        fig,axs = plt.subplots(nrows=1,ncols=3)
        print("tpr={}\nfpr={}\nfnr={}".format(tpr,fpr,fnr))
        axs[0].plot(x,y_g,'b',label='Genuine')
        axs[0].plot(x,y_i,'r',label='Imposter')
        axs[0].title.set_text('Genuine and Imposter')
        axs[0].legend()

        axs[1].plot(fpr,tpr,'b',label='TPR vs FPR')
        axs[1].title.set_text('ROC plot')
        axs[1].legend()
        
        axs[2].plot(fpr,fnr,'r',label='FNR vs FPR')
        axs[2].title.set_text('DET plot')
        axs[2].legend()
        plt.show()




if __name__=="__main__":
	main()
