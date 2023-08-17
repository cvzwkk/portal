
import numpy as np
import matplotlib.pyplot as plt

def calculate_trajectory(initial_velocity, angle_degrees):
    g = 9.81  # Acceleration due to gravity in m/s^2
    angle_radians = np.radians(angle_degrees)
    time_interval = 0.01
    
    x_values = []
    y_values = []
    
    time = 0
    while True:
        x = initial_velocity * np.cos(angle_radians) * time
        y = initial_velocity * np.sin(angle_radians) * time - 0.5 * g * time**2
        
        if y < 0:
            break
        
        x_values.append(x)
        y_values.append(y)
        
        time += time_interval
        
    return x_values, y_values

# Input values
target_distance = float(input("Enter the target distance (meters): "))
projectile_mass = float(input("Enter the projectile mass (kg): "))
initial_velocity = float(input("Enter the initial velocity (m/s): "))

# Use numerical optimization to find firing angle
result = minimize_scalar(target_function, bounds=(0, 90), args=(target_distance, projectile_mass, initial_velocity))

if result.success:
    firing_angle = result.x
    print(f"The firing angle to hit the target at {target_distance} meters is approximately {firing_angle:.2f} degrees.")
    
    # Calculate trajectory
    x_vals, y_vals = calculate_trajectory(initial_velocity, firing_angle)
    
    # Plot trajectory
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Projectile Trajectory')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')
    plt.title('Projectile Trajectory')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Error in optimization. No firing angle solution found.")
