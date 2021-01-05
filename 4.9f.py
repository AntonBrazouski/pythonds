# q-5

from stack import Stack

# new
def fixError(astring):
    newstr = ""
    is_space_place = False

    for token in astring:
        if token != ' ':
            if is_space_place == False:
                newstr = newstr + token
                is_space_place = True
            else:
                newstr = newstr + ' '
                newstr = newstr + token
                is_space_place = True
    return newstr

def infixToPostfix(infixexpr):
    prec = {}

    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []

    infixexpr = fixError(infixexpr) # new

    tokenList = infixexpr.split()

    for token in tokenList:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

        #print(f"token = {token} -- postfixList = {postfixList} -- opStack = {opStack}")

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

print(infixToPostfix("(A + B ) * C - ( D - E ) * ( F + G )")) # intentional error
print(infixToPostfix("5 * 3 ^ (4 - 2)")) # Q-5
