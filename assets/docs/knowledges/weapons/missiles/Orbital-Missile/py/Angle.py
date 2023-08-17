import matplotlib.pyplot as plt
import numpy as np

# Angles in degrees
angles = np.arange(0, 101, 10)

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting lines for each angle
for angle in angles:
    # Convert angle to radians
    radians = np.radians(angle)

    # Calculate coordinates for the line
    x = np.array([0, np.cos(radians)])
    y = np.array([0, np.sin(radians)])

    # Plot the line
    ax.plot(x, y, label=f'{angle}°')

# Set equal aspect ratio and limit plot range
ax.set_aspect('equal', 'box')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Add labels for quadrants
ax.annotate('0°', xy=(1.02, 0.02), color='blue')
ax.annotate('90°', xy=(0.02, 1.02), color='blue')
ax.annotate('180°', xy=(-1.08, 0.02), color='blue')
ax.annotate('270°', xy=(0.02, -1.08), color='blue')

# Set plot title and legend
plt.title('Lines Representing Different Angles')
plt.legend(title='Angles')

# Show the plot
plt.grid(True)
plt.show()
