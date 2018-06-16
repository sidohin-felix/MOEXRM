import numpy
import math

class fBM:
    
    def fBM(self,H,n,T):
        r = [1]
        if H < 0 or H > 1:
            return None
        if n is None:
            n = math.pow(2,12)
        else:
            n = math.pow(2,math.ceil(math.log(n,2)))
        r = []
        r.append(1)
        for i in range(1,int(n)):
            x = 0.5*( math.pow(i+1,2*H) - 2*math.pow(i,2*H) + math.pow(i-1,2*H)  )
            r.append(x)
        r = r + list(reversed(r[1:-1]))
        V = numpy.fft.fft(r).real / (2*n)
        W = []
        for v in V:
            z = numpy.sqrt(v) * numpy.complex(numpy.random.normal(0,1),numpy.random.normal(0,1))
            W.append(z)
        W = numpy.fft.fft(W)
        W = numpy.power(n,-1*H)*numpy.cumsum(numpy.real(W[1:int(n)+1]))
        W = numpy.power(T,H)*W
        return W

    def compositefBM(self,H,n,T):
        X = []
        while(len(H) != 0):
            h = numpy.random.choice(H)
            if(len(X) == 0):
                X = self.fBM(h,n,T)
            else:
                X = X + self.fBM(h,n,T)
            H.remove(h)
        return X