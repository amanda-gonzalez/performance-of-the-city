import turtle
import time

def draw(word):
    rgb = [0,1,2]
    idx = 0
    for letter in word:
        rgb[idx] += word.index(letter) * 255 // 26
        idx += 1
        if idx >= 3:
            idx = 0

    tup = tuple(rgb)
    turtle.bgcolor(tup)
    time.sleep(0.5)


def run():
    with open('poem.txt', 'r') as file:
        for line in file:
            for word in line.split():
                draw(word)

if __name__ == '__main__':
    s = turtle.getscreen()
    t = turtle.Turtle()
    s.colormode(255)
    run()
    turtle.Screen().exitonclick()