from tkinter import *
from random import choice, randint

ball_initial_number = 10
ball_minimal_radius = 15
ball_maximal_radius = 30
ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
balls_coord = []  #список координат шариков
balls_num = []    #список номеров шариков

def click_ball(event):
    """
    Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    По клику мышкой удаляем шарик, на котором стоит указатель мышки,
    а также засчитывать их в очки пользователя
    """
    global points, label,  balls_coord, balls_num
    obj = canvas.find_closest(event.x, event.y) # это шарик (его кортеж!)
    x1, y1,x2,y2 = canvas.coords(obj) # координаты шарика в прямоугольнике
    num = obj[0]  # вытаскиваем номер шарика (объекта) из кортежа
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        index = balls_num.index(num)  # определяем индекс элемента списка,
                                      # где хранится номер объекта
        balls_num.pop(index)    # удаляем элемент списка с номером объекта
        balls_coord.pop(index)  # удаляем элемент списка с координатами объекта
        points += 1             # добавляем очко
        label['text'] = points  # выводим счёт на метку
        create_random_ball()

def move_all_balls(event):
    """ перемещает все шарики на чуть-чуть
    """
    global balls_coord
    for obj in balls_coord:
        x1, y1, x2, y2 = canvas.coords(obj[0])
        # проверяем, не выйдет ли шарик за границы холста
        if x1+obj[1]+2*obj[3] >= int(canvas['width']) or x1+obj[1] <= 0:
            obj[1] = -obj[1] # меняем направление движения шарика
        if y1+obj[2]+2*obj[3] >= int(canvas['height']) or y1+obj[2] <= 0:
            obj[2] = -obj[2]
        canvas.move(obj[0],obj[1],obj[2])

def create_random_ball():
    """
    Создаёт шарик в случайном месте игрового холста canvas,
    причём шарик не выходит за границы холста!
    """
    global balls_coord, balls_num
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width']) - 2*R -1)
    y = randint(0, int(canvas['height']) - 2*R -1)
    # рисуем шарик и запоминаем его номер в num_oval
    num_oval = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())
    dx = randint(-2, 2)
    dy = randint(-2, 2)
    # запоминаем идентификатор, вектор и радиус движения нового шарика
    balls_coord.append([num_oval, dx, dy, R])
    balls_num.append(num_oval) # запоминаем номер нового шарика

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
    global root, canvas, label, points

    root = Tk()  # открываем главное окно
    # поместить холст c белым фоном и размером 600х400 в главном окне:
    canvas = Canvas(root, background='white', width=600, height=400)
    label_text = Label(root, text = 'Набранные очки')
    label_text.pack()
    points = 0
    label = Label(root, text=points) # привязка к переменной
    label.pack()
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