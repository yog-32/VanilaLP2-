import heapq

class Node:
    def __init__(self, state, parent=None, action=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g_cost = g_cost
        self.h_cost = h_cost

    def __lt__(self, other):
        return (self.g_cost + self.h_cost) < (other.g_cost + other.h_cost)

class Heuristic:
    @staticmethod
    def manhattan_distance(state, goal_state):
        return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

class Successors:
    @staticmethod
    def get_actions(state):
        x, y = state
        return [('Move Right', (x+1, y), 1), ('Move Down', (x, y+1), 1)]

    @staticmethod
    def get_result(state, action):
        return action[1]

    @staticmethod
    def get_step_cost(state, action):
        return action[2]

def a_star_search(initial_state, goal_state, heuristic, successors):
    start_node = Node(initial_state, None, None, 0, heuristic(initial_state, goal_state))
    open_list = [start_node]
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            return get_solution_path(current_node)

        closed_set.add(current_node.state)

        for action in successors.get_actions(current_node.state):
            successor_state = successors.get_result(current_node.state, action)
            step_cost = successors.get_step_cost(current_node.state, action)

            if successor_state in closed_set:
                continue

            successor_g_cost = current_node.g_cost + step_cost

            successor_node = None
            for node in open_list:
                if node.state == successor_state:
                    successor_node = node
                    break

            if not successor_node or successor_g_cost < successor_node.g_cost:
                successor_node = Node(successor_state, current_node, action[0], successor_g_cost, heuristic(successor_state, goal_state))
                heapq.heappush(open_list, successor_node)

    return None

def get_solution_path(node):
    path = []
    while node:
        path.append((node.action, node.state))
        node = node.parent
    return list(reversed(path))

# Example usage:

# Define the initial state and goal state
initial_state = (0, 0)
goal_state = (4, 4)

# Solve the problem using A* search
solution = a_star_search(initial_state, goal_state, Heuristic.manhattan_distance, Successors)

if solution:
    print("Solution found:")
    for action, state in solution:
        print(f"- {action}: {state}")
else:
    print("No solution found.")
