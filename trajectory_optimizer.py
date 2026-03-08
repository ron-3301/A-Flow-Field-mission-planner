import numpy as np
from scipy.interpolate import CubicSpline

def smooth_path(pts, n_steps=100):
    """spline smoothing for the jagged path"""
    pts = np.array(pts)
    px = pts[:, 0]
    py = pts[:, 1]
    idx = np.arange(len(pts))
    sx = CubicSpline(idx, px)
    sy = CubicSpline(idx, py)
    idx_new = np.linspace(0, len(pts) - 1, n_steps)
    out_x = sx(idx_new)
    out_y = sy(idx_new)
    return np.vstack((out_x, out_y)).T
