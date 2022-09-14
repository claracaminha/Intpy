from intpy.intpy import initialize_intpy, deterministic
import time
import sys


@deterministic
def get_empirical_CVaR(rewards, alpha = 0.9):
    a = sorted((rewards).copy(), reverse= True)
    temp=[]
    for i in range(1,len(a)-10):
        if (i + 1 / len(a)) >= 1-alpha:
            temp.append((int(a[i])))
      
    return float(sum(temp) / len(a))    
   
  


@initialize_intpy(__file__)
def main(rewards):
    print(get_empirical_CVaR(rewards, 0.9))
  

if __name__ == "__main__":
    n = (sys.argv[2:])
    n.pop()
    n.pop()
    for i in range(len(n)):
      n[i]=n[i][:-1]
    print(n)
    start = time.perf_counter()
    main(n)
    print(time.perf_counter()-start)
