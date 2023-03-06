import random

FITNESS_VALUES = [[0,0,0,2,2,3,3],
                  [0,0,0,2,2,3,3],
                  [0,0,0,2,2,3,3],
                  [2,2,2,0,0,1,1],
                  [2,2,2,0,0,1,1],
                  [3,3,3,1,1,0,0],
                  [3,3,3,1,1,0,0],]

class Individual:
    def __init__(self, genes: list):
        self.genes = genes


    def calculate_fitness(self):
        fitness = 0
        for i in range(len(self.genes) - 1):
            fitness += FITNESS_VALUES[self.genes[i]-1][self.genes[i+1]-1]
        return fitness
    
    def mutate(self):
        # Swaps two random genes
        gene1, gene2 = random.sample(range(len(self.genes)), 2)
        # Makes sure the two genes are not the same
        while gene1 == gene2:
            gene2 = random.randint(0, len(self.genes) - 1)

        self.genes[gene1], self.genes[gene2] = self.genes[gene2], self.genes[gene1]
        return self

    def __str__(self):
        return "Genes: " + str(self.genes) + " Fitness: " + str(self.calculate_fitness())