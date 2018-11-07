'''
Python Functions from BioInformatics Course 1 Week 2 on Coursera:

In this week we discussed how replication works biologically. When DNA replicates it does
so asymmetrically; the forward and reverse half strands have different speeds. If one of the four nucleotides
in single-stranded DNA has a greater tendency than other nucleotides to mutate in single-stranded DNA, then we 
should observe a shortage of this nucleotide on the forward half-strand. We can take advantage of this knowledge
to help locate ORI. The moral of this chapter is that even though computational analysis can be powerful, 
bioinformaticians should collaborate with biologists to verify their predictions.
'''

# in this function we slide a window around the genome looking for statistics on the occurances of a nucleotide to help find the location of the forward and reverse half strand.
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array


# Reproduction of the PatternCount function here.
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 


# This is a faster version of our symbol array function to speed up the computation time
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# Reproduction of the PatternCount function here.
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

'''
We can use the information we learn from keeping track of the skew data on a genome to help us find the Origin of Replication
The origin will be where the skew diagram obtains a minimum! 
'''

# This function is for keeping track of the positive or negative skew based on the amounts of nucleotides
def SkewArray(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == "A" or Genome[i] == "T":
            skew.append(skew[i])
        elif Genome[i] == "G":
            skew.append(skew[i]+1)
        else:
            skew.append(skew[i]-1)
    return skew
	
def MinimumSkew(Genome):
    positions = [] 
    sk = SkewArray(Genome)
    m = min(sk.values())
    for key in sk:
        if sk[key] == m:
            positions.append(key)
    
    return positions

# This function finds the position in the Genome where the skew obtains a minimum.
def SkewArray(Genome):
    skew = {} 
    skew[0] = 0
    for i in range (len(Genome)):
        if Genome[i] == "A" or Genome[i] == "T":
            skew[i + 1] = skew [i]
        elif Genome[i] == "G":
            skew[i + 1] = skew[i] + 1
        else:
            skew[i + 1] = skew[i] - 1
    return skew

'''
Now we want to confirm our hypothesis by taking a look at the genome in this area that the skew is a minimum. We use our
frequent words function from the last week but it doesn't reveal any strings of length 9 that appear 3 or more times. 
However, Finding eight approximate occurrences of our target 9-mer and its reverse complement in a short region is even 
more statistically surprising than finding the six exact occurrences. Furthermore, the discovery of these approximate 
9-mers makes sense biologically, since DnaA can bind not only to “perfect” DnaA boxes but to their slight modifications as well.
'''

# This functions finds all approximate occurances of a pattern within a strings
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    n = len(Text)
    k = len(Pattern)
    p = Pattern
    for i in range(n - k + 1):
        q = Text[i:i+n]
        if HammingDistance(p,q) <= d:
            positions.append(i)
    return positions

# This function computes the 'Hamming distance' (mismatch) between 2 strings of DNA
def HammingDistance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count = count + 1
    return count
	
# This is a modification of our frequent words problem to account for slight mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        substrEqualsPattern = Text[i:i+len(Pattern)] == Pattern
        substrAproximateToPattern = HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d
        if substrEqualsPattern or substrAproximateToPattern:
            count += 1
    return count

def HammingDistance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count = count + 1
    return count
