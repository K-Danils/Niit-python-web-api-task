from scipy.stats import shapiro
from statsmodels.tsa.stattools import adfuller
import scipy.stats as st
import numpy as np

def get_readings_mean(readings):
    if len(readings) == 0:
        return 0
    sum = 0
    for reading in readings:
        sum += reading[1]

    return sum / len(readings)

def get_readings_variance(readings):
    # returns sample variance by:
    # getting the mean of the data set
    # finds squared difference from the mean for each data value (xi - xm)^2
    # find the sum of squared differences
    # get variance by dividing sum of squared differences by size of data set - 1

    if len(readings) == 0:
        return 0

    # to avoid division by zero, if length of readings is 1, don't take away 1
    n = len(readings) if len(readings) == 1 else len(readings) - 1
    mean = get_readings_mean(readings)
    sum_of_squared_differences = 0

    for reading in readings:
        sum_of_squared_differences += (reading[1] - mean)**2

    return sum_of_squared_differences / n

def is_normal_distribution(readings, p_treshold):
    # returns whether data set is gaussian distribution or not, by using Shapiro-Wilk test

    # length must be at least 3, otherwise calculation is impossible
    if len(readings) < 3:
        return False

    mean = get_readings_mean(readings)
    variance = get_readings_variance(readings)
    data = np.random.normal(loc=mean, scale=variance, size=len(readings))
    stat, p = shapiro(data)

    return True if p > p_treshold else False

def get_confidence_treshold(readings, treshold):
    variation = get_readings_variance(readings)
    mean = get_readings_mean(readings)
    sample_size = len(readings)

    return st.t.interval(treshold, sample_size, loc=mean, scale=variation)

def is_stationary(readings, treshold):
    # get all the reading values
    reading_values = [reading[1] for reading in readings]

    if len(reading_values) < 3:
        return "<p>Couldn't calculate stationarity, sample size is too short, must have size of atleast: 3</p>"

    result = adfuller(reading_values)
    p_value = result[1]

    return False if p_value > treshold else True
    