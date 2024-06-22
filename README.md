# ABC Algorithm for Function Optimization

## Objective
The program aims to find the minimum value of the objective function:

\[ f(x, y) = x^2 + y^2 + 25 \cdot (\sin(x) + \sin(y)) \]

## Parameters
- **num_bees:** Total number of bees in the colony.
- **num_employed_bees:** Number of bees acting as employed bees.
- **num_onlooker_bees:** Number of bees acting as onlooker bees.
- **limit:** Limit on the number of trials before abandoning a food source by employed bees.
- **max_iterations:** Maximum number of iterations for the algorithm.
- **lower_bound:** Lower boundary of the search space for \( x \) and \( y \).
- **upper_bound:** Upper boundary of the search space for \( x \) and \( y \).

## Algorithm Overview
1. **Initialization:** Randomly initializes positions for employed bees within the search space and computes their fitness values.
2. **Employed Bees Phase:** Each employed bee explores a neighbor's position and updates its position if a better fitness value is found. Otherwise, it increments a trial counter.
3. **Onlooker Bees Phase:** Bees select food sources probabilistically based on fitness. They perform a similar exploration as employed bees.
4. **Scout Bees Phase:** If an employed bee exceeds the trial limit without improvement, it abandons its position and explores a new random position within the search space.
5. **Iteration:** The process repeats for a fixed number of iterations.
6. **Output:** Displays the best position and fitness found after all iterations.

## Implementation Notes
- Utilizes numpy for efficient array operations and random number generation.
- Includes functions for generating new positions based on a modified ABC algorithm.
- Uses roulette wheel selection for onlooker bees to choose food sources based on fitness probabilities.

## Conclusion
The program effectively demonstrates the ABC algorithm's ability to optimize the given objective function over a defined search space, showcasing how artificial intelligence techniques like swarm intelligence can be applied to optimization problems.
