import matplotlib as mpl 
import matplotlib.pyplot as plt 
from matplotlib import cycler
# Ipython_default=plt.rcParams.copy() # save initial value 
# plt.rcParams.update(Ipython_default) # load initial value 
def plt_dpi(dpi=72):
    plt.rc('figure',dpi=dpi) 

