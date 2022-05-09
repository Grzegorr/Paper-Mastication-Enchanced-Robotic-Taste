import statistics
import numpy

mass_egg = [66.4, 66.3, 69.1, 68.2, 71.4, 69.3, 68.2, 71.6, 69.4, 66.3, 63.1, 67.4]
height_egg = [58.3, 57.3, 57.4, 59.1, 59, 58.2, 57.2, 59.7, 57.2, 60.2, 58.3, 57.4]
diameter_egg = [45.2, 44.2, 45.2, 45.2, 46.9, 46.1, 46.6, 45.9, 45.6, 45.8, 45.3, 45.3]

mass_tomato = [99.7, 123.7, 69.9, 86.3, 55.1, 65.7, 71.2, 80.1, 77.6, 72.0, 101.6]
height_tomato = [43.9, 45.8, 52.3, 47.1, 49.0, 48.5, 52.7, 49.3, 40.4, 44.4, 52.9]
diameter_tomato = [53.2, 51.6, 48.2, 57.2, 60.1, 51.6, 53.7, 57.2, 52.7, 51.4, 50.6]

print("Egg")
print(statistics.mean(mass_egg))
print(statistics.stdev(mass_egg))
print(statistics.mean(height_egg))
print(statistics.stdev(height_egg))
print(statistics.mean(diameter_egg))
print(statistics.stdev(diameter_egg))


print()
print("Tomato")
print(statistics.mean(mass_tomato))
print(statistics.stdev(mass_tomato))
print(statistics.mean(height_tomato))
print(statistics.stdev(height_tomato))
print(statistics.mean(diameter_tomato))
print(statistics.stdev(diameter_tomato))