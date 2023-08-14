
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting
from scipy.constants import hbar, m_e


# Fractals and Chaos
def fractal_dimension(data, box_size):
    num_boxes = len(data) // box_size
    counts = np.zeros(num_boxes)

    for i in range(num_boxes):
        box_data = data[i * box_size: (i + 1) * box_size]
        counts[i] = np.sum(box_data)

    nonzero_counts = counts[counts > 0]
    num_nonzero_boxes = len(nonzero_counts)

    fractal_dimension = np.log(num_nonzero_boxes) / np.log(1.0 / box_size)
    return fractal_dimension

# Calculate energy level based on Quantum Mechanics
def energy_level(n, L):
    return (n**2 * hbar**2 * np.pi**2) / (2 * m_e * L**2) 

# Main script
if __name__ == "__main__":
    # Sample data representing a fractal pattern
    sample_fractal_data = np.random.randint(0, 2, size=1000)

    # Set the size of the boxes for box-counting
    box_size = 10
    fractal_dim = fractal_dimension(sample_fractal_data, box_size)

    # Quantum Mechanics calculation
    n = 3  # Quantum level
    L = 1e-10  # Length of the well in meters
    eigenvalue = energy_level(n, L)

    # Combine results and interpret
    combined_result = fractal_dim * eigenvalue

    # Scatter plot
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    plt.scatter(np.arange(len(sample_fractal_data)), sample_fractal_data, s=5)
    plt.title("Scatter Plot")

    # 2D plot
    plt.subplot(2, 2, 2)
    plt.plot(np.arange(len(sample_fractal_data)), sample_fractal_data)
    plt.title("2D Plot")

    # 3D plot
    plt.subplot(2, 1, 2, projection='3d')
    x = np.arange(len(sample_fractal_data))
    y = np.random.randint(0, 2, size=len(sample_fractal_data))
    z = sample_fractal_data
    plt.scatter(x, y, z)
    plt.title("3D Plot")

    # Waves
    # Sample data representing a fractal pattern
    sample_fractal_data = np.random.randint(0, 2, size=1000)

    # Set the size of the boxes for box-counting
    box_size = 10
    fractal_dim = fractal_dimension(sample_fractal_data, box_size)

    # Quantum Mechanics calculation
    n = 3  # Quantum level
    L = 1e-10  # Length of the well in meters
    eigenvalue = energy_level(n, L)

    # Combine results and interpret
    combined_result = fractal_dim * eigenvalue

    # Scatter plot, 2D plot, 3D plot (same as before)

    # Waveform visualization
    plt.figure(figsize=(8, 4))
    time = np.linspace(0, 1, len(sample_fractal_data))
    frequency = 42 # Adjust frequency as needed
    amplitude = 13
    waveform = amplitude * np.sin(2 * np.pi * frequency * time)

    plt.subplot(2, 2, 3)
    plt.plot(time, waveform, color='purple')
    plt.title("Waveform Visualization")


    print("Combined Result:", combined_result)

    plt.tight_layout()
    plt.show()

    print("Combined Result:", combined_result)
