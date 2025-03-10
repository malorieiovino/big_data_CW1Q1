# Weather Data Analysis using MapReduce

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)](https://www.python.org/)
[![Hadoop](https://img.shields.io/badge/Hadoop-MapReduce-yellow.svg?logo=apache)](https://hadoop.apache.org/)
[![Degree](https://img.shields.io/badge/MSc-Computational%20Linguistics-blueviolet.svg)](https://www.gold.ac.uk/)
[![University](https://img.shields.io/badge/University-Goldsmiths%20UoL-black.svg)](https://www.gold.ac.uk/)
[![Course](https://img.shields.io/badge/Course-Big%20Data%20Analysis-orange.svg)](https://www.gold.ac.uk/computing/)
[![Data](https://img.shields.io/badge/Data-NCDC%20Weather-lightgrey.svg)](https://www.ncdc.noaa.gov/)

## Overview

## Overview
This project implements MapReduce computational model on Hadoop cluster to analyze NCDC weather data from 2007. The analysis focuses on April 2007 hourly weather records and extracts various descriptive statistics across different weather stations.

## Dataset
- **Source**: NCDC hourly weather data (April 2007)
- **Format**: CSV-like data with multiple weather measurements
- **Sample Path**: `/user/miovi001/Q1/200704hourly.txt`
- **Key Measurements**: 
  - Wind Speed
  - Relative Humidity
  - Dew Point Temperature
  - Dry Bulb Temperature

## Analysis Tasks

This project implements four primary analyses as specified in the assignment:

### 1. Wind Speed Analysis
Calculates the daily difference between maximum and minimum wind speed across all weather stations.

- **Mapper**: Extracts date and wind speed from each record
- **Reducer**: Computes max and min values per day, then calculates the difference
- **Files**: 
  - `wind_speed/mapper.py`
  - `wind_speed/reducer.py`
  - `wind_speed/results.txt`
  - `wind_speed/analysis.md`

### 2. Humidity Analysis
Identifies the daily minimum relative humidity value across all weather stations.

- **Mapper**: Extracts date and relative humidity from each record
- **Reducer**: Determines the minimum humidity value for each day
- **Files**:
  - `humidity/mapper.py`
  - `humidity/reducer.py`
  - `humidity/results.txt`
  - `humidity/analysis.md`

### 3. Dew Point Analysis
Calculates the daily mean and variance of dew point temperature across all weather stations.

- **Mapper**: Extracts date and dew point temperature from each record
- **Reducer**: Computes mean and variance using the formula:
### variance = (1/N)*(sum(x_i^2)-N*mean^2
- **Files**:
- `dewpoint/mapper.py`
- `dewpoint/reducer.py`
- `dewpoint/results.txt`
- `dewpoint/analysis.md`

### 4. Correlation Matrix
Constructs a monthly correlation matrix between Relative Humidity, Wind Speed, and Dry Bulb Temperature.

- **Mapper**: Extracts all three measurements from each record
- **Reducer**: Computes Pearson correlation coefficients using the formula:
### correlation = (sum(xy)-sum(x)sum(y)/N)/sqrt[(sum(x^2)-(sum(x)^2)/N)*(sum(y^2)-(sum(y)^2/N)]
- **Files**:
- `correlation/mapper.py`
- `correlation/reducer.py`
- `correlation/results.txt`
- `correlation/analysis.md`

## Implementation Details

### Data Processing Challenges
- The dataset contains records from multiple weather stations with varying time intervals
- Some records might have missing or invalid values for certain measurements
- The data format requires careful parsing to extract the correct fields

### MapReduce Methodology
Each analysis task follows the MapReduce paradigm:

1. **Map Phase**:
 - Extract relevant data points from each record
 - Emit key-value pairs where the key is typically the date
 - Filter out records with missing or invalid data

2. **Reduce Phase**:
 - Aggregate values by key (usually date)
 - Perform statistical calculations (min, max, mean, variance, correlation)
 - Generate the final output

### Running the Code
All MapReduce jobs were executed on the university's Hadoop cluster using the following pattern:

```bash
# Generic format for running a MapReduce job
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/miovi001/Q1/200704hourly.txt \
-output /user/miovi001/Q1/[analysis_name]_output \
-mapper "python3 [analysis_name]_mapper.py" \
-reducer "python3 [analysis_name]_reducer.py" \
-file [analysis_name]_mapper.py \
-file [analysis_name]_reducer.py \
-numReduceTasks 1
```

## Key Results

### 1. Wind Speed Analysis

| Date | Max Wind Speed (kt) | Min Wind Speed (kt) | Daily Range (kt) |
|------|---------------------|---------------------|------------------|
| 2007-04-01 | 13.0 | 4.0 | 9.0 |
| 2007-04-02 | 15.0 | 3.0 | 12.0 |
| 2007-04-03 | 14.0 | 3.0 | 11.0 |
| 2007-04-04 | 17.0 | 4.0 | 13.0 |
| 2007-04-05 | 16.0 | 2.0 | 14.0 |
| ... | ... | ... | ... |
| 2007-04-29 | 12.0 | 3.0 | 9.0 |
| 2007-04-30 | 13.0 | 4.0 | 9.0 |

**Key Findings:**
- Highest daily wind speed range: 16.0 kt (April 12th)
- Lowest daily wind speed range: 7.0 kt (April 22nd)
- Average daily wind speed range: 11.2 kt
- Days with ranges exceeding 14.0 kt: 5 days (16.7% of the month)

### 2. Humidity Analysis

| Date | Minimum Relative Humidity (%) |
|------|------------------------------|
| 2007-04-01 | 4.0 |
| 2007-04-02 | 5.0 |
| 2007-04-03 | 4.0 |
| 2007-04-04 | 3.0 |
| 2007-04-05 | 2.0 |
| 2007-04-06 | 4.0 |
| 2007-04-07 | 6.0 |
| 2007-04-08 | 2.0 |
| ... | ... |
| 2007-04-29 | 4.0 |
| 2007-04-30 | 3.0 |

**Key Findings:**
- Lowest minimum relative humidity: 2.0% (on 2007-04-05, 2007-04-08, 2007-04-16, 2007-04-20, 2007-04-21)
- Highest minimum relative humidity: 6.0% (on 2007-04-07, 2007-04-11, 2007-04-15, 2007-04-23, 2007-04-25)
- Average minimum relative humidity: ~4.0%
- Frequency of extremely low humidity (≤ 3.0%): 10 days (33.3% of the month)

### 3. Dew Point Analysis

| Date | Mean Dew Point (°C) | Variance |
|------|---------------------|----------|
| 2007-04-01 | 23.4 | 5.21 |
| 2007-04-02 | 24.6 | 4.89 |
| 2007-04-03 | 24.1 | 6.32 |
| 2007-04-04 | 22.8 | 5.76 |
| ... | ... | ... |
| 2007-04-29 | 25.2 | 4.98 |
| 2007-04-30 | 24.7 | 5.34 |

**Key Findings:**
- Highest mean dew point: 28.3°C (April 17th)
- Lowest mean dew point: 21.5°C (April 9th)
- Average variance: 5.47
- Days with high dew point variance (> 7.0): 4 days (indicating greater temperature fluctuations)
- Overall trend shows relatively stable dew point conditions throughout the month

### 4. Correlation Matrix

| Variable | Relative Humidity | Wind Speed | Dry Bulb Temp |
|----------|-------------------|------------|---------------|
| Relative Humidity | 1.0 | -0.1336 | -0.2235 |
| Wind Speed | -0.1336 | 1.0 | 0.0195 |
| Dry Bulb Temp | -0.2235 | 0.0195 | 1.0 |

**Key Findings:**
- **Relative Humidity and Wind Speed**: Weak negative correlation (-0.1336)
  - Suggests higher wind speeds slightly correlate with lower humidity levels
  - Meteorologically consistent with the expectation that wind can reduce localized humidity
  
- **Relative Humidity and Dry Bulb Temperature**: Moderate negative correlation (-0.2235)
  - Confirms that as temperature rises, relative humidity tends to decrease
  - This inverse relationship aligns with fundamental atmospheric physics
  
- **Wind Speed and Dry Bulb Temperature**: Near-zero correlation (0.0195)
  - Indicates these variables are largely independent of each other
  - Suggests that in this dataset, temperature has minimal influence on wind patterns
