from lab_python_oop import Rect, Square, Circle
import emoji

if __name__ == '__main__':
    n = 15
    rect = Rect(n, n, 'blue')
    circle = Circle(n, 'green')
    square = Square(n, 'red')

    print(rect)
    print(circle)
    print(square)

    print(emoji.emojize('Love :red_heart:'))