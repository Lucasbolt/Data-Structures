def add_at_the(x, l):
    return [x+ element for element in l]
def bitString(n):
    if n == 0: return []
    if n == 1: return ['0', '1']
    else:
        return (add_at_the('0', bitString(n-1)) + add_at_the('1', bitString(n-1)))

print(bitString(4))