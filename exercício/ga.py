import random
import matplotlib.pyplot as plt

# Constants
MAX_POPULATION = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
MAX_GENERATIONS = 100 # show evaluation of how much is good
BUDGET = 10000
WORKING_TIME = 100
STORAGE_SPACE = 100
PRODUCTS = {
    'A': {'time': 1, 'value': 100, 'space': 1},
    'B': {'time': 2, 'value': 200, 'space': 2},
    'C': {'time': 3, 'value': 300, 'space': 3}
}
fitness_scores = []

def generate_individual():
    return [random.randint(0, 10) for _ in range(3)] # Each individual is represented as a list that contains the quantities of products A, B, and C to be produced.


def fitness(individual):
    total_time = sum(individual[i] * PRODUCTS[product]['time'] for i, product in enumerate(['A', 'B', 'C']))
    total_value = sum(individual[i] * PRODUCTS[product]['value'] for i, product in enumerate(['A', 'B', 'C']))
    total_space = sum(individual[i] * PRODUCTS[product]['space'] for i, product in enumerate(['A', 'B', 'C']))

    if total_time > WORKING_TIME or total_space > STORAGE_SPACE or total_value > BUDGET:
        return 0
    return total_value


def crossover(parent1, parent2):
    pivot = random.randint(1, len(parent1) - 2)
    child1 = parent1[:pivot] + parent2[pivot:]
    child2 = parent2[:pivot] + parent1[pivot:]
    return child1, child2


def mutate(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index] = random.randint(0, 10)
    return individual


# Initialization
population = [generate_individual() for _ in range(MAX_POPULATION)]

for generation in range(MAX_GENERATIONS):
    population = sorted(population, key=lambda x: fitness(x), reverse=True)
    best_fitness = fitness(population[0])
    fitness_scores.append(best_fitness)
    new_population = population[:MAX_POPULATION // 2]

    for _ in range(MAX_POPULATION // 2):
        parent1, parent2 = random.choices(population[:MAX_POPULATION // 2], k=2)
        child1, child2 = crossover(parent1, parent2)

        if random.random() < MUTATION_RATE:
            child1 = mutate(child1)
        if random.random() < MUTATION_RATE:
            child2 = mutate(child2)

        new_population.extend([child1, child2])

    population = new_population

    # Plot the dynamic fitness score
    plt.plot(range(generation + 1), fitness_scores, marker='o', color='b')
    plt.xlabel('Generation')
    plt.ylabel('Best Fitness Score')
    plt.title('Genetic Algorithm Progress')
    plt.pause(0.05)
    if generation < MAX_GENERATIONS - 1:
        plt.clf()

# Print the best solution
best_solution = max(population, key=lambda x: fitness(x))
print("Best solution: ", best_solution)
print("Maximized Profit: ", fitness(best_solution))

# Final plot
plt.show()