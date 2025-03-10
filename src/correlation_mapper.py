#!/usr/bin/env python3

import sys
import csv

# Based on the sample data, these are the correct column positions:
# Format is complex with mixed comma and space delimiters
# Each line looks like: 03011,20070401,0050,AO2 ,-,SCT055             ,10SM  ,-,32,23,28,69 ,4  ,130,-,0 ,30,13...

for line in sys.stdin:
    try:
        # Skip header line
        line = line.strip()
        if not line or "Wban Number" in line:
            continue
            
        # First split by comma for the first few fields
        parts = line.split(',', 4)  # Split only the first 4 commas
        
        if len(parts) < 5:
            continue
            
        # The rest of the line has mixed delimiters, so we'll parse carefully
        rest_of_line = parts[4]
        fields = rest_of_line.split(',')
        
        # Join all parts back to get a consistent array
        all_fields = parts[:4] + fields
        
        # Extract data with careful parsing - find values by counting from split positions
        # Now we need to split by spaces and handle multiple spaces
        field_values = []
        for field in all_fields:
            field_values.extend([f for f in field.split() if f])
        
        # Based on the sample, extract the correct positions
        # Dry Bulb Temp is at position 8 after all splitting
        # Relative Humidity is at position 11 
        # Wind Speed is at position 12
        
        try:
            dry_bulb_temp = float(field_values[8])  # Adjusting for your data
            rel_humidity = float(field_values[11])  # Adjusting for your data
            wind_speed = float(field_values[12])    # Adjusting for your data
            
            # Only emit valid records (non-missing values)
            if all([dry_bulb_temp, rel_humidity, wind_speed]):  # Check none are zero
                # Output for correlation calculation
                print(f"month\t{rel_humidity},{wind_speed},{dry_bulb_temp}")
                
        except (ValueError, IndexError) as e:
            # Skip records with missing or invalid values
            continue
            
    except Exception as e:
        # Skip any problematic lines
        continue
