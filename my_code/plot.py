## python 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from matplotlib import cycler
# Ipython_default=plt.rcParams.copy() # save initial value 
# plt.rcParams.update(Ipython_default) # load initial value 

def pp_dpi(dpi=72):
    pp.rc('figure',dpi=dpi) 

pp=plt

## ggplot
ro.r('library(ggplot2)')
import rpy2.robjects.lib.ggplot2 as gg
from rpy2.robjects.lib import grdevices
# from IPython.display import Image,display
def ggshow(gg, w=1,h=1,r=1):
    with grdevices.render_to_bytesio(grdevices.png,
                                     type="cairo-png",
                                     width=2000*w,
                                     height=1000*h,
                                     res=450*r,
                                     antialias="subpixel") as b:
        ro.r("print")(gg)
    data = b.getvalue()
    ip_img = Image(data=data, format='png', embed=True)
    return ip_img

def ggplot(data):
    if type(data) is rpy2.robjects.vectors.DataFrame:
        rtn=gg.ggplot(data)
    else: 
        rtn=gg.ggplot(p2r(pd.DataFrame(data)))
    return rtn
gg.plot=ggplot
gg.show=ggshow

## rrplot

