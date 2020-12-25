using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;

namespace Test.ReferenceAndValueTypes
{
    class Game : IGame
    {
        public void Start()
        {
            Layout layout = new Layout();
            Snake snake = new Snake();
            int speed = 500;
            UserActionsController input = new UserActionsController();
            Boolean playing = true;
            Food food = new Food();

            layout.AddBorder();
            input.OnKeyPress += (char key) =>
            {
                input.Activity(key.ToString(), ref snake.direction);
            };
            input.StartListenKeyPress();
            food.PlaceFood(layout);

            while (playing)
            {
                if (food.eated)
                {
                    food.PlaceFood(layout);
                    snake.eat();
                }
                snake.Move(snake.direction, layout, ref playing, food.location, ref food.eated);
                layout.Print(snake.snakeBody, food.location);
                Thread.Sleep(speed);
            }
            Console.SetCursorPosition(layout.x + 4, layout.y / 2);
            Console.Write("You lose");
        }
    }
}
