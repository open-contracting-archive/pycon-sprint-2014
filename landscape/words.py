import re
from nltk.corpus import wordnet as wn


def gen_string_pairs(string, max_len=2):
    """
    Generates pairs of a string by splitting it at various points.

    ``max_len`` optionally enforces a max_length for each side, defaults to two characters.

    Examples:

        > list( gen_pairs('contractemail') )
        [('contra', 'ctemail'),
         ('contrac', 'temail'),
         ('contract', 'email'),
         ('contracte', 'mail'),
         ('contractem', 'ail'),
         ('contractema', 'il'),
         ('contrac', 'temail'),
         ('contra', 'ctemail'),
         ('contr', 'actemail'),
         ('cont', 'ractemail'),
         ('con', 'tractemail'),
         ('co', 'ntractemail')]

        > list( gen_pairs('noticeid') )
        [('noti', 'ceid'), 
         ('notic', 'eid'), 
         ('notice', 'id'), 
         ('noti', 'ceid'), 
         ('not', 'iceid'), 
         ('no', 'ticeid')]

        > list( gen_pairs('org') )
        [('o', 'rg'), 
         ('or', 'g')]
    """
    sz = len(string)
    if sz == 1:
        return
    half = sz / 2
    stop = max_len - 1
    for i in range(half, sz-stop):
        yield string[:i], string[i:]
    for i in range(half, sz-stop):
        yield string[:-i], string[-i:]


def is_word(string):
    """
    Returns True if a string is a known word in the wordnet, None otherwise.
    """
    if wn.synsets(string):
        return True

def find_two_words(string):
    """
    Finds two words in a string, or its best guess of those words.

    Returns a 2-tuple of, ie: (left, right) or None if there are no known words 
    (relatively rare actually, since 'o' is technically a word, for instance)

    Examples:

        > find_two_words('noticeid')
        "notice", "id"

        > find_two_words("valuemin")
        "value", "min"

        > find_two_words("thinggbrsh")
        "thing", "gbrsh"

        > find_two_words("pwoe")
        None

    """
    best = None
    best_score = 0
    for left, right in gen_string_pairs(string):
        score = 0
        left_syns = wn.synsets(left)
        right_syns = wn.synsets(right)
        if left_syns:
            score += .5
        if right_syns:
            score += .5
        if score > best_score:
            best = [x.name for x in left_syns], [x.name for x in right_syns]
            best_score = score
    return best


def normalize_string(string_or_sequence_of):
    """
    Splits a string or sequence of strings into a list of words split on spaces.
    """
    if isinstance(string_or_sequence_of, basestring):
        string = string_or_sequence_of.strip().lower()
        return re.split('([^a-z]+)', string)
    else:
        result = []
        for string in string_or_sequence_of:
            result.extend( normalize_string(string) )
        return result


def split_words(string):
    """
    Returns a set of multiple wordnet synsets.
    This assumes any sequence of letters is only at max two words.

    Examples:

        > list( split_words("noticeid") )
        ['notice', 'id']

        > list( split_words("org_contactemail") )
        ['org', 'contact', 'email']

        > list( split_words("contract_sequence_number") )
        ['contract', 'sequence', 'number']

        > list( split_words("contract sequence number") )
        ['contract', 'sequence', 'number']
    """
    results = set()
    for sub in normalize_string(string):
        ## If it's not a word, well we don't care about it.
        if not re.match('[a-z]+', sub):
            continue
        
        syns = wn.synsets(sub)
        
        ## If it is a word, yay!
        if syns:
            for x in syns:
                results.add( x.name )
        
        ## If it's not a word, but it's 3 or less letters it's probably not two words, so just yield that.
        elif len(sub) <= 3:
            results.add( sub )
        
        ## Otherwise let's try to split it into two words
        else:
            pair = find_two_words(sub)
            if pair:
                results.update( pair[0] )
                results.update( pair[1] )
            
            ## No dice, okay well let's just yield it
            else:
                results.add( sub )
    return results

def likeness(a, b):
    """
    Returns how alike words found in the list a and words found in the list b are.
    """
    a_set = split_words(a)
    b_set = split_words(b)
    union = a_set.union(b_set)
    intersection = a_set.intersection(b_set)
    return float(len(intersection)) / len(union)

def subsetness(a, b):
    """
    Returns how much a is in b as a coefficient, 0 - 1.
    
    0: a is not in b at all.
    1: all of the items in a are in b as well.
    """
    a_set = split_words(a)
    b_set = split_words(b)
    sz = len(a_set)
    hits = 0
    for obj in a_set:
        if obj in b_set:
            hits += 1
    return float(hits) / float(sz)
