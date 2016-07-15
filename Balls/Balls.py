from tkinter import *
from random import choice, randint

ball_initial_number = 15
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']


def click_ball(event):
    """
    Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой удаляем шарик, на котором стоит указатель мышки,
    а также засчитывать их в очки пользователя
    """
    obj = canvas.find_closest(event.x, event.y) # это номер шарика
    x1, y1,x2,y2 = canvas.coords(obj) # координаты шарика в прямоугольнике
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)

        create_random_ball()

def move_all_balls(event):
    """ перемещает все шарики на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    Создаёт шарик в случайном месте игрового холста canvas,
    причём шарик не выходит за границы холста!
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width']) - 2*R -1)
    y = randint(0, int(canvas['height']) - 2*R -1)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())

def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)

def init_ball_catch_game():
    """
    Создаём необходимое кол-во шариков, по которым надо будет кликать
    :return:
    """
    for i in range(ball_initial_number):
        create_random_ball()

def init_main_window():
    global root, canvas

    root = Tk()  # открываем главное окно
    # поместить холст c белым фоном и размером 600х400 в главном окне:
    canvas = Canvas(root, background='white', width=600, height=400)
    canvas.bind("<Button>", click_ball) # связываем холст с событием - Button
                                        # и обработчиком click_ball
    canvas.bind("<Motion>", move_all_balls) # связываем холст с событием -
                                  # Motion и обработчиком move_all_balls
    canvas.pack()  # универсальный упаковщик - определяет положение
                   # холста в главном окне


if __name__=="__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()         # запускаем главный исполнитель
    print("Приходите играть ещё!")