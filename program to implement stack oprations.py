def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False


def Push(stk,item):
    stk.append(item)
    top=len(stk)-1


def Pop(stk):
    if isEmpty(stk):
        return "UnderFlow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk) -1
        return item


def Peek(stk):
    if isEmpty(stk):
        return "UnderFlow"
    else:
        top=len(stk)-1
        return stk[top]

def Display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
#__main__
Stack=[]
top=None
while True:
    print("Stack Oprations")
    print("For Push Enter 1")
    print("For Pop Enter 2")
    print("For Peek Enter 3")
    print("For Display Stack Enter 4")
    print("For Exit Enter 5")
    ch=int(input("Enter Your Choice Between 1 to 5 :"))
    if ch==1:
        item=int(input("Enter Item :"))
        Push(Stack,item)
    elif ch==2:
        item=Pop(Stack)
        if item == "UnderFlow":
            print("UnderFlow!!! Stack is Empty!")
        else:
            print("Popped Item is ",item)
    elif ch==3:
        item=Peek(Stack)
        if item=="UnderFlow":
            print("UnderFlow! Stack is Empty!")
        else:
            print("Topmost item is ",item)
    elif ch==4:
        Display(Stack)
    elif ch==5:
        break
    else:
        print("Invalid Choice!")