#!/usr/local/bin/python


# def answer(words, start, end):
#     # Narrow down the search criteria
#     # Find words with have same length as the start and end words
#     valid_words = [start for start in words if len(start) == len(end)]
#
#     Group words that differ by one letter
#     for i in range(len(word)):
#       different = word[:i] + word[i + 1:]

#     # Find words that have at least length of word-1 chars in start and end words
#     for word in valid_words:
#         similar_words = []
#         matched = 0
#         for i in range(len(word)):
#             if word[i] in start and word[i] in end:
#                 matched += 1
#
#         if matched > 2:
#             similar_words.append(word)
#             print similar_words

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
    # Un mark all nodes
    # Create a queue
    # Choose start node and mark as visited
    # While there is a queue, visit adjacent node, mark as visited, insert into queue
    # Remove first node if no adjacent is found
    # First, build the graph from the list of words

    visited_node = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        yield node, path

        for neighbours in graph[node] - visited_node:
            visited_node.add(neighbours)
            queue.append(path + [neighbours])


def answer(words, start, end):
    """
    Compute the answer to the word puzzle by building and searching through a graph compiled from a list of words and
    their similarities.
    """

    graph = build_graph(words)
    for node, path in search_graph(graph, start):
        if node == end:
            return path
        # if node not in visited_node:
        #     if node == end:
        #         return path
        #     visited_node.add(node)

        # for neighbours in graph[node]:
        #     queue.append(neighbours, [neighbours])

if __name__ == '__main__':
    with open('words.txt') as f:
        words = f.read().splitlines()

    print answer(words, 'short', 'bread')
