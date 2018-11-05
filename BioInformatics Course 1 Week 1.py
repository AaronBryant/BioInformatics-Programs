'''
Python Functions from BioInformatics Course 1 on Coursera:

Our theory is that finding frequent strings of text in a region of a genome will help us find the origin of replication.
This is often because certain proteins can only bind to DNA if a specific string of nucleotides is present, 
and if there are more occurrences of the string, then it is more likely that binding will successfully occur. 
(It is also less likely that a mutation will disrupt the binding process.)
'''

# In this function we input a piece of text and a pattern in that text and count the occurences of that pattern:
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 
	
# In this function we input a piece of text and a length, and the function returns a dictionary of how many string(s) there are of that length in the text.
def FrequencyMap(Text, k):
   freq = {}
   n = len(Text)
   for i in range(n-k+1):
       Pattern = Text[i:i+k]
       freq[Pattern] = 0
       for i in range(n-k+1):
           if Text[i:i+k] == Pattern:
              freq[Pattern] = freq[Pattern] + 1
   return freq	

# In this function we find the maximum value obtained from our FrequencyMap() function and we output the string(s) that achieves this value.
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for item in freq:
        if freq[item] == m:
            words.append(item)
    return words
	
'''
If we use our FrequentWords() function with different values for k,  we find a suprising number of words when k = 9. 
This might give us some clues to the location of our Origin of Replication.
Having one strand of DNA and a supply of “free floating” nucleotides we can imagine the synthesis of a complementary strand on a template strand.
This theory of synthesis was confirmed by experiments in 1958.
Now we will make functions that look for the reverse complement of a string, because a "free floating” strand will bind in this way.
Finding many occurences of a pattern and it's reverse complement leads us to believe that this pattern represents DnaA boxes.
DnaA is a protein that activates initiation of DNA replication in bacteria. It is a replication initiation factor which promotes the unwinding of DNA at oriC.
'''


# This takes a pattern and returns the reverse of that pattern.
def Reverse(Pattern):
    rev = ""
    for char in Pattern:
        rev = char + rev
    return rev
	
# This takes a pattern and returns it's complement.
def Complement(Pattern):
    rev = ""
    for char in Pattern:
        if char == 'A':
            rev = rev + 'T'
        elif char == 'T':
            rev = rev + 'A'
        elif char == 'G':
            rev = rev + 'C'
        elif char == 'C':
            rev = rev + 'G'
        else:
            print ('incorrect string')
    return rev   

# This function combines are Reverse() and our Complement() functions.
def ReverseComplement(Pattern):
    return Reverse(Complement(Pattern))

'''
To be sure we have found ORI we need to make sure that there are not other short regions in our Genome with the multiple occurences of the same pattern. 
This is similiar to our PatternCount() function. The only way in which our solution to the Pattern Matching Problem differs is that rather than counting 
the number of occurrences of the pattern, we first form an empty list and then append each starting position of the pattern to it when we encounter a match.
If we find a pattern and its reverse complement appears a suprising number of times in a region of a genome, our theory is that this region is the Origin of Replication.
'''

#This function outputs the starting positions where Pattern appears in Genome as a substring.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions
	
'''
Conclusion- 
We have written several algorithms for finding strings in a Genome, we also need an algorithm for finding a region of the Genome where there are clumps of patterns of text. 
Our theory is that this region would be the Origin of Replication. Apparently the course has created this algorithm and used it on the E. Coli genome, but it didn't give any clues.
Next week, we will look at more information to further narrow down how to find Origin of Replication in a Genome.
'''
