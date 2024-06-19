import numpy as np

'''
Authors: Chen Yangfeng, Diaz Jimenez Jorge Arif, 5BM1, Escom IPN
19/jun/24  Algoritmos Bioinpirados
'''
# Mínimo encontrado en x = -1.4541965942809285, y = -1.4541965942809285
# Valor mínimo de la función = -45.431121993577456

# Definir la función a minimizar
def objective_function(x, y):
    return x**2 + y**2 + 25 * (np.sin(x) + np.sin(y))

# Definir los parámetros del algoritmo ABC
num_bees = 40
num_employed_bees = 20
num_onlooker_bees = 20
limit = 5
max_iterations = 50
lower_bound = -5
upper_bound = 5

# Inicializar las posiciones de las abejas
positions = lower_bound + np.random.uniform(0, 1, (num_employed_bees, 2)) * (upper_bound - lower_bound)
fitness = np.array([objective_function(x, y) for x, y in positions])
trial = np.zeros(num_bees)

# Función para generar una nueva posición
def generate_new_position(position, phi, partner_position):
    return np.clip(position + phi * (position - partner_position), lower_bound, upper_bound)

# Función para realizar la selección por ruleta
def roulette_wheel_selection(probabilities):
    cumulative_sum = np.cumsum(probabilities)
    random_number = np.random.rand()
    for i, cumulative_prob in enumerate(cumulative_sum):
        if random_number < cumulative_prob:
            return i

# Proceso de la colmena artificial
for iteration in range(max_iterations):
    # Fase de abejas empleadas
    for i in range(num_employed_bees):
        j = np.random.randint(2)
        k = np.random.randint(num_employed_bees)
        while k == i:
            k = np.random.randint(num_employed_bees)
        phi = np.random.uniform(-1, 1)

        new_position = positions[i].copy()
        new_position[j] = generate_new_position(positions[i][j], phi, positions[k][j])
        new_fitness = objective_function(*new_position)
        if new_fitness < fitness[i]:
            positions[i] = new_position
            fitness[i] = new_fitness
            trial[i] = 0
        else:
            trial[i] += 1

    # Calcular las probabilidades de selección para abejas observadoras
    fitness_probabilities = fitness / np.sum(fitness)
    # fitness_probabilities = 1 / (1 + fitness_probabilities) # si f(i) >= 0
    fitness_probabilities = 1 + np.abs(fitness_probabilities) # si f(i) < 0
    fitness_probabilities /= np.sum(fitness_probabilities)  # Normalizar para que sumen 1
    
    # Fase de abejas observadoras
    for i in range(num_onlooker_bees):
        selected_bee = roulette_wheel_selection(fitness_probabilities)
        j = np.random.randint(2)
        k = np.random.randint(num_employed_bees)
        while k == selected_bee:
            k = np.random.randint(num_employed_bees)
        phi = np.random.uniform(-1, 1)
        
        new_position = positions[selected_bee].copy()
        new_position[j] = generate_new_position(positions[selected_bee][j], phi, positions[k][j])
        new_fitness = objective_function(*new_position)
        if new_fitness < fitness[selected_bee]:
            positions[selected_bee] = new_position
            fitness[selected_bee] = new_fitness
            trial[selected_bee] = 0
        else:
            trial[selected_bee] += 1

    # Fase de abejas exploradoras
    for i in range(num_employed_bees):
        if trial[i] > limit:
            if np.argmin(fitness) != i: # check if current bee is not at the minimum fitness position
                positions[i] = lower_bound + np.random.rand() * (upper_bound - lower_bound)
                fitness[i] = objective_function(*positions[i])
                trial[i] = 0

    # Imprimir el mejor resultado de la iteración actual
    best_fitness = np.min(fitness)
    best_position = positions[np.argmin(fitness)]
    print(f"Iteración {iteration + 1}: Mejor posición = {best_position}, Mejor fitness = {best_fitness}")

# Resultado final
best_fitness = np.min(fitness)
best_position = positions[np.argmin(fitness)]
print(f"\nMejor posición final = {best_position}, Mejor fitness final = {best_fitness}")
#print(positions)
