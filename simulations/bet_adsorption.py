import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
BET Adsorption & Desorption Simulation (2D)
------------------------------------------
This simulation models the dynamic equilibrium of the BET model:
1. Adsorption:
   - Layer 0 -> 1: Chemisorption (High probability)
   - Layer 1+ -> 1+: Physisorption (Lower probability)
2. Desorption:
   - Layer 1 -> 0: Strong binding (Very low probability)
   - Layer 2+ -> 1+: Weak binding (Higher probability)
"""

# Simulation Configuration
WIDTH = 40
TOTAL_STEPS = 5000  # More steps to see equilibrium
P_ADS_CHEM = 0.8  # Adsorption on bare surface
P_ADS_PHYS = 0.3  # Adsorption on existing layers
P_DES_CHEM = 0.01  # Desorption of the 1st layer (Strong)
P_DES_PHYS = 0.15  # Desorption of upper layers (Weak)

# State
heights = np.zeros(WIDTH, dtype=int)
history = []


def simulate():
    current_heights = heights.copy()

    for i in range(TOTAL_STEPS):
        # 1. Attempt Adsorption
        x_ads = np.random.randint(0, WIDTH)
        h_ads = current_heights[x_ads]
        prob_ads = P_ADS_CHEM if h_ads == 0 else P_ADS_PHYS
        if np.random.random() < prob_ads:
            current_heights[x_ads] += 1

        # 2. Attempt Desorption
        x_des = np.random.randint(0, WIDTH)
        h_des = current_heights[x_des]
        if h_des > 0:
            prob_des = P_DES_CHEM if h_des == 1 else P_DES_PHYS
            if np.random.random() < prob_des:
                current_heights[x_des] -= 1

        if i % 10 == 0:
            history.append(current_heights.copy())


simulate()

# Visualization
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-0.5, WIDTH - 0.5)
ax.set_ylim(0, max(max(h) for h in history) + 3 if history else 10)
ax.set_title("BET Dynamic Equilibrium: Adsorption vs Desorption")
ax.set_xlabel("Surface Position")
ax.set_ylabel("Molecules Stacked (Layers)")

bars = ax.bar(range(WIDTH), np.zeros(WIDTH), color="gray", edgecolor="black")


def update(frame):
    h_data = history[frame]
    for i, bar in enumerate(bars):
        bar.set_height(h_data[i])
        if h_data[i] == 0:
            bar.set_color("lightgray")
        elif h_data[i] == 1:
            bar.set_color("darkblue")  # Chemisorption
        else:
            bar.set_color("skyblue")  # Physisorption
    return bars


ani = FuncAnimation(
    fig, update, frames=len(history), blit=True, repeat=False, interval=20
)

# Add equilibrium info to plot
plt.figtext(
    0.15,
    0.8,
    f"Ads Prob: Chem={P_ADS_CHEM}, Phys={P_ADS_PHYS}\nDes Prob: Chem={P_DES_CHEM}, Phys={P_DES_PHYS}",
    bbox=dict(facecolor="white", alpha=0.5),
)

print("Simulation complete. Showing dynamic equilibrium...")
plt.show()
