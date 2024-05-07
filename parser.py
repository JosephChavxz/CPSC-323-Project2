import re

#CFG REDUCTION RULES
rule1 = "E"
rule2 = "E"
rule3 = "T"
rule4 = "T"
rule5 = "F"
rule6 = "F"

#stack
stack = ['&','0']
#GETTING INPUT AND MAKING INTO TOKENS
input = input("Enter the string you want to parse: ")
items = [i for i in re.split(r'([`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]|\w+)',input) if i]
items.append('$')

#PARSE TABLE
def state0(item):
    if  item == 'id':
        print("did rule 0\n")
        stack.append(item)
        stack.append("5")
    
    elif  item == '(':
        print("did rule 0\n")
        stack.append(item)
        stack.append('4')

    elif  item == 'E':
        print("did rule 0\n")
        stack.append('1')

    elif item == 'T':
        print("did rule 0\n")
        stack.append('2')

    elif item == 'F':
        print("did rule 0\n")
        stack.append('3') 
    
    else:
        print("NOT PARSABLE\n")

def state1(item):
    if item == '+':
        print("did rule 1\n")
        stack.append(item)
        stack.append('6')
    
    elif item == "$":
        print("did rule 1\n")
        print("accepted")
    
    else:
        print('NOT PARSABLE\n')

def state2(item):
    if item == '+' or ')' or '$':
        print("did rule 2\n")
        stack.pop()
        stack.pop()
        stack.append(rule2)            
    elif item == '*':
        print("did rule 2\n")
        stack.append(item)
        stack.append('7')
    else:
        print('NOT PARSABEL\n')

def state3(item):
    if item == '+' or '*' or ')' or '$':
        print("did rule 3\n")
        stack.pop()
        stack.pop()
        stack.append(rule4)
    else:
        print('NOT PARSABLE\n')

def state4(item):
    if item == 'id':
        print("did rule 4\n")
        stack.append(item)
        stack.append('5')
    elif item == '(':
        print("did rule 4\n")
        stack.append(item)
        stack.append('4')
    elif item == 'E':
        print("did rule 4\n")
        stack.append('8')
    elif item == 'T':
        print("did rule 4\n")
        stack.append('2')
    elif item == 'F':
        print("did rule 4\n")
        stack.append('3')
    else:
        print('NOT PARSABEL\n')

def state5(item):
    if item == '+' or '*' or ')' or '$':
        print("did rule 5\n")
        stack.pop()
        stack.pop()
        stack.append(rule6)
    else:
        print('NOT PARSABLE\n')

def state6(item):
    if item =='id':
        print("did rule 6\n")
        stack.append(item)
        stack.append('5')
    elif item == '(':
        print("did rule 6\n")
        stack.append(item)
        stack.append('4')
    elif item == 'T':
        print("did rule 6\n")
        stack.append('9')
    elif item == 'F':
        print("did rule 6\n")
        stack.append('3')
    else:
        print('NOT PARSABEL\n')

def state7(item):
    if item =='id':
        print("did rule 7\n")
        stack.append(item)
        stack.append('5')
    elif item == '(':
        print("did rule 7\n")
        stack.append(item)
        stack.append('4')
    elif item == 'F':
        print("did rule 7\n")
        stack.append('10')
    else:
        print('NOT PARSABLE\n')

def state8(item):
    if item == '+':
        print("did rule 8\n")
        stack.append(item)
        stack.append('6')
    elif item == ')':
        print("did rule 8\n")
        stack.append(item)
        stack.append('11')
    else:
        print('NOT PARSABLE\n')

def state9(item):
    if item == '+'or ')' or '$':
        print("did rule 9\n")
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(rule1)
    elif item == '*':
        print("did rule 0\n")
        stack.append(item)
        stack.append('7')
    else:
        print('NOT PARSABLE\n')

def state10(item):
    if item == '+'or '*' or ')' or '$':
        print("did rule 10\n")
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(rule3)
    else:
        print('NOT PARSABLE\n')

def state11(item):
    if item == '+'or '*' or ')' or '$':
        print("did rule 11\n")

        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(rule5)
    else:
        print('NOT PARSABLE\n')

#MAIN BODY
i=0
while(i < len(items)):
    
    if stack[len(stack)-1] == '0':
        state0(items[i])
    elif stack[len(stack)-1] == '1':
        state1(items[i])
    elif stack[len(stack)-1] == '2':
        state2(items[i])
    elif stack[len(stack)-1] == '3':
        state2(items[i])
    elif stack[len(stack)-1] == '4':
        state4(items[i])
    elif stack[len(stack)-1] == '5':
        state5(items[i])
    elif stack[len(stack)-1] == '6':
        state6(items[i])
    elif stack[len(stack)-1] == '7':
        state7(items[i])
    elif stack[len(stack)-1] == '8':
        state8(items[i])
    elif stack[len(stack)-1] == '9':
        state9(items[i])
    elif stack[len(stack)-1] == '10':
        state10(items[i])
    elif stack[len(stack)-1] == '11':
        state11(items[i])
    elif stack[len(stack)-1] == 'E':
        if stack[len(stack)-2] =='0':
            stack.append('1')
            i-=1
        elif stack[len(stack)-2] == '4':
            stack.append('8')
            i-=1
        else:
            print('The input is not parsable')
    elif stack[len(stack)-1] == 'T':
        if stack[len(stack)-2] == '0':
            stack.append('2')
            i-=1
        elif stack[len(stack)-2] == '4':
            stack.append('2')
            i-=1
        else:
            print('Input is not parsable')
    elif stack[len(stack)-1] == 'F':
        if stack[len(stack)-2] == '0':
            stack.append('3')
            i-=1
        elif stack[len(stack)-2] == '4':
            stack.append('3')
            i-=1
        elif stack[len(stack)-2] == '6':
            stack.append('3')
            i-=1
        elif stack[len(stack)-2] == '7':
            stack.append('10')
            i-=1
    else:
        print('input is not parsable')
    i+=1

print(stack)