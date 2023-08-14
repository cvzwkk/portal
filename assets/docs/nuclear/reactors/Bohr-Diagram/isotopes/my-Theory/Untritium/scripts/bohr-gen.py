
import matplotlib.pyplot as plt
import numpy as np

def plot_bohr_diagram(energy_levels):
    plt.figure(figsize=(10, 10))
    plt.title('Bohr Diagram for Untritium-598 (Utt-598)')

    for level, electrons in energy_levels.items():
        radius = level * 0.5
        angle_increment = 2 * np.pi / electrons

        for i in range(electrons):
            angle = i * angle_increment
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            plt.scatter(x, y, color='blue', s=50)
            plt.text(x, y, f'{level}', ha='center', va='center', color='blue', fontsize=8)

    plt.gca().add_artist(plt.Circle((0, 0), 0.05, color='red', label='Protons (P)'))
    plt.text(0, 0, 'P', color='red', ha='center', va='center', fontsize=8)

    plt.axis('equal')
    plt.axis('off')
    plt.legend()

    plt.show()

# Electron configuration for untritium-598
energy_levels = {
    1: 2,    # 2 electrons in 1s orbital
    2: 14,   # 14 electrons in 2s and 2p orbitals
    3: 36,   # 36 electrons in 3s and 3p orbitals
    4: 54,   # 54 electrons in 4s and 4p orbitals
    5: 54,   # 54 electrons in 5s and 5p orbitals
    6: 36,   # 36 electrons in 6s and 6p orbitals
    7: 14,   # 14 electrons in 7s and 7p orbitals
    8: 4,    # 4 electrons in higher energy orbitals
}

plot_bohr_diagram(energy_levels)
