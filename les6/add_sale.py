import os.path


def main(argv):
    """
    write to the file
    :param argv:
    :return:
    """
    program, *args = argv
    args = list(args)[0] + '\n'
    path = 'bakery.csv'
    # print(args)
    open(path, 'w', encoding='utf-8').close() if os.path.exists(path) is False else None

    with open(path, 'a', encoding='utf-8') as f:
        f.write(args)


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
