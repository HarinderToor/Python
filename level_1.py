#!/usr/local/bin/python


def answer(data, n):
    dict = {}
    for i in range(len(data)):
        dict[data[i]] = dict.get(data[i], 0) + 1

    for key, values in dict.items():
        if values > n:
            for i in range(values):
                data.remove(key)
    return data
