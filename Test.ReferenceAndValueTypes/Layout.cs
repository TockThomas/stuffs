using System;
using System.Collections.Generic;
using System.Text;

namespace Test.ReferenceAndValueTypes
{
    public class Layout : ILayout
    {
        public int x = 21;
        public int y = 10;

        public void AddBorder()
        {
            for (int i = 0; i < x + 1; i++)
            {
                Console.SetCursorPosition(i, 0);
                Console.Write("-");
                Console.SetCursorPosition(i, y);
                Console.Write("-");
            }
            for (int i = 1; i < y; i++)
            {
                Console.SetCursorPosition(0, i);
                Console.Write("|");
                Console.SetCursorPosition(x, i);
                Console.WriteLine("|");
            }
        }

        public void Print(List<System.Drawing.Point> snakebody, System.Drawing.Point food)
        {
            for(int i = 2; i < x; i++)
            {
                for (int j = 1; j < y; j++)
                {
                    Console.SetCursorPosition(i, j);
                    
                    Console.Write("\b \b");
                }
            }
            Console.SetCursorPosition(food.X, food.Y);
            Console.Write("@");
            foreach (System.Drawing.Point position in snakebody)
            {
                Console.SetCursorPosition(position.X, position.Y);
                Console.Write("*");
            }
            Console.SetCursorPosition(x + 4, y / 2);
            Console.Write("\b \b");

        }
    }
}
