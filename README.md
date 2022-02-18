# Plate Temperature Simulator

This is a simple temperature distribution simulator that uses pygame to display a heat map that show the temperature change in real time.

The sim works by using a square 2d list, where the temperature of a single entry tends toward the average of the four entries neighboring it. The average temperature in the system remains the same, as it should, and eventually the temperature evenly disperses across the list.
