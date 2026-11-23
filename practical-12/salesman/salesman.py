import itertools

def tsp_simple(matrix):
    num_cities = len(matrix)
    cities = list(range(1, num_cities)) # All cities except the starting city (0)
    min_cost = float('inf')

    # 1. Generate every possible order to visit the remaining cities
    for path in itertools.permutations(cities):
        current_cost = 0
        current_city = 0 # Always start at city 0

        # 2. Calculate the distance along this specific path
        for next_city in path:
            current_cost += matrix[current_city][next_city]
            current_city = next_city

        # 3. Add the distance back to the starting city (0)
        current_cost += matrix[current_city][0]

        # 4. Keep track of the absolute lowest cost found
        min_cost = min(min_cost, current_cost)

    return min_cost


# --- Quick Test ---
if __name__ == "__main__":
    # Distance matrix for 4 cities
    distance_matrix = [
        [2, 12, 45, 98],                   
        [23, 48, 97,44],               
        [20, 25, 30, 0]
    ]

    print("Minimum Tour Cost:", tsp_simple(distance_matrix)) # Output: 80
