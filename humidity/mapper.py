#!/usr/bin/env python3
import sys
import signal

# Ignore SIGPIPE to avoid BrokenPipeError
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Write debug logs to a file
debug_log = open("humidity_mapper_debug.log", "w")

for line in sys.stdin:
    # Skip header or invalid lines
    if line.startswith('Wban') or len(line.strip()) == 0:
        continue
    
    data = line.strip().split(',')
    
    # Check for enough columns
    if len(data) < 14:
        debug_log.write(f"Not enough columns: {line}\n")
        continue
    
    try:
        # Extract date (second column)
        raw_date = data[1].strip()
        formatted_date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
        
        # Extract relative humidity (column 9, index 8)
        # Assumes the relative humidity is in the 9th column
        humidity = float(data[11].strip())
        
        # Emit key-value pair
        print(f"{formatted_date}\t{humidity}")
    
    except (ValueError, IndexError) as e:
        # Log invalid conversions
        debug_log.write(f"ValueError: {e} in line: {line}")
        continue

debug_log.close()
