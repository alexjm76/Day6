try:
    #raise Exception("쉬는 시간")
    raise TypeError("타입 에러")
    expr = input("분자 분모 입력 : ").split()
    print(int(expr[0])/int(expr[1]))


except ValueError as err:
     print(f"숫자를 입력해주세요({err})")
except ZeroDivisionError as err:
    print(f"분모에 0이 올수 없습니다.({err})")
except IndexError:
    print("범위에 문제")
except:
    print("예외 발생!")
else: #예외가 발생하지 않았을 때
    print("프로그램 정상", end =' ') #줄바꿈 x
finally: #예외 발생여부와 상관 없이 무조건 실행
    print("종료")


# def div_calc(first, second):
#     """
#     나누기 함수
#     :param fist:  분자
#     :param second:  분모
#     :return: 계산 결과
#     """
#     return first / second
# print(div_calc(15,3))
# print(div_calc(15,0))