import sys

current_date = None
min_wind = float("inf")
max_wind = float("-inf")

for line in sys.stdin:
    date, wind_speed = line.strip().split("\t")
    wind_speed = float(wind_speed)

    if date != current_date:
        if current_date is not None:
            print(f"{current_date}\t{max_wind - min_wind}")
        current_date = date
        min_wind, max_wind = wind_speed, wind_speed
    else:
        min_wind = min(min_wind, wind_speed)
        max_wind = max(max_wind, wind_speed)

# Print last entry
if current_date:
    print(f"{current_date}\t{max_wind - min_wind}")

