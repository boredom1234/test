import logging

GRAVITY = 9.81

def setup_logging():
    logging.basicConfig(level=logging.ERROR)

def kinetic_energy(mass, velocity):
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative.")
    return 0.5 * mass * velocity ** 2

def potential_energy(mass, height, gravity=GRAVITY):
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

def momentum(mass, velocity):
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative.")
    return mass * velocity

def frequency(wavelength, speed):
    if wavelength <= 0 or speed < 0:
        raise ValueError("Wavelength must be positive and speed must be non-negative.")
    return speed / wavelength

def main():
    test_cases = [
        {"mass": 10, "velocity": 5},  # Kinetic Energy
        {"mass": 10, "height": 5},     # Potential Energy
        {"mass": 10, "acceleration": 2},  # Force
        {"applied_force": 10, "distance": 5},  # Work Done
        {"mass": 10, "velocity": 5},   # Momentum
        {"wavelength": 2, "speed": 10}  # Frequency
    ]

    try:
        print("Kinetic Energy (mass=10, velocity=5):", kinetic_energy(test_cases[0]["mass"], test_cases[0]["velocity"]))
        print("Potential Energy (mass=10, height=5):", potential_energy(test_cases[1]["mass"], test_cases[1]["height"]))
        print("Force (mass=10, acceleration=2):", force(test_cases[2]["mass"], test_cases[2]["acceleration"]))
        print("Work Done (applied force=10, distance=5):", work_done(test_cases[3]["applied_force"], test_cases[3]["distance"]))
        print("Momentum (mass=10, velocity=5):", momentum(test_cases[4]["mass"], test_cases[4]["velocity"]))
        print("Frequency (wavelength=2, speed=10):", frequency(test_cases[5]["wavelength"], test_cases[5]["speed"]))
    except ValueError as e:
        logging.error("ValueError: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

if __name__ == "__main__":
    setup_logging()
    main()
