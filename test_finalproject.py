
from thirdscript import*

def test_count_substrings(seq, k):

     
        
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

    assert num_observed_substrings

def test_count_possible_substrings(seq, k):
     # Compute the number of possible substrings using the formula (n - k + 1), 
    # where n is the length of the sequence and k is the size of the substring
    num_possible_substrings = len(seq) - k + 1

    assert num_possible_substrings

def test_calculate_linguistic_complexity(seq, k):
   # Count the number of different observed substrings of size k
    num_observed_substrings = count_substrings(seq, k)

    # Count the number of possible substrings of size k
    num_possible_substrings = count_possible_substrings(seq, k)

    # Compute the linguistic complexity using the formula num_observed_substrings / num_possible_substrings
    linguistic_complexity = num_observed_substrings / num_possible_substrings

    assert linguistic_complexity(seq,k)
    
