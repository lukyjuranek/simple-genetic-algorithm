# Simple genetic algorithm to find the best solution to and order of operations
from Classes.individual import Individual
from Classes.population import Population
from Classes.tests import test_mutate, test_fitness

GENERATIONS = 1000
POP_SIZE = 6

def main():
    # Tests if the mutate and fitness functions work as intended
    if test_mutate() and test_fitness():
        print("All tests passed")
    else:
        print("Tests failed")

    # Generates a random population of individuals
    population = Population(POP_SIZE)
    print(population)
    # Evolves the population 
    for _ in range(GENERATIONS):
        population.evolve()
        # Prints the population every 10% of the generations
        if population.iteration % (GENERATIONS/10) == 0 and population.iteration != GENERATIONS:
            print(population)

    print("Final population:")
    print(population)
    # Print Generation size
    print("Generation size:", POP_SIZE)
    # Prints number of generations
    print("Generations:", GENERATIONS)


if __name__ == "__main__":
    main()
