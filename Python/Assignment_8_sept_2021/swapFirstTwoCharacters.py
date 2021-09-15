def swapFirstTwoCharacters(a, b):
  str1 = b[:2] + a[2:]
  str2 = a[:2] + b[2:]

  return str1 + ' ' + str2

str1 = input("Enter string 1 : ")

str2 = input("Enter string 2 : ")
print(swapFirstTwoCharacters(str1, str2))