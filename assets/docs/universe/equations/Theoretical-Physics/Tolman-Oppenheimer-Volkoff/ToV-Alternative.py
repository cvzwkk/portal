import math
import tabulate
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np  # Import the numpy module and give it an alias of np

atomic_masses = {
    "plutonium": 244,
    "uranium": 238,
    "curium": 247,
    "neptunium": 237,
    "americium": 243,
    "berkelium": 247,
    "californium": 251,
    "thorium": 232,
    "protactinium": 231,
    "actinium": 227,
    "thallium": 208,
    "rhenium": 186,
    "promethium": 145,
    "terbium": 158,
    "europium": 152,
    "holmium": 164,
    "ytterbium": 173,
    "lutetium": 175,
    "einsteinium": 252,
    "fermium": 257,
    "mendelevium": 258,
    "nobelium": 259,
    "lawrencium": 266,
    "rutherfordium": 267,
    "DeFi": 314
}

def calculate_properties(r, m, element):
    G = 6.67430e-11  # Gravitational constant in m^3/(kg·s^2)
    c = 299792458  # Speed of light in vacuum in m/s
    v = (4/3) * math.pi * r**3
    ρ = m / v
    atomic_mass = atomic_masses[element]
    P = (G * (ρ + c**2 * (m / (4*math.pi*r**3)))) / (3 * (1 - (2 * G * m) / (r * c**2 * atomic_mass)))
    dP_dr = - G * (ρ + P) * (m + (4/3) * math.pi * r**3 * P) / (r * (r - (2 * G * m) / (c**2 * atomic_mass)))
    return ρ, P, dP_dr

def calculate_sphere_weight(radius, thickness, sphere_density):
    # Calculate the internal and external volumes
    internal_volume = (4/3) * math.pi * radius**3
    external_radius = radius + thickness
    external_volume = (4/3) * math.pi * external_radius**3

    # Calculate the volume of the shell
    shell_volume = external_volume - internal_volume

    # Calculate the total weight
    sphere_weight = shell_volume * sphere_density

    return sphere_weight

def create_cluster():
    num_layers = int(input("Enter the number of layers in the cluster: "))
    cluster = []
    for i in range(num_layers):
        print(f"\nLayer {i+1}:")
        radius_unit = input("Choose the unit of measurement for the radius (1 for m, 2 for cm, 3 for mm): ")
        radius_option = int(radius_unit)
        radius = float(input("Enter the radius: "))

        # Ask the user to choose the unit of thickness
        thickness_unit = input("Choose the unit of measurement for the thickness (1 for m, 2 for cm, 3 for mm): ")
        thickness_option = int(thickness_unit)
        thickness_input = input("Enter the thickness of the sphere: ")
        thickness = float(thickness_input)
        if thickness_option == 2:
            thickness /= 100.0
        elif thickness_option == 3:
            thickness /= 1000.0

        # Ask the user to choose between kg and g for the alloy density
        density_unit = input("Choose the alloy density unit (1 for kg/m^3, 2 for g/m^3): ")
        density_option = int(density_unit)
        density_input = input("Enter the alloy density: ")
        density = float(density_input)
        if density_option == 2:
            density /= 1000.0  # Convert g/m^3 to kg/m^3
        
        mass_unit = input("Choose the Element mass unit (1 for t, 2 for kg, 3 for g, 4 for mg): ")
        mass_option = int(mass_unit)
        mass = float(input("Enter the Element mass: "))
        element = input("Choose the element (plutonium, uranium, curium): ")
        atomic_mass = atomic_masses[element]
        
        # Conversion of units to meters and kilograms
        if radius_option == 2:
            radius /= 100.0
        elif radius_option == 3:
            radius /= 1000.0
        if mass_option == 1:
            mass *= 1000.0
        elif mass_option == 3:
            mass /= 1000.0
        elif mass_option == 4:
            mass /= 1000000.0
        
        density, pressure, dP_dr = calculate_properties(radius, mass, element)

        sphere_weight = calculate_sphere_weight(radius, thickness, density)

        layer = {"Radius": radius, "Thickness": thickness,  "Sphere Density": density, "Sphere Weight": sphere_weight,  "Mass": mass, "Density": density, "Pressure": pressure, "dP/dr": dP_dr, "Element": element}
        cluster.append(layer)
    
    return cluster

# Get the molar fraction of Li-6 in the fuel from user input
li6_fraction = float(input("Enter the molar fraction of Li-6 in the lithium-deuteride fuel: "))

# Create the cluster
cluster = create_cluster()

def calculate_megatons_energy(mass, c=299792458):
    # Convert mass to energy using E=mc^2
    energy_joules = mass * c**2

    # Convert energy to megatons using the mass-energy equivalence: 1 MT = 4.184e15 Joules
    energy_megatons = energy_joules / (4.184e15)

    return energy_megatons


