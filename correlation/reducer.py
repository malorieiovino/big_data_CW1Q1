#!/usr/bin/env python3

import sys
import math

# Initialize variables for correlation calculation
humidity_sum = 0.0
wind_speed_sum = 0.0
temperature_sum = 0.0

humidity_squared_sum = 0.0
wind_speed_squared_sum = 0.0
temperature_squared_sum = 0.0

humidity_wind_prod_sum = 0.0
humidity_temp_prod_sum = 0.0
wind_temp_prod_sum = 0.0

count = 0

# Read input from mapper
for line in sys.stdin:
    # Parse the input
    line = line.strip()
    key, value = line.split('\t', 1)
    
    # Extract the three variables
    humidity, wind_speed, temperature = map(float, value.split(','))
    
    # Update sums
    humidity_sum += humidity
    wind_speed_sum += wind_speed
    temperature_sum += temperature
    
    humidity_squared_sum += humidity * humidity
    wind_speed_squared_sum += wind_speed * wind_speed
    temperature_squared_sum += temperature * temperature
    
    humidity_wind_prod_sum += humidity * wind_speed
    humidity_temp_prod_sum += humidity * temperature
    wind_temp_prod_sum += wind_speed * temperature
    
    count += 1

# Calculate correlation coefficients using the Pearson correlation formula
if count > 0:
    # Correlation between humidity and wind speed
    numerator_hw = (humidity_wind_prod_sum - (humidity_sum * wind_speed_sum) / count)
    denominator_hw = math.sqrt((humidity_squared_sum - (humidity_sum * humidity_sum) / count) * 
                              (wind_speed_squared_sum - (wind_speed_sum * wind_speed_sum) / count))
    corr_humidity_wind = numerator_hw / denominator_hw if denominator_hw != 0 else 0

    # Correlation between humidity and temperature
    numerator_ht = (humidity_temp_prod_sum - (humidity_sum * temperature_sum) / count)
    denominator_ht = math.sqrt((humidity_squared_sum - (humidity_sum * humidity_sum) / count) * 
                              (temperature_squared_sum - (temperature_sum * temperature_sum) / count))
    corr_humidity_temp = numerator_ht / denominator_ht if denominator_ht != 0 else 0

    # Correlation between wind speed and temperature
    numerator_wt = (wind_temp_prod_sum - (wind_speed_sum * temperature_sum) / count)
    denominator_wt = math.sqrt((wind_speed_squared_sum - (wind_speed_sum * wind_speed_sum) / count) * 
                              (temperature_squared_sum - (temperature_sum * temperature_sum) / count))
    corr_wind_temp = numerator_wt / denominator_wt if denominator_wt != 0 else 0

    # Output the correlation matrix
    print("Correlation Matrix:")
    print("Variable\tRelative Humidity\tWind Speed\tDry Bulb Temp")
    print(f"Relative Humidity\t1.0\t{corr_humidity_wind:.4f}\t{corr_humidity_temp:.4f}")
    print(f"Wind Speed\t{corr_humidity_wind:.4f}\t1.0\t{corr_wind_temp:.4f}")
    print(f"Dry Bulb Temp\t{corr_humidity_temp:.4f}\t{corr_wind_temp:.4f}\t1.0")
else:
    print("No valid data found for correlation calculation")
