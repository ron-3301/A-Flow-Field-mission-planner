import numpy as np
from grid_manager import GridManager
from threat_engine import ThreatEngine
from pathfinder import find_path
from trajectory_optimizer import smooth_path
from viz_engine import plot_mission
G_DIM = 20, 20
START = 0, 0
GOAL = 19, 19
WALLS = [(17, 0), (19, 17), (7, 0)]
RADAR_XY = 2, 10
RADAR_R = 7
DANGER_VAL = 5
env = GridManager(*G_DIM)
for w in WALLS:
    env.set_obstacle(*w)
ThreatEngine.inject_radar_bubble(env, RADAR_XY, RADAR_R, DANGER_VAL)
path = find_path(env.grid, START, GOAL)
if path:
    s_path = smooth_path(path)
    plot_mission(env.grid, path, s_path)
else:
    print('No path found.')
