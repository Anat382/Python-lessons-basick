

print(1+1)

def main(argv):
    """
    read the file
    :param argv:
    :return:
    """
    program, *args = argv
    args = list(map(int, list(args)))
    path = 'bakery.csv'
    # print(args)
    count_ = 0
    with open(path, 'r', encoding='utf-8') as f:
        for elem in f:
            elem_ = elem.replace('\n', '')
            if args:
                if len(args) > 1 and (args[0] <= count_ <= args[-1]):
                    print(elem_)
                elif len(args) == 1 and count_ <= args[0]:
                    print(elem_)
            else:
                print(elem_)
            count_ += 1


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
