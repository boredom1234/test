def calculate_molarity_concentration(moles, volume_liters):
    """Calculate molarity (moles per liter)."""
    if volume_liters == 0:
        raise ValueError("Volume cannot be zero to avoid division by zero.")
    if moles == 0:
        raise ValueError("Moles cannot be zero. Molarity is undefined in this case.")
    return moles / volume_liters

def calculate_number_of_moles(molarity, volume_liters):
    """Calculate the number of moles from molarity and volume."""
    if molarity == 0 or volume_liters == 0:
        raise ValueError("Neither molarity nor volume can be zero.")
    return molarity * volume_liters

def calculate_mass_of_substance(moles, molar_mass):
    """Calculate mass from moles and molar mass."""
    if moles == 0 or molar_mass == 0:
        raise ValueError("Neither moles nor molar mass can be zero.")
    return moles * molar_mass

def calculate_percentage_yield(actual_yield, theoretical_yield):
    """Calculate percent yield from actual and theoretical yield."""
    if theoretical_yield == 0:
        raise ValueError("Theoretical yield cannot be zero.")
    return (actual_yield / theoretical_yield) * 100

def calculate_ideal_gas_law_equation(P, V, n, R, T):
    """
    Apply the ideal gas law: PV = nRT -> rearranged to (P * V) / (n * R * T).
    - n (number of moles), R (gas constant), and T (temperature) must not be zero.
    - If any of these are zero, the equation is undefined.
    """
    if n == 0 or R == 0 or T == 0:
        raise ValueError("n, R, and T cannot be zero.")
    return (P * V) / (n * R * T)

# Example calculations with varied scenarios
try:
    molarity_concentration = calculate_molarity_concentration(2, 1)
    number_of_moles = calculate_number_of_moles(0.5, 2)
    mass_of_substance = calculate_mass_of_substance(3, 18)
    percentage_yield = calculate_percentage_yield(45, 50)
    ideal_gas_law_result = calculate_ideal_gas_law_equation(1, 22.4, 1, 0.0821, 273)

    # Output results
    print(f"Molarity Concentration: {molarity_concentration} M")
    print(f"Number of Moles: {number_of_moles} moles")
    print(f"Mass of Substance: {mass_of_substance} g")
    print(f"Percentage Yield: {percentage_yield} %")
    print(f"Ideal Gas Law Result: {ideal_gas_law_result}")

except ValueError as e:
    print(f"Error: {e}")
