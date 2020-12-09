from stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

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
print(baseConverter(25, 16))
print(baseConverter(16,16)) # 10
print(baseConverter(10,16)) # A
print("\n")
print(baseConverter(25,8)) # 31
print(baseConverter(256, 16)) # 100
print(baseConverter(100,6)) # 244
print(baseConverter(100,16)) # 64, not 256 - Q4
print(baseConverter(100,4)) #
