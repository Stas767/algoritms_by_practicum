def sub(s, t):
    idx = -1

    for i in s:
        idx = t.find(i, idx + 1)
        if idx == -1:
            return False

    return True


def main():
    s, t = input(), input()
    print(sub(s, t))


if __name__ == '__main__':
    main()
