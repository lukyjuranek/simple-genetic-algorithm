from copy import deepcopy
from Classes.individual import Individual


def test_mutate():
    # Test mutate function
    individual1 = Individual([1, 2, 3, 4, 5, 6, 7])
    individual1_mutated = deepcopy(individual1)
    individual1_mutated.mutate()
    differences = 0
    for i, gene in enumerate(individual1.genes):
        if gene != individual1_mutated.genes[i]:
            differences += 1
    assert differences == 2, "Mutate function failed" + \
        str(individual1.genes)+str(individual1_mutated.genes)
    return True


def test_fitness():
    # Test fitness function
    individual1 = Individual([1, 4, 6, 3, 5, 2, 7])
    assert individual1.calculate_fitness() == 13, "Fitness function failed: " + \
        str(individual1.genes)+" Fitness: " + \
        str(individual1.calculate_fitness())
    assert Individual([1, 2, 3, 4, 6, 5, 7]).calculate_fitness() == 5, "Fitness function failed"
    return True