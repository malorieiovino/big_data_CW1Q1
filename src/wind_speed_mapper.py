import sys

for line in sys.stdin:
    parts = line.strip().split()  # Adjust split based on dataset structure
    if len(parts) < 5:  # Skip malformed lines
        continue

    date = parts[0]  # Assuming first column is date
    wind_speed = float(parts[2])  # Assuming third column is wind speed

    print(f"{date}\t{wind_speed}")

