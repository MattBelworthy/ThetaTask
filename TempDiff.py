""" This project finds the day with the minimum difference between MxT (maximum temperature) and MnT
(minimum temperature) in a given month.
Author: Matt Belworthy Lewthwaite
Last modified: 19 December 2018
"""

import os, math

def differenceCalculator(line):
    """Calculates the daily difference for a given line"""

    dailyMxt = float(line.split()[1].replace('*', '')) #stripping the daily minimum temperature out
    dailyMnt = float(line.split()[2].replace('*', '')) #stripping the daily maximum temperature out
    dailyDiff = dailyMxt - dailyMnt

    return dailyDiff

def differenceComparer(file):
    currentMin = (0, float('inf'))  # currentMin[0] = day number, currentMin[1] = difference

    for lineNumber, line in enumerate(file):
        if lineNumber > 1:  # ignoring the first two lines in the file

            dailyDiff = differenceCalculator(line)

            if dailyDiff < currentMin[1]:  # if this days difference is more than the current max difference
                currentMin = (line.split()[0], dailyDiff)

    return currentMin[0]


def main():
    """ The main function takes a file as an input (i.e. weather.dat) and checks whether the file can be
    found. """
    filename = raw_input("Please enter filename: ")

    while not os.path.isfile(filename):
        print(filename + " not found...")
        filename = raw_input("Please enter filename: ")


    with open(filename) as file: #Calling calculator for the found file
        minDay = differenceComparer(file)

    print("The day with the lowest difference: " + minDay)

main()