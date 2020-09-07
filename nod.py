"""
A collect of useful functions
"""
import numpy as np

def remove_duplicates(seq): 
    """Remove duplicates from a sequence while preserving the order"""
    unique = []
    [unique.append(i) for i in seq if not unique.count(i)]
    return unique


def jitter_scatter(ax, x_labels, y, label=None, style='o', x_set=None):
    """
    Add a scatter plot with x-axis jitter
    Parameters
    ----------
    x_labels : list
        list of labels
    y : list
        list of y values
    ax : matplotlib.pyplot.axes
        axis to plot on
    style : string
        linestyle
    x_set : list
        if a custom x_tick order is desired
    """
    if not x_set:
        # find unique labels
        x_set = remove_duplicates(x_labels)
    # assign integer vals
    x_vals = [x_set.index(label) for label in x_labels]
    # add "jitter"
    x = np.random.normal(x_vals, 0.04)
    # add to plot axis
    ax.plot(x, y, style, label=label)
    ax.set_xticks(list(range(len(x_set))))
    ax.set_xticklabels(x_set)


def jitter_scatter_old(y_list, ax, x_labels=None):
    '''Add a scatter plot with x-axis jitter'''
    xticks = list(range(1, len(y_list) + 1))
    for x in xticks:
        import ipdb; ipdb.set_trace()
        x_vals = np.random.normal(x, 0.04, size=len(y_list[x-1]))
        ax.plot(x_vals, y_list[x-1], 'ro')

    if x_labels:
        ax.set_xticks(xticks)
        ax.set_xticklabels(x_labels)


