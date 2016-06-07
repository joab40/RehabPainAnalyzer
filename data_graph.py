import matplotlib.pyplot as plt
import numpy as np

#fname = open('msft.csv.org')
fname = open('test.csv')


plt.plotfile(fname, ('date','emotion','headache','hipleft','hipright','shoulderleft','shoulderright','spinallow','spinalmiddle','spinalneck'), subplots=False)

#plt.figtext("hello")
plt.xlabel(r'$date$')
plt.ylabel(r'$levels$')



plt.show()
plt.savefig('data_graph.png')