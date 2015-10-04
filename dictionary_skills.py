# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    word_counts = {}

    #make string into a list of words
    words = input_string.split()

    for word in words:
        # add word to dict if it's the first time it appears in the string
        #set the value equal to 1
        if word not in word_counts:
            word_counts[word] = 1

        #increase value of existing word by 1
        else:
            word_counts[word] += 1

    return word_counts

count_unique("rose is a rose is a rose")


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    pass

############################################################################
# Lavinia! Can we go over this? I found the instructions super unclear.
# They say: "If an item appears more than once in at least one list and is present
# # in both lists, return it each time" and then gives this an an example:
# >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
#         [1, 1, 2, 2]
# However, shouldn't python return [1, 1, 1, 2, 2, 2]?

find_common_items([1, 2, 3, 4], [1, 1, 2, 2])


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    list_dictionary = {}

    #turn given lists into one big list
    list1.extend(list2)

    combined_list = list1

    for i in combined_list:
        # add item to dict if it's the first time it appears in the list
        #set the value (count) equal to 1
        if i not in list_dictionary:
            list_dictionary[i] = 1
        else:
             #increase value (count) of existing word by 1
            list_dictionary[i] += 1
    return list_dictionary

    common_list = []

    for i in list_dictionary:
        #determines if list item appears more than once
        #if yes, appends to a list of common items
        if list_dictionary[i] > 1:
            common_list.append(i)
    return common_list

find_unique_common_items([1, 2, 3, 4], [1, 2])


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # convert list to a set to remove duplicates
    set_list = set(input_list)

    zero_pairs = []

    for i in set_list:
        #in order for a pair of numbers to equal zero, they must be a postive
        #integer and its negative equivalent
        # this loop determines if that condition is met
        #then, if yes, the number pair is appended to a list of total zero pairs
        if i*-1 in set_list and i > 0:
            zero_pairs.append([i, i*-1])
        elif i == 0:
            zero_pairs.append([i, i])
    return zero_pairs

get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0])


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    individual_words = {}

    for word in words:
        #creates a dictionary of words, with the number of times each word
        #appears in the given list of words
        if word not in individual_words:
            individual_words[word] = 1
        else:
            individual_words[word] += 1

    #returns a list of each individual word in the given list
    return individual_words.keys()

remove_duplicates(["Rose", "is", "a", "rose", "is", "a", "rose"])


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    encoded_dict = {'e': 'p', 'a': 'd', 't': 'o', 'i': 'u'}

    encoded_phrase = ''

    for char in phrase:
        # determines if character has an encoded equivalent
        #if yes, appends the encoded equivalent to the encoded phrase string
        #if no, appends the regular character to the encoded phrase string
        if char in encoded_dict:
            encoded_phrase += encoded_dict[char]
        else:
            encoded_phrase += char
    return encoded_phrase

encode("You are a beautiful, talented, brilliant, powerful musk ox.")


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    word_length_dict = {}

    for word in words:
        #for a given list of words, find the length of each word
        #create new dict pair: word length=key, word=value (in a list)
        # if word length already a key, append the word to the value list 
        word_length = len(word)
        if word_length in word_length_dict:
            word_length_dict[word_length].append(word)
        else:
            word_length_dict[word_length] = [word]

    return word_length_dict.items()

sort_by_word_length(["ok", "an", "apple", "a", "day"])


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    english = ['sir', 'hotel', 'student', 'boy', 'madam', 'professor',
               'restaurant', 'your', 'excuse', 'students', 'are', 'lawyer',
               'the', 'restroom', 'my', 'hello', 'is', 'man']

    pirate = ['matey', 'fleabag inn', 'swabbie', 'matey', 'proud beauty',
              'foul blaggart', 'galley', 'yer', 'arr', 'swabbies', 'be',
              'foul blaggart', 'th\'', 'head', 'me', 'avast', 'be', 'matey']

    #convert string to list of words
    workable_phrase = phrase.split()

    translation_dict = {}

    translation = ''

    #make table in a dictionary
    #english word is the key, pirate word is the value
    for i in range(len(english)):
        translation_dict[english[i]] = pirate[i]
    
    #determins if english word has a pirate equivalent
    #if yes, adds pirate equivalent to translation
    #if no, adds english word to translation
    for word in workable_phrase:
        if word in translation_dict.keys():
            translated_word = translation_dict[word]
        else:
            translated_word = word
        translation += ' ' + translated_word

    return translation

get_pirate_talk("my student is not a man")

# # End of skills. See below for advanced problems.
# # To work on them, set ADVANCED=True at the top of this file.
# ############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    letter_counts = {}

    #creates dictionary of letters (keys) and their frequencies (values) 
    for char in input_string.lower():
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1

    #takes a list of letter frequencies, and find the highest value
    highest_number = max(letter_counts.values())

    top_letter_list = []

    #if a letter(key) has the highest number of frequencies, append to a list
    # of top letters
    for key in letter_counts:
        if letter_counts[key] == highest_number:
            top_letter_list.append(key)
    return top_letter_list

adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    word_length_dict = {}

    for word in words:
        #for a given list of words, find the length of each word
        #create new dict pair: word length=key, word=value (in a list)
        # if word length already a key, append the word to the value list 
        word_length = len(word)
        if word_length in word_length_dict:
            word_length_dict[word_length].append(word)
        else:
            word_length_dict[word_length] = [word]

    #takes dict values (which are lists) and sorts them
    for key in word_length_dict:
            word_length_dict[key].sort()

    return word_length_dict.items()

adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])


# ##############################################################################
# # You can ignore everything below this.

# def print_dict(d):
#     # This method is just used to print dictionaries in key-alphabetical
#     # order, and is only used for our documentation tests. You can ignore it.
#     if isinstance(d, dict):
#         print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
#     else:
#         print d


# def sort_pairs(l):
#     # Print sorted list of pairs where the pairs are sorted. This is used only
#     # for documentation tests. You can ignore it.
#     return sorted(sorted(pair) for pair in l)

# if __name__ == "__main__":
#     print
#     import doctest
#     for k, v in globals().items():
#         if k[0].isalpha():
#             if k.startswith('adv_') and not ADVANCED:
#                 continue
#             a = doctest.run_docstring_examples(v, globals(), name=k)
#     print "** END OF TEST OUTPUT"
#     print
