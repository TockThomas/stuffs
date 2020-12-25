using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace Test.ReferenceAndValueTypes
{
    public class Snake : ISnake
    {
        public List<System.Drawing.Point> snakeBody = new List<System.Drawing.Point>();
        public MoveDirection direction;
        public int snakeLength;
        int x;

        public Snake()
        {
            snakeBody.Insert(0, new System.Drawing.Point(3, 3));
            snakeBody.Insert(0, new System.Drawing.Point(4, 3));
            snakeLength = 1;
            direction = MoveDirection.right;
        }

        public void Move(MoveDirection direction, Layout layout, ref Boolean playing, System.Drawing.Point foodlocation, ref Boolean foodeated)
        {
            if (direction == MoveDirection.right)
            {
                this.snakeBody.Insert(0, new System.Drawing.Point(this.snakeBody[0].X + 1, this.snakeBody[0].Y));
                try
                {
                    this.snakeBody.RemoveAt(this.snakeLength + 1);
                }
                catch
                {

                }
                if (this.snakeBody[0].X == layout.x - 2)
                {
                    playing = false;
                }
            } 
            else if (direction == MoveDirection.left)
            {
                this.snakeBody.Insert(0, new System.Drawing.Point(this.snakeBody[0].X - 1, this.snakeBody[0].Y));
                try
                {
                    this.snakeBody.RemoveAt(this.snakeLength + 1);
                }
                catch
                {

                }
                if (this.snakeBody[0].X == 1)
                {
                    playing = false;
                }
            }
            else if (direction == MoveDirection.up)
            {
                this.snakeBody.Insert(0, new System.Drawing.Point(this.snakeBody[0].X, this.snakeBody[0].Y - 1));
                try
                {
                    this.snakeBody.RemoveAt(this.snakeLength + 1);
                }
                catch
                {

                }
                if (this.snakeBody[0].Y == 1)
                {
                    playing = false;
                }
            }
            else if (direction == MoveDirection.down)
            {
                this.snakeBody.Insert(0, new System.Drawing.Point(this.snakeBody[0].X, this.snakeBody[0].Y + 1));
                try
                {
                    this.snakeBody.RemoveAt(this.snakeLength + 1);
                }
                catch
                {

                }
                if (this.snakeBody[0].Y == layout.y - 1)
                {
                    playing = false;
                }
            }
            if (this.snakeBody[0] == foodlocation)
            {
                foodeated = true;
            }
            x = 1;
            foreach (System.Drawing.Point body in snakeBody)
            {
                if (x == 1)
                {
                    x += 1;  //to skip this.snakeBody[0]
                }
                else if (body == this.snakeBody[0])
                {
                    playing = false;
                }
            }
        }

        public void eat()
        {
            this.snakeLength += 1;
        }
    }
}
