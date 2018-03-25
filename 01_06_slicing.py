def main():
    theList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    print(f'theList = {theList}')
    print('slice with only start: theList[3:]')
    print(theList[3:])
    print('slice with only end: theList[:3]')
    print(theList[:3])
    print('slice with start and stop: theList[3:6]')
    print(theList[3:6])
    print('slice with only stride: theList[::3]')
    print(theList[::3])
    print('slice with negative stride: theList[::-3]')
    print(theList[::-3])
    print('slice with start, end, and stride is confusing')
    print('theList[2:6:2]')
    print(theList[2:6:2])

    print('theList[6:1:-2]')
    print(theList[6:1:-2])

    print('theList[6::-2]')
    print(theList[6::-2])

    print('theList[2::-2]')
    print(theList[2::-2])

    print('Slice a string')
    print("'python'[::-2]")
    print('python'[::-2])
    print()
    print('Slice some bytes')
    print("b'python'[:4]")
    print(b'python'[:4])
    print()

    print('Slicing multibyte unicode is tricky')
    jp = '\u3041\u3080'
    print("jp == '\\u3041\\u3080'")
    print("jp == '\u3041\u3080'")

    jp_utf = jp.encode('utf-8')
    print("jp_utf == jp.encode('utf-8')")
    print(jp_utf)

    print('reverse_jp_utf = jp_utf[::-1]')
    reverse_jp_utf = jp_utf[::-1]
    print(reverse_jp_utf)
    print("reverse_jp_utf.decode('utf-8')")
    try:
        print(reverse_jp_utf.decode('utf-8'))
    except Exception as e:
        print(e)


    print()
    print('prefer to slice to a new list and then stride')
    print('a = theList[2:8]')
    a = theList[2:8]
    print(f"a == {a}")
    print('b = a[::-2]')
    b = a[::-2]
    print(f"b == {b}")


if __name__ == '__main__':
    main()