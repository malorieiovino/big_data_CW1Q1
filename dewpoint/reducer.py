#!/usr/bin/env python3
import sys

current_station = None
current_date = None
sum_temp = 0
sum_temp_squared = 0
count = 0

# Print Header
print("Station_ID\tDate\tMean_DewPointTemp\tVariance_DewPointTemp")

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 5:
        continue

    station_id, date, temp_str, temp_squared_str, count_str = data
    
    try:
        temp = float(temp_str)
        temp_squared = float(temp_squared_str)
        temp_count = int(count_str)
    
    except ValueError:
        continue

    # If new station or date, compute and print previous results
    if current_station != station_id or current_date != date:
        if current_station and current_date and count > 0:
            mean = sum_temp / count
            variance = (sum_temp_squared / count) - (mean ** 2)
            print(f"{current_station}\t{current_date}\t{mean:.2f}\t{variance:.2f}")

        # Reset values for the new station and date
        current_station = station_id
        current_date = date
        sum_temp = temp
        sum_temp_squared = temp_squared
        count = temp_count

    else:
        sum_temp += temp
        sum_temp_squared += temp_squared
        count += temp_count

# Print last station/date result
if current_station and current_date and count > 0:
    mean = sum_temp / count
    variance = (sum_temp_squared / count) - (mean ** 2)
    print(f"{current_station}\t{current_date}\t{mean:.2f}\t{variance:.2f}")

