import matplotlib.pyplot as plt
from collections import Counter
import pylab
from master_and_margaret import *

def sentencesBar():
    symbols = ['.','!','?']

    for i in range(0, len(symbols)):
        xdata = [symbols[i]]
        ydata = [text.count(symbols[i])]
        pylab.bar(xdata, ydata)

    pylab.show()

sentencesBar()
