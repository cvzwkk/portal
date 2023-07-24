import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
massa_sol = 1.989e30  # kg
distancia_media = 147_098_074.2  # km (average distance Earth-Sun, approximate)
periodo_orbital = 365.256  # days (orbital period of Earth)

# Convert distance to AU (astronomical units)
distancia_media_au = distancia_media / 149_597_870.7  # 1 AU is approximately 149.6 million kilometers

# Create the figure and 3D axis objects
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Earth and Sun properties
earth_radius = 6371  # km
sun_radius = 6.96e5  # km

# Plot the Sun as a sphere
ax.scatter(0, 0, 0, c='yellow', marker='o', s=1000)

# Plot the Earth as a sphere
ax.scatter(distancia_media_au, 0, 0, c='blue', marker='o', s=100)

# Set plot limits
ax.set_xlim(-distancia_media_au, distancia_media_au)
ax.set_ylim(-distancia_media_au, distancia_media_au)
ax.set_zlim(-distancia_media_au, distancia_media_au)

# Add labels for Sun and Earth
ax.text(0, 0, 0, 'Sun', color='black', fontsize=12, ha='center', va='center')
ax.text(distancia_media_au, 0, 0, 'Earth', color='black', fontsize=12, ha='center', va='center')

# Set axis labels
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')

# Set the title
ax.set_title('3D Representation of Earth and Sun')

# Add annotations for the variables
annotations = [
    ("Sun Mass (kg)", massa_sol, (0.2, 0.2, 0.7)),
    ("Earth Radius (km)", earth_radius, (0.2, 0.2, 0.5)),
    ("Orbital Period of Earth (days)", periodo_orbital, (0.2, 0.2, 0.3)),
]

for annotation, value, position in annotations:
    ax.text2D(0.05, 0.95 - annotations.index((annotation, value, position)) * 0.1, f"{annotation}: {value:.2e}", transform=ax.transAxes, fontsize=10, color=position)

# Save the plot as a PNG image
plt.savefig('earth_sun_3d_plot.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
