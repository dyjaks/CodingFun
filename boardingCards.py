from collections import deque


class Travel:
    class BoardingCard:
        def __init__(self, origin, destination, transport_type, seat_assignment):
            self.origin = origin
            self.destination = destination
            self.transport_type = transport_type
            self.seat_assignment = seat_assignment

    '''
    Takes a list of boarding cards, prints valid itenary
    Problem statement assumes valid approach, even so we'll assume otherwise
    No source or dest is provided, must find one so should use top sort
    Will takes kahns approach
    Space Complexity: O(V+E)
    Time Complexity: O(V+E)
    '''
    class NoPathFoundException(Exception):
        def __init__(self, message):
            self.message = message

    def top_sort(graph, node_degree):
        def generate_output():
            res = []
            for ix, p in enumerate(path):
                res.append(f"{ix}: Take the {p.transport_type} from {p.origin} to {p.destination}. Use seat: {p.seat_assignment}")

            return res

        path = []
        q = deque()
        for degree in node_degree:
            if node_degree[degree] == 0:
                q.append(degree)

        while q:
            curr = q.popleft()
            path.append(curr)

            if curr in graph:
              for node in graph[curr]:
                  node_degree[node[0]] -= 1
                  if node_degree[node[0]] == 0:
                      q.append(node[0])

        if len(path) != len(node_degree):
            raise Travel.NoPathFoundException('No Valid Path Exists')

        #output = generate_output()
        return path

    def get_itenary(cards):
        def build_adj_list() -> dict:
            mp = {}
            for card in cards:
                if card.origin not in mp:
                    mp[card.origin] = []
            for card in cards:
                mp[card.origin].append((card.destination, card))

            return mp

        def build_degree_counter(graph: dict) -> dict:
            d = {}
            for c in cards:
                if c.origin not in d:
                    d[c.origin] = 0
                if c.destination not in d:
                    d[c.destination] = 0
            for v in graph:
                for target in graph[v]:
                    d[target[0]] += 1

            return d

        graph = build_adj_list()
        #print(graph)
        node_degree = build_degree_counter(graph)
        #print(node_degree)
        possible_path = []
        try:
            possible_path = Travel.top_sort(graph, node_degree)
            possible_path.append('You have arrived at your final destination.')
        except Travel.NoPathFoundException:
            return ['We are not able to find a working itneary with those boarding cards']

        return possible_path


if __name__ == '__main__':
    trip1 = Travel.BoardingCard('Seattle', 'Los Angeles', 'Plane', '32A')
    trip2 = Travel.BoardingCard('Atlanta', 'Dallas', 'Car', 'No Seat Assignment')
    trip3 = Travel.BoardingCard('Los Angeles', 'Atlanta', 'Train', 'First Class 2B')
    trips = [trip1, trip2, trip3]
    trip_order = Travel.get_itenary(trips)
    print(trip_order)
