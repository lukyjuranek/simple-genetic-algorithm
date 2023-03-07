#!/usr/bin/env python3
from Classes.individual import Individual

jobs = input("Enter the 7 job numbers separated by a space: ").split()

# Converts the input to integers
jobs = [int(j) for j in jobs]

individual = Individual(jobs)
print("Fitness score:", individual.calculate_fitness())
