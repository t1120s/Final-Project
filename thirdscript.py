#!/usr/bin/env python3

import sys

def count_substrings(seq, k):
    """
    Count the number of different observed substrings of size k in a DNA sequence.

    Parameters:
    seq (str): DNA sequence string
    k (int): size of the substring

    Returns:
    int: number of different observed substrings of size k
    """
     # Initialize an empty dictionary
    substr_counts = {}

    # Slide the window along the sequence
    for i in range(len(seq)-k+1):
        # Get the substring of size k
        substr = seq[i:i+k]

        # If the substring is observed for the first time, add it to the dictionary
        if substr not in substr_counts:
            substr_counts[substr] = 1
        # If the substring is already in the dictionary, increment its count
        else:
            substr_counts[substr] += 1

    # Count the number of unique substrings in the dictionary
    num_observed_substrings = len(substr_counts)

    return num_observed_substrings

seq = "ATGTCTGTCTGTA"
k = 3
num_observed_substrings = count_substrings(seq, k)
print(num_observed_substrings)  # Output: 6

def count_possible_substrings(seq, k):
    """
    Count the number of possible substrings of size k in a DNA sequence.

    Parameters:
    seq (str): DNA sequence string
    k (int): size of the substring

    Returns:
    int: number of possible substrings of size k
    """
    # Compute the number of possible substrings using the formula (n - k + 1), 
    # where n is the length of the sequence and k is the size of the substring
    num_possible_substrings = len(seq) - k + 1

    return num_possible_substrings


seq = "ATGTCTGTCTGTA"
k = 3
num_possible_substrings = count_possible_substrings(seq, k)
print(num_possible_substrings)  # Output: 11

def test_calculate_linguistic_complexity(seq, k):
    """
    Calculate the linguistic complexity of a DNA sequence.

    Parameters:
    seq (str): DNA sequence string
    k (int): size of the substring

    Returns:
    float: linguistic complexity of the DNA sequence
    """
   # Count the number of different observed substrings of size k
    num_observed_substrings = count_substrings(seq, k)

    # Count the number of possible substrings of size k
    num_possible_substrings = count_possible_substrings(seq, k)

    # Compute the linguistic complexity using the formula num_observed_substrings / num_possible_substrings
    linguistic_complexity = num_observed_substrings / num_possible_substrings

    assert linguistic_complexity(seq,k)
    

seq = "ATGTCTGTCTGTA"
k = 3
linguistic_complexity = calculate_linguistic_complexity(seq, k)
print(linguistic_complexity)  # Output: 0.545