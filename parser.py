import re

#CFG REDUCTION RULES
rule1 = "E" #E -> E+T or E+T -> E
rule2 = "E" #E -> T or T-> E
rule3 = "T" #T ->T*F or T*F -> T
rule4 = "T" #T ->F or F-> T
rule5 = "F" #F -> (E) or (E) -> F
rule6 = "F" #F -> id or id -> F

#stack
stack = ['&','0']
#GETTING INPUT AND MAKING INTO TOKENS
input = input("Enter the string you want to parse: ")
items = [i for i in re.split(r'([`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]|\w+)',input) if i]
items.append('$')
#item index
i=0
#step counter
c=0


#PARSE TABLE
def state0(item):
    if  item == 'id':
        print("did state 0 for id")
        stack.append(item)
        stack.append("5")
    
    elif  item == '(':
        print("did state 0 for (")
        stack.append(item)
        stack.append('4')

    elif  item == 'E':
        print("did state 0 for E")
        stack.append('1')

    elif item == 'T':
        print("did state 0 for T")
        stack.append('2')

    elif item == 'F':
        print("did state 0 for F")
        stack.append('3') 
    
    else:
        print("NOT PARSABLE")
        quit()

def state1(item):
    if item == '+':
        print("did state 1 for +")
        stack.append(item)
        stack.append('6')
    
    elif item == "$":
        print("did state 1 for $")
        print("Accepted")
        quit()
    
    else:
        print('NOT PARSABLE\n')
        quit()

def state2(item,i):
    if item == '*':
        print("did state 2 for *")
        stack.append(item)
        stack.append('7')
        i=i
    elif item == '+' or ')' or '$':
        print("did reduction")
        stack.pop()
        stack.pop()
        stack.append(rule2)  
        i-=1          
    else:
        print('NOT PARSABEL\n')
        quit()

def state3(item,i):
    if item == '+' or '*' or ')' or '$':
        print("did reduction")
        stack.pop()
        stack.pop()
        stack.append(rule4)
        i-=1
    else:
        print('NOT PARSABLE\n')
        quit()

def state4(item):
    if item == 'id':
        print("did state 4 for id")
        stack.append(item)
        stack.append('5')
    elif item == '(':
        print("did state 4 for (")
        stack.append(item)
        stack.append('4')
    else:
        print('NOT PARSABEL\n')
        quit()

def state5(item,i):
    if item == '+' or '*' or ')' or '$':
        print("did reduction")
        stack.pop()
        stack.pop()
        stack.append(rule6)
        i-=1
    else:
        print('NOT PARSABLE\n')
        quit()

def state6(item):
    if item =='id':
        print("did state 6 for id")
        stack.append(item)
        stack.append('5')
    elif item == '(':
        print("did state 6 for (")
        stack.append(item)
        stack.append('4')
    else:
        print('NOT PARSABEL\n')
        quit()

def state7(item):
    if item =='id':
        print("did state 7 for id")
        stack.append(item)
        stack.append('5')
    elif item == '(':
        print("did state 7 for (")
        stack.append(item)
        stack.append('4')
    else:
        print('NOT PARSABLE\n')
        quit()

def state8(item):
    if item == '+':
        print("did state 8 for +")
        stack.append(item)
        stack.append('6')
    elif item == ')':
        print("did state 8 for )")
        stack.append(item)
        stack.append('11')
    else:
        print('NOT PARSABLE\n')
        quit()

def state9(item,i):
    if item == '+'or ')' or '$':
        print("did reduction")
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(rule1)
        i-=1
        
    elif item == '*':
        print("did state 0 for *")
        stack.append(item)
        stack.append('7')
    else:
        print('NOT PARSABLE\n')
        quit()

def state10(item,i):
    if item == '+'or '*' or ')' or '$':
        print("did reduction")
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(rule3)
        i-=1
    else:
        print('NOT PARSABLE\n')
        quit()

def state11(item,i):
    if item == '+'or '*' or ')' or '$':
        print("did reduction")
        i-=1
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append(rule5)
    else:
        print('NOT PARSABLE\n')
        quit()
#MAIN BODY
print('Input we are working with: ', input)
while(i < len(items)):
    print('step ',c)
    print('Currently working with: ',items[i])
    print('current stack: ',stack)
    if stack[len(stack)-1] == '0':
        state0(items[i])
    elif stack[len(stack)-1] == '1':
        state1(items[i])
    elif stack[len(stack)-1] == '2':
        state2(items[i],i)
    elif stack[len(stack)-1] == '3':
        state3(items[i],i)
    elif stack[len(stack)-1] == '4':
        state4(items[i])
    elif stack[len(stack)-1] == '5':
        state5(items[i],i)
    elif stack[len(stack)-1] == '6':
        state6(items[i])
    elif stack[len(stack)-1] == '7':
        state7(items[i])
    elif stack[len(stack)-1] == '8':
        state8(items[i])
    elif stack[len(stack)-1] == '9':
        state9(items[i],i)
    elif stack[len(stack)-1] == '10':
        state10(items[i],i)
    elif stack[len(stack)-1] == '11':
        state11(items[i],i)
    
    if stack[len(stack)-1] == 'E':
        i-=1
        print('looked left')
        if stack[len(stack)-2] =='0':
            stack.append('1')
            
        elif stack[len(stack)-2] == '4':
            stack.append('8')
        else:
            print('The input is not parsable')

    elif stack[len(stack)-1] == 'T':
        i-=1
        print('looked left')
        if stack[len(stack)-2] == '0':
            stack.append('2')
        elif stack[len(stack)-2] == '4':
            stack.append('2')
        elif stack[len(stack)-2] == '6':
            stack.append('9')
        else:
            print('Input is not parsable')

    elif stack[len(stack)-1] == 'F':
        i-=1
        print('looked left')
        if stack[len(stack)-2] == '0':
            stack.append('3')
        elif stack[len(stack)-2] == '4':
            stack.append('3')
        elif stack[len(stack)-2] == '6':
            stack.append('3')
        elif stack[len(stack)-2] == '7':
            stack.append('10')
        else:
            print('input not parsable')

    i+=1
    c+=1


