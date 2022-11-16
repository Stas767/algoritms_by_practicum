def is_correct_bracket_seq(subsequence):

    while '{}' in subsequence or '[]' in subsequence or '()' in subsequence:
        subsequence = subsequence.replace('()', '')
        subsequence = subsequence.replace('[]', '')
        subsequence = subsequence.replace('{}', '')
    return not subsequence


def read_input():
    subsequence = str(input())
    return subsequence


if __name__ == '__main__':
    subsequence = read_input()
    print(is_correct_bracket_seq(subsequence))
