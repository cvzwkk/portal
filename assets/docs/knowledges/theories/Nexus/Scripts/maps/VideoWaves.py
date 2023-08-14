
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sample data representing a fractal pattern
sample_fractal_data = np.random.randint(0, 2, size=1000)
box_size = 10

# Set up the figure and axis for the animation
fig_anim = plt.figure(figsize=(12, 6))
ax_waveform = plt.subplot(2, 1, 1)
ax_gravitational = plt.subplot(2, 1, 2)
time_values = np.linspace(0, 1, len(sample_fractal_data))

# Animation function
def update_animation(frame):
    ax_waveform.clear()
    ax_gravitational.clear()

    # Update wave function values
    frequency_wave = (frame + 1) * 1.23e41  # Adjust frequency for animation
    amplitude_wave = 5.67e-20  # Scientific notation: 5.67 × 10^-20
    waveform = amplitude_wave * np.sin(2 * np.pi * frequency_wave * time_values)
    
    ax_waveform.plot(time_values, waveform, color='purple')
    ax_waveform.set_title("Waveform Visualization - Frame: " + str(frame + 1))
    ax_waveform.set_xlabel("Time")
    ax_waveform.set_ylabel("Amplitude")

    # Update gravitational wave values
    frequency_gravitational = (frame + 1) * 1.23e-17  # Adjust frequency for animation
    amplitude_gravitational = 2.45e-26  # Hypothetical amplitude for gravitational waves
    gravitational_waveform = amplitude_gravitational * np.sin(2 * np.pi * frequency_gravitational * time_values)

    ax_gravitational.plot(time_values, gravitational_waveform, color='blue')
    ax_gravitational.set_title("Gravitational Wave Visualization - Frame: " + str(frame + 1))
    ax_gravitational.set_xlabel("Time")
    ax_gravitational.set_ylabel("Amplitude")

# User input for video duration
duration_minutes = 4
frame_interval = 100  # milliseconds
num_frames = (duration_minutes * 60 * 1000) // frame_interval

# Create an animation
animation = FuncAnimation(fig_anim, update_animation, frames=num_frames, interval=frame_interval)

# Export the animation as a video
video_filename = 'waveform_and_gravitational_animation.mp4'
animation.save(video_filename, writer='ffmpeg')

print(f"Animation saved as '{video_filename}'")
plt.show()  # To display the final frame of the animation
