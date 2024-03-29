# Define a dictionary with elements and their molar masses
elements_directory = {
    'H': 1.01,
    'He': 4.00,
    'Li': 6.94,
    'Be': 9.01,
    'B': 10.81,
    'C': 12.01,
    'N': 14.01,
    'O': 16.00,
    'F': 19.00,
    'Ne': 20.18,
    'Na': 22.99,
    'Mg': 24.31,
    'Al': 26.98,
    'Si': 28.09,
    'P': 30.97,
    'S': 32.07,
    'Cl': 35.45,
    'Ar': 39.95,
    'K': 39.10,
    'Ca': 40.08,
    'Sc': 44.96,
    'Ti': 47.87,
    'V': 50.94,
    'Cr': 51.99,
    'Mn': 54.94,
    'Fe': 55.85,
    'Ni': 58.69,
    'Co': 58.93,
    'Cu': 63.55,
    'Zn': 65.38,
    'Ga': 69.72,
    'Ge': 72.63,
    'As': 74.92,
    'Se': 78.97,
    'Br': 79.90,
    'Kr': 83.80,
    'Rb': 85.47,
    'Sr': 87.62,
    'Y': 88.91,
    'Zr': 91.22,
    'Nb': 92.91,
    'Mo': 95.94,
    'Tc': 98.00,
    'Ru': 101.1,
    'Rh': 102.9,
    'Pd': 106.4,
    'Ag': 107.9,
    'Cd': 112.4,
    'In': 114.8,
    'Sn': 118.7,
    'Sb': 121.8,
    'Te': 127.6,
    'I': 126.9,
    'Xe': 131.3,
    'Cs': 132.9,
    'Ba': 137.3,
    'La': 138.9,
    'Ce': 140.1,
    'Pr': 140.9,
    'Nd': 144.2,
    'Pm': 145.0,
    'Sm': 150.4,
    'Eu': 151.9,
    'Gd': 157.3,
    'Tb': 158.9,
    'Dy': 162.5,
    'Ho': 164.9,
    'Er': 167.3,
    'Tm': 168.9,
    'Yb': 173.0,
    'Lu': 174.9,
    'Hf': 178.5,
    'Ta': 180.9,
    'W': 183.8,
    'Re': 186.2,
    'Os': 190.2,
    'Ir': 192.2,
    'Pt': 195.1,
    'Au': 197.0,
    'Hg': 200.6,
    'Tl': 204.4,
    'Pb': 207.2,
    'Bi': 208.9,
    'Po': 209.0,
    'At': 210.0,
    'Rn': 222.0,
    'Fr': 223.0,
    'Ra': 226.0,
    'Ac': 227.0,
    'Th': 232.0,
    'Pa': 231.0,
    'U': 238.0,
    'Np': 237.0,
    'Pu': 244.0,
    'Am': 243.0,
    'Cm': 247.0,
    'Bk': 247.0,
    'Cf': 251.0,
    'Es': 252.0,
    'Fm': 257.0,
    'Md': 258.0,
    'No': 259.0,
    'Rf': 267.0,
    'Db': 268.0,
    'Sg': 269.0,
    'Bh': 270.0,
    'Hs': 277.0,
    'Mt': 276.0,
    'Ds': 281.0,
    'Rg': 280.0,
    'Cn': 285.0,
    'Nh': 284.0,
    'Fl': 289.0,
    'Mc': 288.0,
    'Lv': 293.0,
    'Ts': 294.0,
    'Og': 294.0,
}

def calculate_molar_mass(compound):
    total_mass = 0.0
    current_element = ''
    current_count = ''

    for char in compound:
        if char.isalpha():
            if current_element:
                element_mass = elements_directory.get(current_element, 0.0)
                count = int(current_count) if current_count else 1
                total_mass += element_mass * count

            current_element = char
            current_count = ''
        elif char.isdigit():
            current_count += char

    # Handle the last element in the compound
    if current_element:
        element_mass = elements_directory.get(current_element, 0.0)
        count = int(current_count) if current_count else 1
        total_mass += element_mass * count

    return total_mass

def grams_to_moles(grams, molar_mass):
    moles = grams / molar_mass
    return moles

def moles_to_grams(moles, molar_mass):
    grams = moles * molar_mass
    return grams

def main():
    while True:
        print("\nChoose an option:")
        print("1. Find molar mass of a compound")
        print("2. Convert grams to moles")
        print("3. Convert moles to grams")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            compound_input = input("Enter a chemical compound: ")
            compound_mass = calculate_molar_mass(compound_input)
            print(f"The molar mass of {compound_input} is {compound_mass:.2f} g/mol.")
        elif choice == '2':
            grams = float(input("Enter the amount in grams: "))
            compound_input = input("Enter the chemical compound: ")
            compound_mass = calculate_molar_mass(compound_input)
            moles = grams_to_moles(grams, compound_mass)
            print(f"{grams:.2f} grams of {compound_input} is equal to {moles:.2f} moles.")
        elif choice == '3':
            moles = float(input("Enter the amount in moles: "))
            compound_input = input("Enter the chemical compound: ")
            compound_mass = calculate_molar_mass(compound_input)
            grams = moles_to_grams(moles, compound_mass)
            print(f"{moles:.2f} moles of {compound_input} is equal to {grams:.2f} grams.")
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
