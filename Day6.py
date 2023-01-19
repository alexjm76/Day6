# def document_it(func):
#     def new_function(*args, **kwargs):
#         print("Running function: ",func.__name__) #함수의 이름 리턴
#         print("Positional arguments: ", args)  #튜플출력
#         print("Keyword arguments:" kwargs)  #딕셔너리 출력
#         result = func(*args, **kwargs)
#         print("Result:" ,result)
#         return result
#     return new_function()


@document_it
def add_ints(a,b):
    return  a+b

add_ints(3,5)  #기존의 함수를 건들이지 않으면서 수정하고 싶을때 decorator 사용