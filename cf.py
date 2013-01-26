from matplotlib import pyplot

def compound_interest(W, r, n, m=1):
    """ compound interest calculator for given period and initial investment """
    return W*reduce(lambda x,y: x*y, [(1+r/m) for _ in xrange(n*m)], 1)

def future_value(stream, r, m=1):
    """ given a list of cashflows starting at t=0 return future value of stream at t=n """
    return sum([x*(1+r/m)**(len(stream)-k) for k, x in enumerate(stream)])

def present_value(stream, r, m=1, time=0):
    """ given a list of cashflows starting at t=0 return present value of stream """
    return sum([x/((1+r/m)**(k)) for k, x in enumerate(stream[time:])])

def forward_rate(start, end, start_spot, end_spot):
    """ NB not to be confused with a market forward rate """
    return (((1.0+end_spot)**end)/(1.0+start_spot)**start)**(1.0/(end-start)) -1

def future_rates(curve):
    """ returns spot rate curve for next year under expectation dynamics """
    start_rate = curve.pop(0)
    return [forward_rate(1, n+2, start_rate, s) for n,s in enumerate(curve)]

def plot_compound_interest(W,r,n, m=1):
    xaxis = xrange(n)
    yaxis = [compound_interest(W, r, x, m) for x in xaxis]
    pyplot.bar(xaxis,yaxis)
    pyplot.xlabel("Time")
    pyplot.ylabel("Value")
    pyplot.title("Compound Interest with initial investment %s at rate %s" % (W,r))
    pyplot.savefig("Compound_Interest_%s" % (n))