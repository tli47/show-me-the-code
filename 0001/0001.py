__author__ = 'tli47'

import random, string

ALL_LETTERS = string.ascii_lowercase + string.digits
codeAmount = 200
codeRound = 10
codeResult = []

while len(codeResult) != codeAmount:
    everyCode = ''.join((random.choice(ALL_LETTERS) for i in range(codeRound)))
    if everyCode not in codeResult:
        codeResult.append(everyCode)

print(len(codeResult))
print(codeResult)