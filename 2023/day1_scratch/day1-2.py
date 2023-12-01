s = 0

terms = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for l in open("input").readlines():
    first_digit = None
    for i in range(len(l)):
        if l[i] in "01233456789":
            first_digit = int(l[i])
            break
        for term, d in terms.items():
            # print(l[i:], l[i:].startswith(term))
            if l[i:].startswith(term):
                first_digit = d
                break
        if first_digit is not None:
            break

    last_digit = None
    for i in range(len(l) - 1, -1, -1):
        if l[i] in "01233456789":
            last_digit = int(l[i])
            break
        for term, d in terms.items():
            if l[:i].endswith(term):
                last_digit = d
                break
        if last_digit is not None:
            break

    s += first_digit * 10 + last_digit

print(s)
