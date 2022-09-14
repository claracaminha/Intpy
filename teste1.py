from intpy.intpy import initialize_intpy, deterministic
import time
import sys


@deterministic
def get_empirical_CVaR(rewards, alpha = 0.9):
    a = sorted((rewards).copy(), reverse= True)
    temp=[]
    for i in range(1,len(a)-5):
        if float((len(a)) + 1) / len(a) >= 1-alpha:
            temp.append((int(a[i])))
        else:
            temp.append((int(a[i])))

    return float(sum(temp) / len(temp))    
   
  


@initialize_intpy(__file__)
def main(rewards):
    print(get_empirical_CVaR(rewards, 0.9))
  

if __name__ == "__main__":
    n = (sys.argv[1:])
    n.pop()
    n.pop()
    print(n)
    start = time.perf_counter()
    main(n)
    print(time.perf_counter()-start)
