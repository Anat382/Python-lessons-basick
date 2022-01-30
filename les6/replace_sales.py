
def main(argv):
    """
    replace number
    arg 1: index
    arg 2: new number
    :param argv:
    :return:
    """
    program, *args = argv
    args = list(map(lambda x: float(x.replace(',', '.')), list(args)))
    path = 'bakery.csv'
    # print(args)
    ind = int(args[0])
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.replace('\n', ''), lines))

    if len(args) == 2:
        if args[0] <= len(lines):
            lines[ind] = args[1] if args[1]  else 0
            lines = list(map(lambda x: f'{x}\n', lines))
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        else:
            return 'Индекса не существуюет укажите занчение меньше !!!'
    else:
        return 'Не введены параметры !!!'


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
