# based on video


from stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRS"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

        newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(27423,26)) # string index out of range
