import matplotlib.pyplot as plt

def plot_raien_diagram():
    # Define diagram elements
    elements = ['Rare Earth Element Cavity Stabilizers (REECS)',
                'Implosion-Based Energy Generator',
                'Rocket Nozzle',
                'Superconducting Electromagnets',
                'Reactor Core']

    # Define connections between elements
    connections = [('Rare Earth Element Cavity Stabilizers (REECS)', 'Reactor Core'),
                   ('Implosion-Based Energy Generator', 'Reactor Core'),
                   ('Reactor Core', 'Rocket Nozzle'),
                   ('Reactor Core', 'Superconducting Electromagnets')]

    # Create a plot and set its size
    plt.figure(figsize=(10, 6))

    # Draw nodes (elements)
    for element in elements:
        plt.scatter(0, elements.index(element), marker='o', s=500, label=element)

    # Draw connections (lines)
    for conn in connections:
        start_idx = elements.index(conn[0])
        end_idx = elements.index(conn[1])
        plt.plot([0, 0], [start_idx, end_idx], 'k-')

    # Set plot properties
    plt.xticks([])
    plt.yticks(range(len(elements)), elements)
    plt.title('RAIEN Atomic Engine Diagram')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()

    # Save the diagram to an image file
    plt.savefig('raien_atomic_engine_diagram.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_raien_diagram()
