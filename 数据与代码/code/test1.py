def test(n):
    if n==1:
        return 1
    if n==2:
        return 2

    return test(n-1)+test(n-2)


if __name__ == '__main__':
    res = test(5)
    print(res)