print("\nCluster Properties:")
total_megatons = 0  # Initialize the total megatons produced by all clusters together
for i, layer in enumerate(cluster):
    print(f"\nLayer {i+1}:")
    print("Radius: {:.2f} meters".format(layer["Radius"]))
    print("Thickness: {:.2f} meters".format(layer["Thickness"]))
    print("Sphere Density: {:.2f} kg/m^3".format(layer["Sphere Density"]))
    print("Sphere Weight: {:.2f} kg".format(layer["Sphere Weight"]))

    print("Element: {}".format(layer["Element"]))
    print("Mass: {:.2f} kilograms".format(layer["Mass"]))
    print("Density: {:.2f} kg/m^3".format(layer["Density"]))
    print("Pressure: {:.2f} N/m^2".format(layer["Pressure"]))
    print("dP/dr: {:.2f} N/(m^2/m)".format(layer["dP/dr"]))

    # Calculate and display the fuel quantity
    fuel_quantity = li6_fraction * layer["Mass"]
    print("Fuel Quantity: {:.2f} kilograms".format(fuel_quantity))

    # Calculate and display the megatons produced by the cluster
    cluster_energy_megatons = calculate_megatons_energy(layer["Sphere Weight"] + layer["Mass"])
    print("Energy Produced: {:.2f} megatons".format(cluster_energy_megatons))

    # Accumulate the megatons produced by the cluster in the total_megatons variable
    total_megatons += cluster_energy_megatons

# Calculate the total cluster weight including elements
total_cluster_weight = sum(layer["Sphere Weight"] + layer["Mass"] for layer in cluster)
print("Total Cluster Weight: {:.2f} kg".format(total_cluster_weight))

# Calculate and display the total fuel quantity
total_fuel_quantity = sum(li6_fraction * layer["Mass"] + layer["Sphere Weight"] for layer in cluster)
print("\nTotal Fuel Quantity: {:.2f} kilograms".format(total_fuel_quantity))

# Display the total megatons produced by all clusters together
print("Total Energy Produced by All Clusters: {:.2f} megatons".format(total_megatons))


# Calculate the total cluster weight including elements
total_cluster_weight = sum(layer["Sphere Weight"] + layer["Mass"] for layer in cluster)
print("Total Cluster Weight: {:.2f} kg".format(total_cluster_weight))

# Calculate and display the total fuel quantity
total_fuel_quantity = sum(li6_fraction * layer["Mass"] + layer["Sphere Weight"] for layer in cluster)
print("\nTotal Fuel Quantity: {:.2f} kilograms".format(total_fuel_quantity))

# Define the colormap for the outer spheres (grayscale)
gray_cmap = LinearSegmentedColormap.from_list("gray_cmap", [(0, "gray"), (1, "gray")])

# Create the 3D plot of the cluster
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add the layers to the plot
for i, layer in enumerate(cluster):
    r = layer["Radius"]
    density = layer["Density"]
    
    if i == 0:
        color = 'red'  # Innermost sphere is red
        alpha = 0.7  # No transparency for innermost sphere
    else:
        # Grayscale color based on density
        color = gray_cmap((density - min([l["Density"] for l in cluster])) / (max([l["Density"] for l in cluster]) - min([l["Density"] for l in cluster])))
        alpha = 0.3  # Complete transparency for outer spheres
    
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = r * np.cos(u) * np.sin(v)
    y = r * np.sin(u) * np.sin(v)
    z = r * np.cos(v)
    ax.plot_surface(x, y, z, color=color, alpha=alpha, edgecolor='none')

# Add smaller clusters inside the larger ones
if i < len(cluster) - 1:
    r1 = layer["Radius"]
    r2 = cluster[i+1]["Radius"]
    x1, y1, z1 = np.mgrid[-r1:r1:2*r2*1j, -r1:r1:2*r2*1j, -r1:r1:2*r2*1j]
    inside = (x1**2 + y1**2 + z1**2) < r2**2
    x2, y2, z2 = np.broadcast_to(np.array([x[i], y[i], z[i]]), x1.shape)
    facecolors = np.broadcast_to(np.array([(color, 0, 1-color)]), x1.shape + (3,))
    ax.voxels(x2, y2, z2, inside, facecolors=facecolors, edgecolor='k', alpha=0.2)

# Set the limits of the plot
max_radius = max([l["Radius"] for l in cluster])
ax.set_xlim([-max_radius, max_radius])
ax.set_ylim([-max_radius, max_radius])
ax.set_zlim([-max_radius, max_radius])

# Add labels to the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Save the image in .png format
plt.savefig("cluster.png")

# Create a new figure for displaying the properties

massa_total = sum(layer["Mass"] for layer in cluster)

fig_prop = plt.figure(figsize=(11, 5))
text_ax = fig_prop.add_subplot(111)
text_ax.axis('off')
table_data = []
headers = ["Layer", "Radius (m)", "Mass (kg)", "Density (kg/m^3)", "Pressure (N/m^2)", "dP/dr (N/(m^2/m))", "Element", "Fuel Amount", "Total Fuel Amount"]
for i, layer in enumerate(cluster):
    row = [
        i+1,
        "{:.2f}".format(layer["Radius"]),
        "{:.2f}".format(layer["Mass"]),
        "{:.2f}".format(layer["Density"]),
        "{:.2f}".format(layer["Pressure"]),
        "{:.2f}".format(layer["dP/dr"]),
        layer["Element"],
        "{:.2f}".format(total_fuel_quantity)
    ]
    table_data.append(row)

table_text = tabulate.tabulate(table_data, headers=headers, tablefmt="pretty")
text_ax.text(0., 0.7, table_text, fontsize=10)

# Adjust the layout to fill the empty space
#plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.tight_layout()

# Save the properties as a separate image
plt.savefig("cluster_properties.png")
