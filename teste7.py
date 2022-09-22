from intpy.intpy import initialize_intpy, deterministic
import time
import sys
import itertools

@deterministic
def chunks(n, l):
    """Divide a list of nodes `l` in `n` chunks"""
    l_c = iter(l)
    while 1:
        x = tuple(itertools.islice(l_c, n))
        if not x:
            return
        return x
      
      
 @initialize_intpy(__file__)
def main(n,l):
    print(chunks(n, l))
    
if __name__ == "__main__":
    n = (sys.argv[2])
    l = (sys.argv[4:])
    l.pop()
    l.pop()
    for i in range(len(l)):
      l[i]=l[i][:-1]
    start = time.perf_counter()
    main(n)
    print(time.perf_counter()-start)
