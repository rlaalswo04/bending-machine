# ; 프로그램 목적:
# ;     커피 자판기 프로그램 개발
# ; 기능:
# ;     1. 입력: 사용자가 선택, 출력: 커피를 출력(기본기능)
# ;     2. 금액체크
# ;     3. 남은재료 관리 or 몇잔 팔렸는지 관리
# ; 커피 종류: 
# ;     1.에스프레소
# ;     2.카페라테
# ;     3.아메리카노
# ;     4.초코라테

# 1. 입력받기
def user_coffee_input():
    user_coffee = input("커피종류를 입력해 주세요: ")
    return user_coffee

# # 2. 비즈니스 로직

is_coffee = True
if user_coffee == "에스프레소":
    print("에스프레소 한잔 제조 중")
elif user_coffee == "카페라떼":
    print("카페라떼 한잔 제조 중")
elif user_coffee == "아메리카노":
    print("아메리카노 한잔 제조 중")   
elif user_coffee == "초코라떼":
    print("초코라떼 한잔 제조 중")     
else:
    is_coffee = False
    print("커피의 종류가 없습니다")
    
# # 3. 출력
# if is_coffee == True:
#     print("음료제조가 완료되었습니다. 맛있게 드세요.")

user_coffee = user_coffee_input()
print(user_coffee) 