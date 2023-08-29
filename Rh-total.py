import matplotlib.pyplot as plt
import numpy as np

# Temperature and dew point values
temperature = [19.4, 20.5, 20.5, 19.4, 18.2, 22.8]
dew_point = [4, 3, 2, -1, 18, 8]

# Calculate relative humidity for each temperature-dew point pair
calculated_relative_humidity = []
for T, TD in zip(temperature, dew_point):
    RH = 100 * (np.exp(17.625 * TD / (243.04 + TD)) / np.exp(17.625 * T / (243.04 + T)))
    calculated_relative_humidity.append(RH)

# Measured relative humidity values
measured_relative_humidity = [35.5, 30.4, 30.4, 25, 85, 65]  # Add the measured RH for M6

# Print the calculated relative humidity with references
for i, RH in enumerate(calculated_relative_humidity):
    print("Calculated Relative Humidity for M{}: {:.2f}%".format(i+1, RH))

# Plotting
plt.scatter(temperature, dew_point, c=calculated_relative_humidity, cmap='viridis', alpha=0.8, label='Calculated')
plt.scatter(temperature, dew_point, c=measured_relative_humidity, cmap='viridis', marker='x', s=100, linewidths=1.5, label='Measured')

# Custom triangle marker for RPC mixture
RPC_Temperature = 22.8
RPC_Dew_point = 8
RPC_relative_humidity = 100 * (np.exp(17.625 * RPC_Dew_point / (243.04 + RPC_Dew_point)) / np.exp(17.625 * RPC_Temperature / (243.04 + RPC_Temperature)))

triangle_marker = '^'
triangle_size = 100
triangle_color = plt.cm.viridis(RPC_relative_humidity / 100)  # Map the color based on the relative humidity value

plt.scatter(RPC_Temperature, RPC_Dew_point, c=triangle_color, marker=triangle_marker, s=triangle_size, linewidths=1.5, label='RPC mixture')
plt.annotate("RPC mixture", (RPC_Temperature, RPC_Dew_point), textcoords="offset points", xytext=(0, 5), ha='center', va='bottom', fontsize=8)

plt.colorbar(label='Relative Humidity (%)')

# Add references as annotations to the data points with adjusted positions
offsets = [(5, 5), (-15, -10), (-15, -10), (5, 5), (5, 5), (0, -10), (-15, -10)]  # Adjust the offsets as needed for proper positioning
for i, (T, TD) in enumerate(zip(temperature, dew_point)):
    plt.annotate("M{}".format(i+1), (T, TD), textcoords="offset points", xytext=offsets[i], ha='center', va='center', fontsize=8)

plt.xlabel('Temperature (°C)')
plt.ylabel('Dew Point (°C)')
plt.title('Relative Humidity at Different Temperatures and Dew Points')

plt.legend()
plt.show()
