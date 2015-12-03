# -*- coding: utf-8 -*-
"""
This script generates all the relevant figures from the experiment.
"""

from pyrm2tt.processing import *
from pyrm2tt.plotting import *

set_sns()
save = False
savetype = ".eps"
show = True

def main():
    plot_perf_curves(save=save, savetype=savetype)
    plot_perf_curves(subplots=False, save=save, savetype=savetype)
    plot_perf_re_dep(save=save, savetype=savetype, errorbars=False,
                     dual_xaxes=True)
    PerfCurve(1.0).plotcp(save=save, savetype=savetype, show=False)
    wm = WakeMap()
    wm.plot_meancontquiv(save=save, savetype=savetype)
    wm.plot_k(save=save, savetype=savetype)
    wm.make_K_bar_graph(save=save, savetype=savetype)
    plot_no_blades_all(save=save, savetype=savetype)
    plot_cp_covers(save=save, savetype=savetype, add_strut_torque=False)
    plot_cp_covers(save=save, savetype=savetype, add_strut_torque=True)
    if show:
        plt.show()

if __name__ == "__main__":
    if not os.path.isdir("Figures"):
        os.mkdir("Figures")
    main()