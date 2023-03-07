from Classes.individual import Individual
import random

class Population:
    def __init__(self, size: int):
        self.iteration = 0
        self.size = size
        self.individual_length = 7
        self.mutation_rate = 0.1
        # Generates a random population of individuals of size size
        self.population = [Individual(random.sample(range(1, 8), 7)) for _ in range(size)]
        # self.new_population = []


    def evolve(self):
        self.iteration += 1
        # Selects the two best individuals from the population
        parents = self.select()
        # Generates new individuals by crossing over the parents
        children = self.crossover(parents)
        # Mutate the children
        for child in children:
            if random.random() < self.mutation_rate:
                child.mutate()
        
        # Replaces the two worst individuals in the population with the children
        self.population[-2:] = children
        

    def select(self):
        # Returns the two best individuals from the population
        self.population.sort(key=lambda individual: individual.calculate_fitness())
        return self.population[:2]

    def crossover(self, parents: list):
        # Creates individuals by crossing over two best individuals and repairs repeating genes
    
        # Chooses a random crossover point
        crossover_point = random.randint(1, 5)
        
        # Creates two new individuals by combining genes of the parents
        child1 = parents[0].genes[:crossover_point] + parents[1].genes[crossover_point:]
        child2 = parents[1].genes[:crossover_point] + parents[0].genes[crossover_point:]
        # Replaces repeating genes(gene repair)
        for i, gene in enumerate(child1):
            while child1.count(gene) > 1:
                index = child1.index(gene)
                child1[index] = random.randint(1, 7)
                gene = child1[index]  # update gene variable
        for i, gene in enumerate(child2):
            while child2.count(gene) > 1:
                index = child2.index(gene)
                child2[index] = random.randint(1, 7)
                gene = child2[index]  # update gene variable

        # Add the new individuals to the population
        return [Individual(child1), Individual(child2)]



    def __str__(self):
        result = "Population #" + str(self.iteration) +":\n"
        for individual in self.population:
            result += "\t" + str(individual) + "\n"
        return result