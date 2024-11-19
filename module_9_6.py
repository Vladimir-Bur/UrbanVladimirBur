from itertools import combinations

def all_variants(text):
    for n in range(1, len(text) + 1):
        for l in list(combinations(text, n)):
            yield "".join(l)

a = all_variants("abc")
for i in a:
    print(i)
