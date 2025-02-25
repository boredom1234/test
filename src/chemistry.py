def calculate_molarity_concentration(moles, volume_liters):
    if volume_liters == 0:
        raise ValueError("Volume cannot be zero to avoid division by zero.")
    return moles / volume_liters

def calculate_number_of_moles(molarity, volume_liters):
    return molarity * volume_liters

def calculate_mass_of_substance(moles, molar_mass):
    return moles * molar_mass

def calculate_percentage_yield(actual_yield, theoretical_yield):
    if theoretical_yield == 0:
        raise ValueError("Theoretical yield cannot be zero.")
    return (actual_yield / theoretical_yield) * 100

def calculate_ideal_gas_law_equation(P, V, n, R, T):
    if n == 0 or R == 0 or T == 0:
        raise ValueError("n, R, and T cannot be zero.")
    return (P * V) / (n * R * T)

# Example calculations
molarity_concentration = calculate_molarity_concentration(2, 1)
number_of_moles = calculate_number_of_moles(1, 2)
mass_of_substance = calculate_mass_of_substance(3, 18)
percentage_yield = calculate_percentage_yield(50, 100)
ideal_gas_law_result = calculate_ideal_gas_law_equation(1, 22.4, 1, 0.0821, 273)

# Output results
print(f"Molarity Concentration: {molarity_concentration}")
print(f"Number of Moles: {number_of_moles}")
print(f"Mass of Substance: {mass_of_substance}")
print(f"Percentage Yield: {percentage_yield}")
print(f"Ideal Gas Law Result: {ideal_gas_law_result}")
