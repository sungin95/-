from django.shortcuts import render
import sys
sys.stdin = open("view.txt", encoding="UTF-8")


def index():
    food_list = list(input().split())
    # food_list = request
    receipe = {
        "김치찌개": ['돼지고기', '고추가루', '두부'],
        "된장찌개": ['돼지고기', '고추가루', '두부', '된장'],
        "김밥": ['김', '밥', '단무지', '햄', '계란', '우엉', '시금치'],
        "제육볶음": ['돼지고기', '고추가루', '간장', '설탕', '마늘', '양파', '대파'],
        "두부김치": ['돼지고기', '두부', '고추가루', '김치', '양파', '간장', '설탕', '마늘', '소금'],
    }
    recipe = []
    can_make_food = []
    for fo in receipe.items():
        O = []
        X = []
        check = False
        check2 = False
        print(fo[0])
        # 구분
        for i in range(len(fo[1])):
            if fo[1][i] in food_list:
                O.append(fo[1][i])
            else:
                X.append(fo[1][i])
        # print
        if X == [] and O != []:
            print("이 음식은 만들 수 있습니다.")
            can_make_food.append(fo[0])
            check = True
        if O == []:
            check2 = True
            print("이 음식은 있는 재료가 없습니다.")

        if check2 == False:
            print("있는 재료")
            for o in O:
                print(o, end=" ")
            print()
        if check == False:
            print("없는 재료")
            for x in X:
                print(x, end=" ")
            print()
        context = {
            '현재 가지고 있는 재료(처음 입력)': [],
            '레시피': {'있는 재료': [], '없는 재료': [], },
            '만들 수 있는 음식': [],
        }
        return
        # return render(request, 'index.html')


index()
