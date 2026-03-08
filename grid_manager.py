import numpy as np
import matplotlib.pyplot as plt

class GridManager:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.grid = np.ones((h, w), dtype=float)

    def set_obstacle(self, x, y):
        """no-go zone"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y, x] = float('inf')

    def set_threat(self, x, y, t_val):
        """add cost for threat areas"""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        self.grid[y, x] = t_val

    def visualize(self):
        plt.imshow(self.grid, cmap='viridis', origin='lower')
        plt.colorbar(label='Cost Weight')
        plt.title('Operational Environment (Cost Map)')
        plt.show()

if __name__ == '__main__':
    env = GridManager(20, 20)
    env.set_obstacle(5, 5)
    env.set_threat(10, 10, 5)
    env.visualize()
