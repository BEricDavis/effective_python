# Python 3 bytes: raw 8-bt values
# Python 3 str: Unicode characters

def to_str(input):
    """
    Given a bytes or str value, avalue = inputlways return a str
    :param input: bytes or str value
    :return: str
    """
    if isinstance(input, bytes):
        value = input.decode('utf-8')
    else:
        value = input
    return value # instance of str

def to_bytes(input):
    """
    Given a bytes or str value, always return a bytes value
    :param input: bytes or str value
    :return: bytes
    """
    if isinstance(input, str):
        value = input.encode('utf-8')
    else:
        value = input
    return value # instance of str


if __name__ == '__main__':
    some_str_text = 'Some str Text'
    some_bytes_text = b'Some bytes Text'
    print(f'* Given this text:')
    print (f"'some_str_text' is a {type(some_str_text)}")
    print (f"'some_bytes_text' is a {type(some_bytes_text)}")

    print('* Return string every time')
    print(to_str(some_str_text))
    print(to_str(some_bytes_text))

    print('* Return bytes every time')
    print(to_bytes(some_str_text))
    print(to_bytes(some_bytes_text))

    print('* bytes and strs cannot be mixed')
    try:
        print(some_str_text + some_bytes_text)
    except Exception as e:
        print(e)

    print('* bytes and bytes or strs and strs though, that\'s cool')
    try:
        print(to_bytes(some_str_text) + some_bytes_text)
        print(some_str_text + to_str(some_bytes_text))
    except Exception as e:
        print(e)
