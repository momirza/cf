from matplotlib import pyplot

def compound_interest(W, r, n, m=1):
    """ compound interest calculator for given period and initial investment """
    return W*reduce(lambda x,y: x*y, [(1+r/m) for _ in xrange(n*m)], 1)

def future_value(stream, r, m=1):
    """ given a list of cashflows starting at t=0 return future value of stream at t=n """
    return sum([x*(1+r/m)**(len(stream)-k) for k, x in enumerate(stream)])

def present_value(stream, r, m=1):
    """ given a list of cashflows starting at t=0 return present value of stream """
    return sum([x/((1+r/m)**(k)) for k, x in enumerate(stream)])

def plot_compound_interest(W,r,n, m=1):
    xaxis = xrange(n)
    yaxis = [compound_interest(W, r, x, m) for x in xaxis]
    pyplot.bar(xaxis,yaxis)
    pyplot.xlabel("Time")
    pyplot.ylabel("Value")
    pyplot.title("Compound Interest with initial investment %s at rate %s" % (W,r))
    pyplot.savefig("Compound_Interest_%s" % (n))