#!/usr/local/bin/python

from collections import defaultdict
from collections import deque
from itertools import product


def build_graph(words):

    # Build a graph
    # Each word is a node on the graph
    #   Build a graph with all the nodes
    #   Create edges between nodes that differ by one character
    #   Nodes are only connected if they are different by one character
    # Search answer
    #   (BFS or A*?) graph to find the "shortest" path between two (start/end) nodes

    # bed - key
    # bid - value
    # bin - value
    # pin - value

    """
    Construct a graph of nodes for all words and connect nodes that differ by one letter.
    """

    # Use default dicts for adding new items without key errors
    similar_words = defaultdict(list)
    word_graph = defaultdict(set)

    for word in words:
        # Group words that differ by one letter
        # Only consider same length words
        for i in range(len(word)):
            # if len(word) != len(word[i]):
            #     return
            different = word[:i] + word[i+1:]
            if different in similar_words:
                similar_words[different].append(word)
            else:
                similar_words[different] = [word]

    # Add all the nodes for the similar words
    for key, values in similar_words.items():
        # Get ordered pairs
        for word_1, word_2 in product(values, repeat=2):
            if word_1 != word_2:
                word_graph[word_1].add(word_2)
                word_graph[word_2].add(word_1)

    return word_graph


def search_graph(graph, start):
    # Breadth First Search
    # https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
    # Un mark all nodes
    # Create a queue and choose a start node and mark as visited
    # While there is a queue, visit adjacent node, mark as visited, insert into queue
    # Remove first node if no adjacent is found

    queue = deque([[start]])
    visited_node = set()

    while queue:
        # Explore a path
        path = queue.pop()
        # Get last node from this path
        node = path[-1]

        yield node, path

        # Find nearest nodes in graph that have not been visited
        for nearest in graph[node] - visited_node:
            # Mark as visited and insert to queue
            visited_node.add(nearest)
            queue.append(path + [nearest])


def answer(words, start, end):
    """
    Compute the answer to the puzzle by building and searching through a graph compiled from a list of words and
    their similarities.
    """
    valid_words = [x for x in words if len(start) == len(end)]
    # Build a graph from words of same length as start and end
    graph = build_graph(valid_words)
    
    for node, path in search_graph(graph, start):
        if node == end:
            return path
            
if __name__ == '__main__':
    with open('words.txt') as f:
        words = f.read().splitlines()

    print answer(words, 'short', 'bread')
