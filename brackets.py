# encoding:utf-8

bracketString = list("([])")

def function1():
    lenString = len(bracketString)
    valid = True
    for index, stringitem in enumerate(bracketString):
        if stringitem == "(":
            if bracketString[lenString - 1 - index] != ")":
                valid = False
            elif bracketString[lenString - 1 - index] == ")":
                bracketString.pop(bracketString[lenString - 1 - index])
        if stringitem == "[":
            if bracketString[lenString - 1 - index] != "]":
                valid = False
            elif bracketString[lenString - 1 - index] == "]":
                bracketString.pop(bracketString[lenString - 1 - index])
        if stringitem == "{":
            if bracketString[lenString - 1 - index] != "}":
                valid = False
            elif bracketString[lenString - 1 - index] == "}":
                bracketString.pop(bracketString[lenString - 1 - index])
    return valid

print(function1())
