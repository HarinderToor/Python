#!/usr/bin/env python3


class Bookcase:
    """
    Implements an ADT to store various media items on virtual shelves.
    A bookcase has r rows (shelves) and c columns, numbered from zero.
    A valid position is given by a row from 0 to r-1 and a column from 0 to c-1.
    """
    
    def __init__(self, rows, columns):
        """
        Assumes rows and columns are positive integers and
        creates an empty bookcase with that many rows (shelves) and columns.
        """
        assert rows > 0 and columns > 0
        # create a matrix with the name of each item, initially the empty string
        self.name = [["" for column in range(columns)] for row in range(rows)]
        # create a matrix with the type of each item, initially the empty string
        self.type = [["" for column in range(columns)] for row in range(rows)]
        self.rows = rows
        self.columns = columns
   
    def getRows(self):
        """
        Returns the number of rows (shelves) in the bookcase.
        """
        return self.rows
    
    def getColumns(self):
        """
        Returns the length of each shelf in the bookcase.
        """
        return self.columns

    def getName(self, row, column):
        """
        Assumes the position is valid and returns a string.
        The string is empty if there's no item at that position,
        otherwise it's that item's name.
        """
        assert 0 <= row and row < self.rows
        assert 0 <= column and column <= self.columns
        return self.name[row][column]

    def getType(self, row, column):
        """
        Assumes the position is valid and returns a string.
        The string is empty if there's no item at that position,
        otherwise it's that item's media type.
        """
        assert 0 <= row and row < self.rows
        assert 0 <= column and column <= self.columns
        return self.type[row][column]

    def setName(self, row, column, name):
        """
        Assumes the position is valid and that name is a non-empty string,
        and sets the item name for that position.
        """
        assert 0 <= row and row < self.rows
        assert 0 <= column and column <= self.columns
        assert len(name) > 0
        self.name[row][column] = name

    def setType(self, row, column, mediaType):
        """
        Assumes the position is valid and that mediaType is a non-empty string,
        and sets the item name for that position.
        """
        assert 0 <= row and row < self.rows
        assert 0 <= column and column <= self.columns
        assert len(mediaType) > 0
        self.type[row][column] = mediaType

    def isEmptySpace(self, row, column):
        """
        Assumes the position is valid and returns True if the position is empty,
        otherwise False.
        """
        assert 0 <= row and row < self.rows
        assert 0 <= column and column <= self.columns
        return self.getName(row, column) == ""

    def getEmptySpaces(self):
        """
        Returns the number of empty spaces in the bookcase.
        """
        spaces = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.isEmptySpace(row, column):
                    spaces = spaces + 1
        return spaces
