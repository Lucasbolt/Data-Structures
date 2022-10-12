def my_sort(a, b, c):
    items = [a, b, c]
    output = []
    comp = a
    if comp > b:
        comp = b
        if comp > c:
            comp = c
    output.append(comp)
    items.remove(comp)
    if items[0] > items[1]:
        output.append(items[1])
        output.append(items[0])
    else:
        output.append(items[0])
        output.append(items[1])
    print(output)

if __name__ == "__main__":
    from time import time
    start_time = time()
    my_sort(80, 1, 99)
    end_time = time()
    print(end_time - start_time)