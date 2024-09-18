from collections import defaultdict

def find_route(tickets, start, cities):
    graph = defaultdict(list)
    for src, dest in tickets:
        graph[src].append(dest)

    route = []

    def dfs(city):
        route.append(city)

        if len(route) == len(cities):
            return True

        if city in graph:
            destinations = graph[city][:]
            for next_city in destinations:
                graph[city].remove(next_city)

                if dfs(next_city):
                    return True
                graph[city].append(next_city)
        route.pop()
        return False

    dfs(start)
    return route

tickets = [
    ("Paris", "Skopje"), ("Zurich", "Amsterdam"), ("Prague", "Zurich"),
    ("Barcelona", "Berlin"), ("Kiev", "Prague"), ("Skopje", "Paris"),
    ("Amsterdam", "Barcelona"), ("Berlin", "Kiev"), ("Berlin", "Amsterdam")
]

cities = ["Amsterdam", "Kiev", "Zurich", "Prague", "Berlin", "Barcelona"]
start_city = "Kiev"

route = find_route(tickets, start_city, cities)
print("Route taken by son:", route)
