from turtle import Screen
from myturtle import MyTurtle
from car import Car
import time
import random

MIN_AMOUNT_OF_CARS = 3
MAX_AMOUNT_OF_CARS = 12
TIME_ADD_CAR = 3

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)

turtle = MyTurtle()
turtle.create_turtle()
screen.listen()
screen.onkey(turtle.move_forward, "Up")

def create_cars():
    amount_of_cars = random.randint(MIN_AMOUNT_OF_CARS, MAX_AMOUNT_OF_CARS)
    new_cars = []
    for car in range(amount_of_cars):
        new_car = Car()
        new_cars.append(new_car)
    return new_cars

game_is_on = True
timer = TIME_ADD_CAR
cars_on_the_fild = []
while game_is_on:
    if timer >= TIME_ADD_CAR:
        new_cars = create_cars()
        timer = 0.0
    if len(new_cars) >= MIN_AMOUNT_OF_CARS:
        lines = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        for car in new_cars:
            chosen_l = random.choice(lines)
            lines.remove(chosen_l)
            car.goto(random.randint(200,300), -250 + (chosen_l * 20))
            cars_on_the_fild.append([car, random.randint(5,15)])
        print(lines)
        new_cars = []
    for car in cars_on_the_fild:
        car[0].forward(car[1])
        if car[0].distance(turtle) < 25:
            lost = MyTurtle()
            lost.create_text("YOU LOST!")
            game_is_on = False
    time.sleep(0.1)
    
    if turtle.ycor() > 280:
        won = MyTurtle()
        won.create_text("YOU WON!")
        game_is_on = False
        
    timer += 0.1
    screen.update()

screen.exitonclick()