substrings = input().split(", ")

words = input().split(", ")

occ_substring = [substr for substr in substrings for word in words if substr in words]

print(sorted(set(occ_substring), key=occ_substring.index))
