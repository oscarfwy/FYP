from matplotlib import pyplot as plt
import pandas as pd


def draw(new,old):



    #df=pd.DataFrame(dict)
    pd.plotting.register_matplotlib_converters()


    plt.plot(new, label='index tracking')
    plt.plot(old,label='Original')

    plt.legend(loc='upper right')
    plt.show()



