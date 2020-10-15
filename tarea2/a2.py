def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char == nucleotide:
            count = count + 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(possible_dna):
    """(str) -> bool

    Return True if and only id possible Dna sequence contains valid
    nucleotides ('A', 'G', 'C', 'T'). Lowercase characters are not valid
    for dna sequence
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('MMCGGC')
    False
    >>>is_valid_sequence('OOCGGC')
    False
    """
    resul = True
    for char in possible_dna:
        if not char in 'ATCG':
            resul= False

    return resul

def insert_sequence(dna1, dna2, index):
     """ (str, str, int) -> str

     Return the DNA sequence obtained by inserting the second DNA
     sequence into the first DNA sequence at the given index.
     (You can assume that the index is valid.)
     
     >>> insert_sequence('ATGC', 'CG', 2)
     'ATCGGC'
     >>> insert_sequence('ATGG', 'CC', 1)
     'ACCTGG'
     """
     return dna1[: index] + dna2 + dna1[index:] 

def get_complement(nucleotide):
    """ (str)-> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A' 
    """
    dna = 'ATCG'
    complement = 'TAGC'
    index = -1
    
    for char in dna:
        index = index + 1
        if char == nucleotide:
            resul = complement[index]
            
    return resul

def get_complementary_sequence(dna):
    """(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    >>> get_complementary_sequence('GA')
    'CT'
    """
    resul =''
    
    for char in dna:
        comp = get_complement(char)
        resul = resul + comp
        
    return resul

def suma_pares(num1, num2):
    i = num1
    result=0
    while i <= num2:
        if i%2==0:
            result= result + i
            print(result)
        i = i + 2
    return result

def suma_impares(num1, num2):
    i = num1
    result=0
    while i <= num2:
        if i%2!=0:
            result= result + i
            print(result)
        i = i + 2
    return result

