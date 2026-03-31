message = '나는야 전역 변수'
print(message)

def no_secret():
    global message
    message = '이러면 또 지역변수'
    print(message)

no_secret()


x=3
def add():
    x= 6
    x+=3
add()
print(x)