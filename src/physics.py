def kinetic_energy(mass, velocity):
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative.")
    return 0.5 * mass * velocity ** 2

def potential_energy(mass, height, gravity=9.81):
    if mass < 0 or height < 0 or gravity <= 0:
        raise ValueError("Mass, height, and gravity must be non-negative.")
    return mass * gravity * height

def force(mass, acceleration):
    if mass < 0 or acceleration < 0:
        raise ValueError("Mass and acceleration must be non-negative.")
    return mass * acceleration

def work_done(force, distance):
    if force < 0 or distance < 0:
        raise ValueError("Force and distance must be non-negative.")
    return force * distance

def momentum(mass, velocity):
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative.")
    return mass * velocity

def frequency(wavelength, speed):
    if wavelength <= 0 or speed < 0:
        raise ValueError("Wavelength must be positive and speed must be non-negative.")
    return speed / wavelength

def main():
    try:
        print("Kinetic Energy (mass=10, velocity=5):", kinetic_energy(10, 5))
        print("Potential Energy (mass=10, height=5):", potential_energy(10, 5))
        print("Force (mass=10, acceleration=2):", force(10, 2))
        print("Work Done (force=10, distance=5):", work_done(10, 5))
        print("Momentum (mass=10, velocity=5):", momentum(10, 5))
        print("Frequency (wavelength=2, speed=10):", frequency(2, 10))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
