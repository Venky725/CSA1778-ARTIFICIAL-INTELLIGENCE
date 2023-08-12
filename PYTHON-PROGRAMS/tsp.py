import itertools

def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def total_distance(path, cities):
    distance = 0
    for i in range(len(path) - 1):
        distance += euclidean_distance(cities[path[i]], cities[path[i + 1]])
    distance += euclidean_distance(cities[path[-1]], cities[path[0]])
    return distance

def tsp_bruteforce(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    best_path = None

    for path in itertools.permutations(range(num_cities)):
        distance = total_distance(path, cities)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return best_path, min_distance

# Example usage
cities = [
    (0, 0),
    (1, 3),
    (4, 2),
    (5, 7),
    (8, 1)
]

best_path, min_distance = tsp_bruteforce(cities)
print("Best Path:", best_path)
print("Min Distance:", min_distance)
