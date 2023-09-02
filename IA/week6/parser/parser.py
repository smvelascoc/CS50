import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VS | NP VS C
S -> S Conj S

NP -> Det NP | Adj NP | N | NP Conj NP | NP P NP
VS -> V | VS Conj VS | V Adv | Adv V | V C
C -> NP | NP P NP | P NP | NP Adv | P NP Adv

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    nltk.download('punkt')
    s = nltk.tokenize.word_tokenize(sentence)

    #Remove all non alphanumerical values
    for word in s:
        if not word.isalpha(): s.remove(word)

    #Lower all the words
    for i in range(len(s)): s[i] = s[i].lower()

    return s
    #raise NotImplementedError


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    nps = list()

    for st in tree.subtrees(filter=lambda t: t.label()=='NP'):
        number = 0
        for st1 in st.subtrees():
            if st1.label() == 'P' or st1.label() == 'Conj':
                number +=1

        if number == 0: nps.append(st)

    nps_ans = nps

    #Cleaning repeated values contained in others NP
    for st in reversed(nps):
        
        for j in range(len(nps)-1):
            if  st in nps[j]:
                if st in nps_ans: nps_ans.remove(st)

    return nps_ans
    #raise NotImplementedError


if __name__ == "__main__":
    main()
