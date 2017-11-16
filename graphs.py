# Code to design and implement a data structure for a social network
# Author: Mirav Gokani
import sys
import pprint
graph = {}  # Define empty dictionary


# Function to input user values and add to dictionary
def add_node():
    entered_graph = False
    while not entered_graph:
        source_node = input("Enter a source node:")
        try:
            num_neighbours = int(input("Enter how many neighbours this node has including previously entered nodes:"))
        except ValueError:
            print("\nYou did not enter a valid integer")
            sys.exit(0)
        graph[source_node] = []
        for neighbour in range(num_neighbours):
            neighbour = input("Enter neighbor node:")
            graph[source_node].append(neighbour)
        end_loop = input("Enter y to finish graph entry:")
        end_loop = end_loop.lower()
        if end_loop == "y":
            entered_graph = True


# Function will return all paths between two nodes in graph
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# Function to print the network at different hops with hop as an input
def print_distance_nodes(graph, start, hop_count, path=[]):
    path.append(start)
    if hop_count == 0:
        print(start)
    hop_count -= 1
    for node in graph[start]:
        if node != start and node not in path:
            print_distance_nodes(graph, node, hop_count, path)


def main():
    add_node()
    pprint.pprint(graph, width=1)

    print("Enter the names of two people and find the connection between them")
    i = input("enter name 1:")
    j = input("enter name 2:")
    if i not in graph or j not in graph:
        print("Path not found")
    else:
        print("Printing all paths between", i, "and", j, find_all_paths(graph, i, j))
    k = input("enter name 3:")
    try:
        hop_count = int(input("Enter hop count:"))
    except ValueError:
        print("\n You did not enter a valid integer")
        sys.exit(0)
    if k not in graph:
        print("Name not found or wrong hop count value")
    else:
        print("Printing all nodes that are", hop_count, "hops away from", k)
        print_distance_nodes(graph, k, hop_count)


if __name__ == "__main__":
    main()

