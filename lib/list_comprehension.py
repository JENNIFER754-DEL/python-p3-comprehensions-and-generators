#!/usr/bin/env python3

# lib/list_comprehension.py

def return_evens(sequence):
    """Return a list of all even elements from the given sequence."""
    return [x for x in sequence if x % 2 == 0]

def make_exclamation(sentences):
    """Return a list of sentences with exclamation marks at the end."""
    return [sentence + "!" for sentence in sentences]
