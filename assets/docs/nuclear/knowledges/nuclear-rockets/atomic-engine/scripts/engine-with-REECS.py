import matplotlib.pyplot as plt

# Function to draw a rocket with REECS components
def draw_reecs_diagram():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_axis_off()

    # Draw the rocket body
    rocket_body = plt.Rectangle((0, 0), 4, 12, fc='gray', edgecolor='black')
    ax.add_patch(rocket_body)

    # Draw the exhaust nozzle
    exhaust_nozzle = plt.Rectangle((1.5, -1), 1, 1, fc='darkgray', edgecolor='black')
    ax.add_patch(exhaust_nozzle)

    # Draw the heat exchangers
    heat_exchanger_1 = plt.Rectangle((0, 8), 4, 1.5, fc='lightblue', edgecolor='black')
    heat_exchanger_2 = plt.Rectangle((0, 9.5), 4, 1.5, fc='lightblue', edgecolor='black')
    ax.add_patch(heat_exchanger_1)
    ax.add_patch(heat_exchanger_2)

    # Draw the turbines
    turbine_1 = plt.Rectangle((0.5, 5.5), 3, 1.5, fc='lightgreen', edgecolor='black')
    turbine_2 = plt.Rectangle((0.5, 7), 3, 1.5, fc='lightgreen', edgecolor='black')
    ax.add_patch(turbine_1)
    ax.add_patch(turbine_2)

    # Draw the generators
    generator_1 = plt.Rectangle((1.5, 3), 1, 2, fc='lightcoral', edgecolor='black')
    generator_2 = plt.Rectangle((1.5, 0.5), 1, 2, fc='lightcoral', edgecolor='black')
    ax.add_patch(generator_1)
    ax.add_patch(generator_2)

    # Draw arrows to represent energy flow
    arrow_kwargs = dict(arrowstyle='->', lw=1.5, color='black')
    ax.annotate("", xy=(2, 11), xytext=(2, 9.7), arrowprops=arrow_kwargs)
    ax.annotate("", xy=(2, 6), xytext=(2, 4.7), arrowprops=arrow_kwargs)
    ax.annotate("", xy=(2, 3), xytext=(2, 1.7), arrowprops=arrow_kwargs)

    # Label the components
    ax.text(2, 11.2, "Exhaust Gases", ha='center', va='bottom', fontsize=8)
    ax.text(2, 9.3, "Heat Exchangers", ha='center', va='bottom', fontsize=8)
    ax.text(2, 7.8, "Turbines", ha='center', va='bottom', fontsize=8)
    ax.text(2, 4.2, "Generators", ha='center', va='bottom', fontsize=8)

    # Set plot limits and display the diagram
    ax.set_xlim(0, 4)
    ax.set_ylim(-2, 12)
    plt.show()
    plt.savefig("rocket_with_reecs.png", dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    draw_reecs_diagram()
