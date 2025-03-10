#!/usr/bin/env python3
import sys

current_date = None
humidity_values = []

for line in sys.stdin:
    try:
        # Split the input line
        date, humidity = line.strip().split('\t')
        humidity = float(humidity)
    except ValueError:
        continue

    # If we've moved to a new date, output the previous date's results
    if current_date and current_date != date:
        # Calculate and print minimum humidity for the previous date
        min_humidity = min(humidity_values)
        print(f"{current_date}\t{min_humidity}")
        
        # Reset for the new date
        humidity_values = []

    # Update current date and humidity values
    current_date = date
    humidity_values.append(humidity)

# Output the last day's result
if current_date:
    min_humidity = min(humidity_values)
    print(f"{current_date}\t{min_humidity}")
