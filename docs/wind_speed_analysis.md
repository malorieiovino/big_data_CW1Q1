# Wind Speed Range Analysis for April 2007

## Data Source
- NCDC Hourly Weather Data
- Month: April 2007

## Methodology
Utilized MapReduce framework to process hourly weather data from multiple weather stations

## Daily Wind Speed Range Results

| Date       | Wind Speed Range (kt) |
|------------|----------------------:|
| 2007-04-01 | 43.0 |
| 2007-04-02 | 56.0 |
| 2007-04-03 | 40.0 |
| 2007-04-04 | 96.0 |
| 2007-04-05 | 42.0 |
| 2007-04-06 | 41.0 |
| 2007-04-07 | 43.0 |
| 2007-04-08 | 64.0 |
| 2007-04-09 | 71.0 |
| 2007-04-10 | 57.0 |
| 2007-04-11 | 50.0 |
| 2007-04-12 | 60.0 |
| 2007-04-13 | 67.0 |
| 2007-04-14 | 90.0 |
| 2007-04-15 | 73.0 |
| 2007-04-16 | 97.0 |
| 2007-04-17 | 59.0 |
| 2007-04-18 | 71.0 |
| 2007-04-19 | 65.0 |
| 2007-04-20 | 36.0 |
| 2007-04-21 | 96.0 |
| 2007-04-22 | 60.0 |
| 2007-04-23 | 81.0 |
| 2007-04-24 | 67.0 |
| 2007-04-25 | 40.0 |
| 2007-04-26 | 37.0 |
| 2007-04-27 | 38.0 |
| 2007-04-28 | 37.0 |
| 2007-04-29 | 93.0 |

## Key Observations
- Highest wind speed range: 97.0 kt (2007-04-16)
- Lowest wind speed range: 36.0 kt (2007-04-20)
- Average wind speed range: ~60.0 kt

## Technical Implementation
- Mapper: Extracted date and wind speed
- Reducer: Calculated daily wind speed range across all weather stations

## Limitations
- Analysis based on available weather station data
- Potential variations due to different station locations
