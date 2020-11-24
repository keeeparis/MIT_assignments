# Problem Set 4A
# Name: <Vladimir Trotsenko>
# Collaborators:
# Time Spent: 4:20 :>

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    final = []
    if len(sequence) == 1:
        final.append(sequence)
        return final
    else:
        temp = get_permutations(sequence[1:])
        for i in temp:
            for j in range(len(i)+1):
                temp_list = list(i)
                temp_list.insert(j,sequence[0])
                temp_list = ''.join(temp_list)
                final.append(temp_list) 
        final.sort()
        return final

if __name__ == '__main__':
    #EXAMPLE
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # f = open('123456789', 'w')
    # f.write(' '.join(get_permutations(example_input)))
    # f.close()
    
    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)
    # example_input = 'abc'
    # print('Input:', example_input)
    # # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    
    # example_input = 'abc'
    # print('Input:', example_input)
    # # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    # pass #delete this line and replace with your code here




