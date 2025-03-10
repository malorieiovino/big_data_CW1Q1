#!/usr/bin/env python3
import sys
import signal

# Ignore SIGPIPE to avoid BrokenPipeError
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

for line in sys.stdin:
    data = line.strip().split(",")

    if len(data) < 14:  # Adjust if needed
        continue

    try:
        station_id = data[0].strip()
        raw_date = data[1].strip()
        formatted_date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
        
        # Extract Dew Point Temperature (CHECK THE RIGHT COLUMN NUMBER)
        dew_point_temp = float(data[5].strip())

        # Emit (station, date) → (dew_point_temp, dew_point_temp^2, 1)
        print(f"{station_id}\t{formatted_date}\t{dew_point_temp}\t{dew_point_temp**2}\t1")
    
    except ValueError:
        continue  # Skip invalid values

