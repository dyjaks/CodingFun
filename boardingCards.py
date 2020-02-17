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

    def top_sort(self, graph: dict, node_degree: dict) -> list[str]:
        def generate_output():
            res = []
            for ix, p in enumerate(path):
                res.append(f"{ix}: Take the {p.transport_type} from {p.origin} to {p.destination}. Use seat: {p.seat_assignment}")

            return res

        path = []
        q = deque()
        for degree in node_degree:
            if node_degree[degree] == 0:
                q.append(node_degree)

        while q:
            curr = q.popleft()
            path.append(graph[curr][1])

            for node in node_degree[curr]:
                node_degree[node] -= 1
                if node_degree[node] == 0:
                    q.append(node)

        if len(path) != len(node_degree):
            raise self.NoPathFoundException('No Valid Path Exists')

        output = generate_output()
        return output

    def get_itenary(self, cards: list[BoardingCard]) -> list[str]:
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
            for v in graph:
                for target in graph[v][0]:
                    d[target] = d.get(target, 0) + 1

            return d

        graph = build_adj_list()
        node_degree = build_degree_counter(graph)
        possible_path = []
        try:
            possible_path = self.top_sort(graph, node_degree)
            possible_path.append('You have arrived at your final destination.')
        except self.NoPathFoundException:
            return ['We are not able to find a working itneary with those boarding cards']

        return possible_path


if __name__ == '__main__':
    trip1 = self.BoardingCard('Seattle', 'Los Angeles', 'Plane', '32A')
    trip2 = self.BoardingCard('Atlanta', 'Dallas', 'Car', 'No Seat Assignment')
    trip3 = self.BoardingCard('Los Angles', 'Atlanta', 'Train', 'First Class 2B')
    trips = [trip1, trip2, trip3]
    trip_order = self.get_itenary(trips)
    print(trip_order)
