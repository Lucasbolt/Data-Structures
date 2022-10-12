#this program is a recursive function for sorting arrays/list.

array_list = []
def array_sort(args):
    while args:
        a = min(args)
        array_list.append(a)
        args.remove(a)
        array_sort(args)
    return array_list


if __name__ == "__main__":
    print(array_sort(['boy', 'apple', 'cider', 'elephant', 'dog']))
    