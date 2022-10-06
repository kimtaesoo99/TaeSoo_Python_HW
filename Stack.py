##함수 선언 부분##
def isStackFull() :   #스택이 꽉 찼는지 확인하는 함수
    global  SIZE, stack, top
    if(top>=SIZE-1):
        return True
    else:
        return False

def isStackEmpty() :   #스택이 비어있는지 확인하는 함수
    global SIZE,stack,top
    if(top==-1):
        return True
    else:
        return False

def push(data) :    #스택에 데이터를 삽입하는 함수
    global SIZE,stack ,top
    if(isStackFull()):
        print("스택이 꽉 찼습니다.")
        return
    top+=1
    stack[top] = data

def pop() :   #스택에서 데이터를 추출하는 함수
    global SIZE,stack,top
    if(isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top]=None
    top-=1
    return data

def peek():   #스택에서 top 위치의 데이터를 확인하는 함수
    global  SIZE,stack,top
    if(isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return stack[top]

##전역변수 선언 부분##
SIZE = int(input("스택 크기를 입력하세요==> "))
stack = [None for _ in range(SIZE)]
top=-1

##메인 코드 부분##
if __name__ =="__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X)중 하나를 선택==>")

    while(select!='X'and select !='x'):
        if select == 'I' or select =='i':
            data = input("입력할 데이터==>")
            push(data)
            print("스택 상태:",stack)
        elif select =='E' or select=='e':
            data=pop()
            print("추출된 데이터==>",data)
            print("스택 상태 :",stack)
        elif select =='V' or select=='v':
            data=peek()
            print("확인된 데이터==>",data)
            print("스택 상태 :",stack)
        else:
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X)중 하나를 선택==>")

    print("프로그램 종료!")