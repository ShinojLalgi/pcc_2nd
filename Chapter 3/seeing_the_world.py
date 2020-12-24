places = ['delhi', 'paris', 'chennai', 'kochi', 'tokyo']

print("Original list:")
print(places)

print("\nTemporarily sorted list:")
print(sorted(places))

print("\nOriginal list:")
print(places)

print("\nTemporarily sorted list (Reverse):")
print(sorted(places, reverse=True))

print("\nOriginal list:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nReversed again list:")
print(places)

places.sort()
print("\nSorted list")
print(places)

places.sort(reverse=True)
print("\nSorted list")
print(places)
