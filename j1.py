def longest(sen):
    l = sen.strip().split()
    a = l[0]
    for x in l:
        if len(x) > len(a):
            a = x
    return a
