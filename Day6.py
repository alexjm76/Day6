
def document_info(func):
    def new_function(*args, **kwargs):
        print("Running function: " ,func.__name__)  # 함수의 이름 리턴
        print("Positional arguments: ", args)  # 튜플출력
        print("Keyword arguments:", kwargs)  # 딕셔너리 출력
        result = func(*args, **kwargs)
        print("Result:" ,result)
        return result

    return new_function()


@document_info
def sub_int(x, y):
    return x - y


@document_info
def squares(n):
    return n * n


print(sub_int(7, 3))
print(squares5
)