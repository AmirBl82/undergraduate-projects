import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
import random

class ParticleSwarmOptimization:
    def __init__(self, X, y, swarm_size=30, max_iter=10, w=0.5, c1=1.0, c2=1.0, n_splits=3, random_state=42):
        self.X = X
        self.y = y
        self.num_features = X.shape[1]
        self.swarm_size = swarm_size
        self.max_iter = max_iter
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.n_splits = n_splits
        self.random_state = random_state

        np.random.seed(self.random_state)
        random.seed(self.random_state)

        self.positions = np.random.randint(2, size=(self.swarm_size, self.num_features))
        self.velocities = np.random.uniform(-1, 1, size=(self.swarm_size, self.num_features))
        self.pbest_positions = self.positions.copy()
        self.pbest_scores = np.zeros(self.swarm_size)
        self.gbest_position = None
        self.gbest_score = 0.0
        self.cv = StratifiedKFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)

    def fitness_function(self, position):
        selected_features = np.where(position == 1)[0]
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

    def update_pbest_gbest(self):
        for i in range(self.swarm_size):
            fitness = self.fitness_function(self.positions[i])
            if fitness > self.pbest_scores[i]:
                self.pbest_scores[i] = fitness
                self.pbest_positions[i] = self.positions[i].copy()
            if fitness > self.gbest_score:
                self.gbest_score = fitness
                self.gbest_position = self.positions[i].copy()

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def run(self):
        self.update_pbest_gbest()
        for iteration in range(self.max_iter):
            for i in range(self.swarm_size):
                r1 = np.random.rand(self.num_features)
                r2 = np.random.rand(self.num_features)
                self.velocities[i] = (
                    self.w * self.velocities[i]
                    + self.c1 * r1 * (self.pbest_positions[i] - self.positions[i])
                    + self.c2 * r2 * (self.gbest_position - self.positions[i])
                )
                prob = self.sigmoid(self.velocities[i])
                self.positions[i] = np.where(np.random.rand(self.num_features) < prob, 1, 0)
            self.update_pbest_gbest()
            print(f"Iteration {iteration+1}: gbest_score = {self.gbest_score:.4f}")
        return self.gbest_position, self.gbest_score
