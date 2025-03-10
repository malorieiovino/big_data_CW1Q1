# Correlation Matrix Analysis

## Results

The correlation matrix shows the relationships between three key weather variables: Relative Humidity, Wind Speed, and Dry Bulb Temperature.

| Variable | Relative Humidity | Wind Speed | Dry Bulb Temp |
|----------|-------------------|------------|---------------|
| Relative Humidity | 1.0 | -0.1336 | -0.2235 |
| Wind Speed | -0.1336 | 1.0 | 0.0195 |
| Dry Bulb Temp | -0.2235 | 0.0195 | 1.0 |

## Key Observations:

- **Relative Humidity and Wind Speed**: Weak negative correlation (-0.1336), suggesting higher wind speeds slightly correlate with lower humidity levels.
- **Relative Humidity and Dry Bulb Temperature**: Moderate negative correlation (-0.2235), confirming that as temperature rises, relative humidity tends to decrease.
- **Wind Speed and Dry Bulb Temperature**: Near-zero correlation (0.0195), indicating these variables are largely independent of each other.

## Methodology:

- Calculated correlation coefficients using Pearson's correlation formula
- Used MapReduce framework to process hourly weather data from April 2007
- Implemented single-pass data collection to gather all necessary statistics
- Formula used: 
  Pearson Correlation = ∑xy - (∑x∑y/N) / √[(∑x² - (∑x)²/N)(∑y² - (∑y)²/N)]
