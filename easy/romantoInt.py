nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman = list("LXXXIV")
negs = ["I", "X", "C"]
number = 0
l = len(roman)
for i in range(len(roman)):
    letter=roman[i]
    if i+1==l:
        number += nums.get(letter, 0)
    else:
        if letter in negs and  (nums.get(letter, 0)< nums.get(roman[i + 1]) ) :

            number -= nums.get(letter, 0)
        else:
            number += nums.get(letter, 0)
