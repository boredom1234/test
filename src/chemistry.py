def calculate_molarity_concentration(moles, volume_liters):
    """Calculate molarity (moles per liter)."""
    if volume_liters == 0:
        raise ValueError("Error: Volume cannot be zero. Molarity is calculated as moles per liter, and division by zero is undefined.")
    if moles == 0:
        raise ValueError("Warning: Moles is zero. This means there is no solute in the solution, resulting in a molarity of 0 M.")
    return moles / volume_liters

def calculate_number_of_moles(molarity, volume_liters):
    """Calculate the number of moles from molarity and volume."""
    if volume_liters == 0:
        raise ValueError("Error: Volume cannot be zero. The number of moles is calculated as molarity × volume, so division by zero is undefined.")
    return molarity * volume_liters  # No error for molarity = 0, since result is correctly 0.

def calculate_mass_of_substance(moles, molar_mass):
    """Calculate mass from moles and molar mass."""
    if molar_mass == 0:
        raise ValueError("Error: Molar mass cannot be zero. Every substance has a defined molar mass greater than zero.")
    return moles * molar_mass  # If moles = 0, the result is correctly 0, no need for an error.

def calculate_percentage_yield(actual_yield, theoretical_yield):
    """Calculate percent yield from actual and theoretical yield."""
    if theoretical_yield == 0:
        raise ValueError("Error: Theoretical yield cannot be zero. Percent yield is undefined when the theoretical yield is zero.")
    return (actual_yield / theoretical_yield) * 100

def calculate_ideal_gas_law_equation(P, V, n, R, T):
    """
    Apply the ideal gas law: PV = nRT -> rearranged to (P * V) / (n * R * T).
    - n (number of moles), R (gas constant), and T (temperature) must not be zero.
    - If any of these are zero, the equation is undefined.
    """
    if n == 0:
        raise ValueError("Error: Number of moles (n) cannot be zero. The gas law equation requires a nonzero quantity of gas.")
    if R == 0:
        raise ValueError("Error: The gas constant (R) cannot be zero. R is a fundamental constant and must be provided.")
    if T == 0:
        raise ValueError("Error: Temperature (T) cannot be zero. Temperature must be in Kelvin, and absolute zero is unattainable.")
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
    print(f"Calculation Error: {e}")

# Note: Results are printed instead of stored in a data structure
# because this script is meant for quick calculations.
# In a real-world scenario, storing values in a dictionary or database
# would be a better approach for further processing.
