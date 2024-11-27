import matplotlib as mpl
from IPython.core.display import HTML
    # Make widget backgrounds transparent
html = r"""

         <style>
         .cell-output-ipywidget-background {
         background-color: transparent !important;
        }
         .jp-OutputArea-output {
         background-color: transparent;
        }
         </style>
"""
def use():
# Set some default colors
    bgcol = '#3f3f3f'
    mpl.rcParams['figure.figsize'] = (12, 6)
    mpl.rcParams['axes.facecolor'] = bgcol
    mpl.rcParams['axes.edgecolor'] = 'white'
    mpl.rcParams['axes.labelcolor'] = 'white'
    mpl.rcParams['xtick.color'] = 'white'
    mpl.rcParams['ytick.color'] = 'white'
    mpl.rcParams['text.color'] = 'white'
    mpl.rcParams['figure.facecolor'] = bgcol
    mpl.rcParams['figure.edgecolor'] = bgcol
    mpl.rcParams['savefig.facecolor'] = bgcol
    mpl.rcParams['savefig.edgecolor'] = bgcol
    
    # Set plot colour cycling defaults
    cmap = [
        [9.88362e-01, 9.98364e-01, 6.44924e-01, 1.00000e+00],
        [7.29909e-01, 2.12759e-01, 3.33861e-01, 1.00000e+00],
        [1.46200e-03, 4.66000e-04, 1.38660e-02, 1.00000e+00],
        [0.993248, 0.906157, 0.143936, 1.      ],
        [0.128729, 0.563265, 0.551229, 1.      ],
        [0.267004, 0.004874, 0.329415, 1.      ]
    ]
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=cmap)
    HTML(html)
