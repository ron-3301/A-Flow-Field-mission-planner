import matplotlib.pyplot as plt
import numpy as np

def plot_mission(m_grid, p_raw, p_smooth):
    """quick plot of the mission area and paths"""
    plt.figure(figsize=(10, 8))
    plt.imshow(m_grid, cmap='viridis', origin='lower', alpha=0.6)
    p_arr = np.array(p_raw)
    plt.plot(p_arr[:, 1], p_arr[:, 0], 'r--', label='A* (Raw)', alpha=0.5)
    plt.plot(p_smooth[:, 1], p_smooth[:, 0], 'b-', linewidth=2, label=
        'Optimized')
    plt.legend()
    plt.title('Tactical Mission Plan')
    plt.show()
