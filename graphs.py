import numpy as np
import matplotlib.pyplot as plt

# Generate Shock Wave Structure Plot
x = np.linspace(-2, 2, 100)
shock_wave = np.exp(-x**2) + 0.1 * np.sin(5*x)

plt.figure(figsize=(6,4))
plt.plot(x, shock_wave, label="Shock Wave")
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.8)
plt.xlabel("Position (m)")
plt.ylabel("Pressure Coefficient")
plt.title("Shock Wave Structure")
plt.legend()
plt.grid(True)
plt.savefig("shock_structure.png")
plt.show()

# Generate Heat Flux Distribution Plot
x = np.linspace(0, 5, 100)
heat_flux = np.exp(-x) * 1000

plt.figure(figsize=(6,4))
plt.plot(x, heat_flux, label="Heat Flux", color='r')
plt.xlabel("Distance along Surface (m)")
plt.ylabel("Heat Flux (W/m²)")
plt.title("Heat Flux Distribution on Entry Vehicle")
plt.legend()
plt.grid(True)
plt.savefig("heat_flux_distribution.png")
plt.show()

# Generate Entry Trajectory Analysis Plot
altitude = np.linspace(100, 0, 100)
velocity = np.sqrt(altitude) * 200

plt.figure(figsize=(6,4))
plt.plot(velocity, altitude, label="Entry Trajectory", color='b')
plt.xlabel("Velocity (m/s)")
plt.ylabel("Altitude (km)")
plt.title("Entry Trajectory: Altitude vs. Velocity")
plt.legend()
plt.grid(True)
plt.savefig("trajectory_analysis.png")
plt.show()
