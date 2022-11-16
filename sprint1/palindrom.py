import string


def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    for word in line:
        if word in string.punctuation:
            line = line.replace(word, '')
    text = line.upper()
    if text == text[::-1]:
        return True
    return False


print(is_palindrome(''.join(input().strip().split())))
