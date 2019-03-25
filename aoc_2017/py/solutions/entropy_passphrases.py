import sys


def is_valid_passphrase(input_str):
    words_dict = {}
    for word in input_str.split():
        if not words_dict.get(word):
            words_dict[word] = 1
        else:
            return False
    return True


def is_anagram(a, b):
    """ Increment each letter in the first go & decrement each letters count in the second pass,
        If one of the letter's count is not Zero, then the letter is missing from either one of
        the words. Not an anagram. If the final count for all chars is zero then its an anagram"""
    letter_dicts = {}
    for char in a:
        letter_dicts[char] = 1 + letter_dicts.get(char, 0)
    for char in b:
        letter_dicts[char] = letter_dicts.get(char, 0) - 1
    for char in letter_dicts:
        if letter_dicts[char] != 0:
            return False
    return True


def no_anagrams_in_passphrase(input_str):
    all_words = input_str.split()
    for i in range(len(all_words)):
        for j in range(len(all_words)):
            if i != j and is_anagram(all_words[i], all_words[j]):
                return False
    return True


def solve_part_one(input_file_path):
    count = 0
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            # remove leading and trailing whitespace chars
            stripped_line = line.strip()
            # convert all numbers to int
            if is_valid_passphrase(stripped_line):
                count += 1
    return count


def solve_part_two(input_file_path):
    count = 0
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            # remove leading and trailing whitespace chars
            stripped_line = line.strip()
            # convert all numbers to int
            if no_anagrams_in_passphrase(stripped_line):
                count += 1
    return count


if __name__ == '__main__':
    input_file_path = './inputs/entropy_passphrases/test2.txt'
    result = 0

    if len(sys.argv) < 2 or (sys.argv[1] != 'one' and sys.argv[1] != 'two'):
        print "Run step one or two ? Usage : python -m solutions.entropy_passphrases <one|two>"
        sys.exit(0)

    if sys.argv[1] == 'one':
        result = solve_part_one(input_file_path)
    else:
        result = solve_part_two(input_file_path)

    print 'Result is', result
