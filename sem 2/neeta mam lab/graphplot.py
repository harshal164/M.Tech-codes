import random
import matplotlib.pyplot as plt
import numpy as np
def main():
        ns = 300
        plt.rcParams['lines.linewidth']=2
        s = [random.uniform(0,1) for _ in range(ns)]
        g = lambda x : 2 + 4 * x * x
        im = lambda x : 4 - 4 * x * x
        p_s_genuine=[g(s[i]) for i in range(len(s))]
        p_s_imposter=[im(s[i]) for i in range(len(s))]
        #print(len(s))
        #print(len(p_s_genuine))
        #plt.plot(s,p_s_genuine,'ro')
        #plt.plot(s,p_s_imposter,'bo')
        tpr=[]
        fpr=[]
        fnr=[]
        for n in np.arange(0,1,0.05):
                tp = 0
                fn = 0
                fp = 0
                tn = 0
                for i in range(len(s)):
                        if s[i] < n:
                                #print("{} is imposter for threshold {}".format(s[i],n))
                                #print("P(s|genuine)={} and P(s|imposter)={}".format(p_s_genuine[i],p_s_imposter[i]))
                                if p_s_genuine[i] < p_s_imposter[i]:
                                        tn = tn+1
                                else:
                                        fn = fn+1
                        else:
                                #print("{} is genuine for threshold {}".format(s[i],n))
                                #print("P(s|genuine)={} and P(s|imposter)={}".format(p_s_genuine[i],p_s_imposter[i]))
                                if p_s_genuine[i] < p_s_imposter[i]:
                                        fp = fp+1
                                else:
                                        tp = tp+1
                        #print('')
                d1=tp+fn
                d2=fp+tn
                tpr.append(tp*1.0/d1)
                print("tp= {} fp={} tn={} fn={} n={}".format(tp,fp,tn,fn,n))
                fpr.append(fp*1.0/d2)
                fnr.append(fn*1.0/d1)
        print("{} {}".format(tpr, fpr))
        idx = sorted(range(len(s)), key = lambda k:s[k])
        s_ = []
        s_g = []
        s_i = []
        for i in range(len(s)):
            s_.append(s[idx[i]])
            s_g.append(p_s_genuine[idx[i]])
            s_i.append(p_s_imposter[idx[i]])
        
        fig,axs = plt.subplots(nrows=1,ncols=3)
        
        axs[0].plot(s_,s_g,'C0',label='Genuine')
        axs[0].plot(s_,s_i,'C1',label='Imposter')
        #axs[0].xlabel='score'
        #axs[0].ylabel='pdf'
        axs[0].title.set_text('Genuine and Imposter pdf')
        axs[0].legend()

        axs[1].plot(fpr,tpr,'C0',label='TPRv.FPR')
        axs[1].title.set_text('ROC Plot')
        axs[1].legend()
        #axs[1].xlabel = 'FPR'
        #axs[1].ylabel = 'TPR'
        
        axs[2].plot(fpr,fnr,'C1',label='FNRv.FPR')
        axs[2].title.set_text('DET Plot')
        axs[2].legend()
        #axs[2].xlabel = 'FNR'
        #axs[2].ylabel = 'FPR'
        plt.show()
if __name__=="__main__":
	main()
