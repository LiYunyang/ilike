import getdist.plots as gdplots
from matplotlib import pyplot as plt

def init(width_inch=7.01):
    """
    Initialize a GetDist plotter with the default settings.

    Parameters
    ----------
    width_inch: float, optional
        The width of the plot in inches. Default is 7.01 inches.

    Returns
    -------
    g : getdist.plots.GetDistPlotter
        The initialized GetDist plotter.

    """
    # plt.style.use('prd')
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    g = gdplots.get_subplot_plotter(
        width_inch=width_inch,
        rc_sizes=True,
        scaling=False,
    )
    s = g.settings

    # Colors
    s.line_styles = [("-", c) for c in colors]
    s.solid_colors = colors

    # Typography
    s.fontsize = plt.rcParams["font.size"]
    s.axes_labelsize = plt.rcParams["axes.labelsize"]
    s.axes_fontsize = plt.rcParams["xtick.labelsize"]
    s.legend_fontsize = plt.rcParams["legend.fontsize"]

    # Line widths
    s.linewidth = plt.rcParams["lines.linewidth"]
    s.linewidth_contour = plt.rcParams["lines.linewidth"]

    # Other styling
    s.num_plot_contours = 2
    s.solid_contour_palefactor = 0.65
    s.title_limit_fontsize = plt.rcParams["axes.titlesize"]
    return g
    g.triangle_plot(samples, pnames, filled=True, title_limit=1,
                    # contour_colors=colors[:2],
                    markers=dict(s8omegamp25=cosmos.s8omegamp25, Tcal_lens=1, Pcal_lens=1, Atsz=1, Acib=1,
                                 Arad=1)
                    )