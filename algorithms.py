#!/usr/bin/env python3

from Bookcase import Bookcase

def findSpace(aBookcase):
    """
    Returns the row and column of a free position in aBookcase.
    """
    assert aBookcase.getEmptySpaces() >= 1
    rows = aBookcase.getRows()
    columns = aBookcase.getColumns()

    aSpace = (aBookcase.isEmptySpace(rows, columns))
    for row in range(aBookcase.rows):
        for column in range(aBookcase.columns):
            if aBookcase.isEmptySpace(rows, columns):
                 aBookcase.findSpace = True
    return aSpace


def addItem(aBookcase, name, mediaType):
    """
    Returns False if aBookcase is full, otherwise returns True and
    adds item of given name and mediaType to aBookcase.
    """
    assert str(name) != ""
    assert str(mediaType) != ""
    if aBookcase.getEmptySpaces() == 0:
        return False
    elif findSpace(aBookcase) == True:
        aBookcase.setName(findspace)
        aBookcase.setMediaType(findSpace)
    return True


def countItems(aBookcase, mediaType):
    """
    Returns how many items of given mediaType are in aBookcase.
    """
    assert len(mediaType) > 0
    countItems = 0
    for row in range(aBookcase.rows):
        for column in range(aBookcase.columns):
            if isEmptySpace == False:
                update.countItems + 1
    return countItems


# Tests


GAME = "video game"         # constants for the media types, to avoid typos

FILM = "film"

BOOK = "book"

SONG = "music"



# create two bookcases and check they're empty



tiny = Bookcase(1, 1)      # borderline case: smallest possible bookcase

small = Bookcase(2, 3)



assert tiny.getRows() == 1

assert tiny.getColumns() == 1

assert small.getRows() == 2

assert small.getColumns() == 3



assert tiny.isEmptySpace(0, 0)          # borderline case: first item

assert tiny.getEmptySpaces() == 1



assert small.isEmptySpace(1, 2)         # borderline case: last item

assert small.getEmptySpaces() == 2*3



# smallest bookcase stays empty



assert findSpace(tiny) == (0, 0)



# add to the other an item in 2nd shelf, 1st place



small.setName(1, 0, "Store Wars episode X")

small.setType(1, 0, FILM)



# check the resulting bookcases



assert small.getType(1, 0) == FILM

assert small.getEmptySpaces() == 2*3 - 1    # one space less

assert findSpace(small) != (1, 0)           # any other space is free



# add another item, in first position



small.setName(0, 0, "Angry Poultry")

small.setType(0, 0, GAME)



# check the resulting bookcase



assert findSpace(small) != (0, 0) and findSpace(small) != (1, 0)



print("findSpace passed all tests")



# there are 4 free spaces, so adding 2 items must succeed



spaces = small.getEmptySpaces()

assert addItem(small, "Algorhythms, date structures and compatibility", BOOK)

assert addItem(small, "Angry Poultry: The Pigs Strike Back", GAME)



# check the resulting bookcase: 2 spaces less



assert small.getEmptySpaces() == spaces - 2



print("addItem passed all tests")



# the previous tests only added 1 film, 1 book and 2 video games



assert countItems(small, FILM) == 1

assert countItems(small, BOOK) == 1

assert countItems(small, GAME) == 2

assert countItems(small, SONG) == 0



print("countItems passed all tests")
