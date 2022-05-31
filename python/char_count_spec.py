# Can you translate this driver code to unit tests?

from char_count import char_count

print(char_count("aaabbc") == {
  'a': 3,
  'b': 2,
  'c': 1,
  })

print(char_count("an apple a day will keep the doctor away") == {
  'a': 6, 
  'n': 1,
  'p': 3,
  'l': 3,
  'e': 4,
  'd': 2,
  'y': 2,
  'w': 2,
  'i': 1,
  'k': 1,
  't': 2,
  'h': 1,
  'o': 2,
  'c': 1,
  'r': 1
  })
