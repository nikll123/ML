import matplotlib.pyplot as plt

def myPlotterHelper(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


def doPlot(x_values, y_values):
   """
    A helper function to make a graph

    Parameters
    ----------
    x_values : array
       The x data

    y_values : array
       The y data

    Returns
    -------
       visualization

   """
   fig, ax = plt.subplots(1, 1)
   myPlotterHelper(ax, x_values, y_values, {'marker': 'x'})
   plt.show()
