def shift_zeroes(l: list[int]):
    """ Shift all non-zeros left, in place"""
    cursor = 0
    for i in range(len(l)):
        if l[i] != 0:
            if i != cursor:
                l[cursor] = l[i]
            cursor += 1
    l[cursor:] = [0] * (len(l) - cursor)

if __name__ == "__main__":
    asd = [1,2,3]
    asd2 = [1,0,2,3,0,0,5]
    shift_zeroes(asd)
    shift_zeroes(asd2)
    print(asd)
    print(asd2)
