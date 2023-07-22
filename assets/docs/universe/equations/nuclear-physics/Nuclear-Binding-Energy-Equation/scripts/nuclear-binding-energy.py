def energy_per_nucleon(element, mass, unit='kg'):
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

    if element.lower() not in atomic_masses:
        print(f"O elemento {element} não está na lista de elementos suportados.")
        return None

    mass_nucleon = 1.66053906660e-27  # kg (massa de 1 núcleon em kg)
    speed_of_light = 299792458  # m/s (velocidade da luz no vácuo)

    A = atomic_masses[element.lower()]
    Z = A - mass  # Número de prótons no núcleo
    N = mass      # Número de nêutrons no núcleo

    M = Z * 1.00727646688 + N * 1.00866491588  # Massa do núcleo em kg

    if unit.lower() == 'kg':
        mass_in_kg = mass
    elif unit.lower() == 'g':
        mass_in_kg = mass / 1000
    else:
        print("Unidade não suportada. Use 'kg' ou 'g'.")
        return None

    energy_per_nucleon = (Z * (1.00727646688 * speed_of_light**2) +
                          N * (1.00866491588 * speed_of_light**2) - M) / A

    return energy_per_nucleon * mass_in_kg


# Exemplo de uso:
element = input("Digite o elemento para calcular a energia de ligação por núcleon: ")
mass = float(input("Digite a quantidade do elemento (em kg ou g): "))
unit = input("Unidade (kg ou g): ")

energy = energy_per_nucleon(element, mass, unit)
if energy is not None:
    print(f"A energia de ligação por núcleon para {mass} {unit} de {element} é {energy:.8e} J/núcleon.")
