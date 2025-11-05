from sklearn.datasets import load_breast_cancer
from ga import GeneticAlgorithm
from pso import ParticleSwarmOptimization
import time

def main():
    data = load_breast_cancer()
    X = data.data
    y = data.target

    print("=== Genetic Algorithm ===")
    start_time_ga = time.time()
    ga = GeneticAlgorithm(
        X=X,
        y=y,
        population_size=30,
        num_generations=40,
        mutation_rate=0.2,
        elitism=True,
        n_splits=3,
        tournsize=3,
        random_state=42
    )
    best_chrom_ga, best_fitness_ga = ga.run()
    end_time_ga = time.time()
    ga_execution_time = end_time_ga - start_time_ga
    print("GA - Best Chromosome:", best_chrom_ga)
    print(f"GA - Best Fitness (CrossVal): {best_fitness_ga:.4f}")
    print(f"GA - Execution Time: {ga_execution_time:.4f} seconds")

    print("\n=== Particle Swarm Optimization ===")
    start_time_pso = time.time()
    pso = ParticleSwarmOptimization(
        X=X,
        y=y,
        swarm_size=30,
        max_iter=40,
        w=0.5,
        c1=1.0,
        c2=1.0,
        n_splits=3,
        random_state=42
    )
    best_pos_pso, best_fitness_pso = pso.run()
    end_time_pso = time.time()
    pso_execution_time = end_time_pso - start_time_pso
    print("PSO - Best Position:", best_pos_pso)
    print(f"PSO - Best Fitness (CrossVal): {best_fitness_pso:.4f}")
    print(f"PSO - Execution Time: {pso_execution_time:.4f} seconds")

    print("\n=== Comparison ===")
    if best_fitness_ga > best_fitness_pso:
        print("Genetic Algorithm performed better on this dataset.")
    elif best_fitness_ga < best_fitness_pso:
        print("Particle Swarm Optimization performed better on this dataset.")
    else:
        print("Both algorithms performed equally well on this dataset.")

    print("\n=== Execution Time Comparison ===")
    if ga_execution_time < pso_execution_time:
        print(f"Genetic Algorithm was faster by {pso_execution_time - ga_execution_time:.4f} seconds.")
    elif ga_execution_time > pso_execution_time:
        print(f"Particle Swarm Optimization was faster by {ga_execution_time - pso_execution_time:.4f} seconds.")
    else:
        print("Both algorithms took the same amount of time to execute.")

if __name__ == "__main__":
    main()
