import numpy as np

class ThreatEngine:

    @staticmethod
    def inject_radar_bubble(mgr, pos, r, t_cost):
        """slaps a circular cost zone onto the grid"""
        h = mgr.height
        w = mgr.width
        y, x = np.ogrid[:h, :w]
        d_map = np.sqrt((x - pos[0]) ** 2 + (y - pos[1]) ** 2)
        mask = d_map <= r
        mgr.grid[mask] = np.maximum(mgr.grid[mask], t_cost)

    @staticmethod
    def inject_no_fly_zone(mgr, p1, p2):
        """hard block for a rectangular area"""
        x1, y1 = p1
        x2, y2 = p2
        mgr.grid[y1:y2, x1:x2] = float('inf')
