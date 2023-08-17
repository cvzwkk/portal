
import numpy as np
import matplotlib.pyplot as plt

def missile_trajectory(initial_velocity, angle_degrees, delta_v, time_interval):
    angle_radians = np.radians(angle_degrees)
    acceleration = delta_v / time_interval

    x_values = []
    y_values = []
    vx_values = []
    vy_values = []

    time = 0
    while True:
        x = initial_velocity * np.cos(angle_radians) * time
        y = initial_velocity * np.sin(angle_radians) * time - 0.5 * acceleration * time**2
        vx = initial_velocity * np.cos(angle_radians)
        vy = initial_velocity * np.sin(angle_radians) - acceleration * time

        if y < 0:
            break

        x_values.append(x)
        y_values.append(y)
        vx_values.append(vx)
        vy_values.append(vy)

        time += time_interval

    return x_values, y_values, vx_values, vy_values

# Input values
initial_velocity = 1000  # Initial velocity in m/s (changed from km/s)
angle_degrees = 45       # Launch angle in degrees
delta_v = 8              # Delta-v in km/s
time_interval = 1        # Time interval in seconds

# Calculate missile trajectory
x_vals, y_vals, vx_vals, vy_vals = missile_trajectory(initial_velocity, angle_degrees, delta_v, time_interval)

# Visualize the trajectory
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Missile Trajectory')
plt.xlabel('Distance (m)')
plt.ylabel('Altitude (m)')
plt.title('Missile Trajectory')
plt.legend()
plt.grid(True)
plt.show()
