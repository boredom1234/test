import logging

# Set up logging configuration
logging.basicConfig(level=logging.ERROR)

def kinetic_energy(mass, speed):
    if mass < 0 or speed < 0:
        raise ValueError("Mass and speed must be non-negative.")
    return 0.5 * mass * speed ** 2

def potential_energy(mass, height, gravity=9.81):
    if mass < 0 or height < 0 or gravity <= 0:
        raise ValueError("Mass, height, and gravity must be non-negative.")
    return mass * gravity * height

def force(mass, acceleration):
    if mass < 0 or acceleration < 0:
        raise ValueError("Mass and acceleration must be non-negative.")
    return mass * acceleration

def work_done(applied_force, distance):
    if applied_force < 0 or distance < 0:
        raise ValueError("Applied force and distance must be non-negative.")
    return applied_force * distance

def momentum(mass, speed):
    if mass < 0 or speed < 0:
        raise ValueError("Mass and speed must be non-negative.")
    return mass * speed

def frequency(wavelength, speed):
    if wavelength <= 0 or speed < 0:
        raise ValueError("Wavelength must be positive and speed must be non-negative.")
    return speed / wavelength

def main():
    test_cases = [
        (10, 5),  # mass, speed for kinetic energy
        (10, 5),  # mass, height for potential energy
        (10, 2),  # mass, acceleration for force
        (10, 5),  # applied force, distance for work done
        (10, 5),  # mass, speed for momentum
        (2, 10)   # wavelength, speed for frequency
    ]

    try:
        print("Kinetic Energy (mass=10, speed=5):", kinetic_energy(*test_cases[0]))
        print("Potential Energy (mass=10, height=5):", potential_energy(*test_cases[1], gravity=9.81))
        print("Force (mass=10, acceleration=2):", force(*test_cases[2]))
        print("Work Done (applied force=10, distance=5):", work_done(*test_cases[3]))
        print("Momentum (mass=10, speed=5):", momentum(*test_cases[4]))
        print("Frequency (wavelength=2, speed=10):", frequency(*test_cases[5]))
    except ValueError as e:
        logging.error("Error: %s", e)

if __name__ == "__main__":
    main()
