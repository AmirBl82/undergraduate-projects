import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
import random

def tournament_selection(population, fitness_scores, k=3):
    selected_parent_indices = []
    for _ in range(2):
        tournament_indices = np.random.choice(len(population), size=k, replace=False)
        best_idx_local = tournament_indices[np.argmax(fitness_scores[tournament_indices])]
        selected_parent_indices.append(best_idx_local)
    return population[selected_parent_indices[0]], population[selected_parent_indices[1]]

class GeneticAlgorithm:
    def __init__(self, X, y, population_size=30, num_generations=10, mutation_rate=0.2, elitism=True, n_splits=3, tournsize=3, random_state=42):
        self.X = X
        self.y = y
        self.num_features = X.shape[1]
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.elitism = elitism
        self.n_splits = n_splits
        self.tournsize = tournsize
        self.random_state = random_state

        np.random.seed(self.random_state)
        random.seed(self.random_state)
        self.population = np.random.randint(2, size=(self.population_size, self.num_features))
        self.cv = StratifiedKFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)

    def fitness_function(self, chromosome):
        selected_features = np.where(chromosome == 1)[0]
        if len(selected_features) == 0:
            return 0.0
        accuracies = []
        for train_idx, test_idx in self.cv.split(self.X, self.y):
            X_train, X_test = self.X[train_idx, :], self.X[test_idx, :]
            y_train, y_test = self.y[train_idx], self.y[test_idx]
            X_train_sel = X_train[:, selected_features]
            X_test_sel = X_test[:, selected_features]
            model = RandomForestClassifier(random_state=self.random_state)
            model.fit(X_train_sel, y_train)
            y_pred = model.predict(X_test_sel)
            accuracies.append(accuracy_score(y_test, y_pred))
        return np.mean(accuracies)

    def select_parents(self, fitness_scores):
        return tournament_selection(self.population, fitness_scores, k=self.tournsize)

    def crossover(self, parent1, parent2):
        if self.num_features < 2:
            return parent1.copy(), parent2.copy()
        points = np.sort(np.random.choice(range(1, self.num_features), size=2, replace=False))
        p1, p2 = points[0], points[1]
        child1, child2 = parent1.copy(), parent2.copy()
        child1[p1:p2], child2[p1:p2] = parent2[p1:p2].copy(), parent1[p1:p2].copy()
        return child1, child2

    def mutate(self, chromosome):
        for i in range(len(chromosome)):
            if np.random.rand() < self.mutation_rate:
                chromosome[i] = 1 - chromosome[i]
        return chromosome

    def run(self):
        best_fitness_overall = 0.0
        best_chromosome_overall = None
        for generation in range(self.num_generations):
            fitness_scores = np.array([self.fitness_function(ch) for ch in self.population])
            new_population = []
            if self.elitism:
                best_idx = np.argmax(fitness_scores)
                best_individual = self.population[best_idx].copy()
                best_score = fitness_scores[best_idx]
            while len(new_population) < self.population_size:
                parent1, parent2 = self.select_parents(fitness_scores)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.append(child1)
                new_population.append(child2)
            new_population = new_population[:self.population_size]
            new_population = np.array(new_population)
            if self.elitism:
                replace_idx = np.random.randint(0, self.population_size)
                new_population[replace_idx] = best_individual
            self.population = new_population
            current_best_fitness = max(fitness_scores)
            if current_best_fitness > best_fitness_overall:
                best_fitness_overall = current_best_fitness
                best_chromosome_overall = self.population[np.argmax(fitness_scores)].copy()
            print(f"Generation {generation+1}: Best Fitness = {current_best_fitness:.4f}")
        final_scores = np.array([self.fitness_function(ch) for ch in self.population])
        best_idx = np.argmax(final_scores)
        best_chromosome = self.population[best_idx]
        best_fitness = final_scores[best_idx]
        if best_fitness_overall > best_fitness:
            best_fitness = best_fitness_overall
            best_chromosome = best_chromosome_overall
        return best_chromosome, best_fitness

