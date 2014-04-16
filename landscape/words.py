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

def split_words(string):
    """
    Generates lists of multiple wordnet synsets.
    This assumes any sequence of letters is only at max two words.
    If there is a space in it, we assume it's already split and just yield that.

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
    string = string.strip().lower()
    
    if ' ' in string:
        for obj in string.split():
            yield obj.lower()
    
    subs = re.split('([^a-z]+)', string.lower())
    for sub in subs:
        
        ## If it's not a word, well we don't care about it.
        if not re.match('[a-z]+', sub):
            continue
        
        ## If it is a word, yay!
        if is_word(sub):
            yield sub
        
        ## If it's not a word, but it's 3 or less letters it's probably not two words, so just yield that.
        elif len(sub) <= 3:
            yield sub
        
        ## Otherwise let's try to split it into two words
        else:
            pair = find_two_words(sub)
            if pair:
                yield pair[0]
                yield pair[1]
            
            ## No dice, okay well let's just yield it
            else:
                yield sub
