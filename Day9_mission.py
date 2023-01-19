# while True:
#     try:
#         x= int(input("아무거나 입력해: "))
#         break
#     except OopsException






class OopsError(Exception):
    pass

def Oops():
    a=input('아무거나 입력 ')
    if len(a)<10:
        raise OopsError("Caught and oops")


try:
    Oops()
except OopsError as i:
    print('오류발생!', i)
