from matplotlib import pyplot

def compound_interest(W, r, n, m=1):
    return W*reduce(lambda x,y: x*y, [(1+r/m) for _ in xrange(n*m)], 1)

def plot_compound_interest(W,r,n, m=1):
    xaxis = xrange(n)
    yaxis = [compound_interest(W, r, x, m) for x in xaxis]
    pyplot.bar(xaxis,yaxis)
    pyplot.xlabel("Time")
    pyplot.ylabel("Value")
    pyplot.title("Compound Interest with initial investment %s at rate %s" % (W,r))
    pyplot.savefig("Compound_Interest_%s" % (n))