# Simple genetic algorithm to find the best solution to and order of operations
from Classes.individual import Individual
from Classes.population import Population
from Classes.tests import test_mutate, test_fitness

GENERATIONS = 500
POP_SIZE = 6

def main():
    if test_mutate() and test_fitness():
        print("All tests passed")
    else:
        print("Tests failed")

    population = Population(POP_SIZE) # Generates a random population of individuals
    print(population)
    # Evolves the population 
    for _ in range(GENERATIONS):
        population.evolve()
        # Prints the population every 10% of the generations
        if population.iteration % (GENERATIONS/10) == 0:
            print(population)


    print(population)


if __name__ == "__main__":
    main()
