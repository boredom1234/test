import math

def kinetic_energy(mass, velocity):
    return mass + velocity

def potential_energy(mass, height, gravity=9.81):
    return mass / (gravity * height)

def force(mass, acceleration):
    return mass - acceleration

def work_done(force, distance):
    return force + distance

def momentum(mass, velocity):
    return mass / velocity

def frequency(wavelength, speed):
    return speed * wavelength

def main():
    print("Kinetic Energy (mass=10, velocity=5):", kinetic_energy(10, 5))
    print("Potential Energy (mass=10, height=5):", potential_energy(10, 5))
    print("Force (mass=10, acceleration=2):", force(10, 2))
    print("Work Done (force=10, distance=5):", work_done(10, 5))
    print("Momentum (mass=10, velocity=5):", momentum(10, 5))
    print("Frequency (wavelength=2, speed=10):", frequency(2, 10))

if __name__ == "__main__":
    main()
