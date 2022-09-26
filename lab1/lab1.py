import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except:
        while True:
            print(prompt)
            coef_str = input()
            try:
                coef = float(coef_str)
                break
            except:
                print('Ошибка')
    return coef


def main():
    a = get_coef(1, 'Введите коэффициент A:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    if a == 0 and b == 0:
        if c == 0:
            print('Бесконечное количество корней')
        else:
            print('Нет корней')
    elif a == 0 and b != 0:
        if c == 0:
            print('Один корень: 0')
        elif -c / b > 0:
            print(f'Два корня: {-math.sqrt(-c/b)} {math.sqrt(-c/b)}')
        elif -c / b == 0:
            print('Один корень: 0')
        else:
            print('Нет корней')
    elif a != 0 and b == 0:
        if c==0:
            print('Один корень: 0')
        elif -c / a > 0:
            print(f'Два корня: {-math.sqrt(math.sqrt(-c / a))} {math.sqrt(math.sqrt(-c / a))}')
        else:
            print('Нет корней')
    elif a != 0 and b != 0:
        if c == 0:
            if - b / a > 0:
                print(f'Два корня: 0 {-math.sqrt(- b / a)} {math.sqrt(- b / a)}')
            else:
                print('Один корень: 0')
        else:
            D = b**2 - 4 * a * c
            if D > 0:
                D = math.sqrt(D)
                c1 = (-b - D)/(2*a)
                c2 = (-b + D)/(2*a)
                if c1 > 0 and c2 > 0:
                    print(f'Четыре корня: {-math.sqrt(c1)} {math.sqrt(c1)} {-math.sqrt(c2)} {math.sqrt(c2)}')
                elif c1 > 0 and c2 < 0:
                    print(f'Два корня: {-math.sqrt(c1)} {math.sqrt(c1)}')
                elif c1 < 0 and c2 > 0:
                    print(f'Два корня: {-math.sqrt(c2)} {math.sqrt(c2)}')
                elif c1 < 0 and c2 < 0:
                     print('Нет корней')
            elif D == 0:
                if - b / (2 * a) > 0:
                    print(f'Два корня: {- b / (2 * a)} {b / (2 * a)}')
                elif - b / (2 * a) == 0:
                    print('Один корень: 0')
                else:
                    print('Нет корней')
            else:
                print('Нет корней')


if __name__ == "__main__":
    main()
