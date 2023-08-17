
import numpy as np
from scipy.optimize import minimize_scalar

def target_function(angle, distance, projectile_mass, initial_velocity):
    g = 9.81  # Acceleration due to gravity in m/s^2
    angle_radians = np.radians(angle)

    time_of_flight = (2 * initial_velocity * np.sin(angle_radians)) / g
    horizontal_distance = initial_velocity * np.cos(angle_radians) * time_of_flight

    return abs(horizontal_distance - distance)

# Input values
target_distance = float(input("Enter the target distance (meters): "))
projectile_mass = float(input("Enter the projectile mass (kg): "))
initial_velocity = float(input("Enter the initial velocity (m/s): "))

# Use numerical optimization to find firing angle
result = minimize_scalar(target_function, bounds=(0, 90), args=(target_distance, projectile_mass, initial_velocity))

if result.success:
    firing_angle = result.x
    print(f"The firing angle to hit the target at {target_distance} meters is approximately {firing_angle:.2f} degrees.")
else:
    print("Error in optimization. No firing angle solution found.")
