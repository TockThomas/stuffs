using System;
using System.Collections.Generic;
using System.Text;

namespace Test.ReferenceAndValueTypes
{
    interface ISnake
    {
        void Move(MoveDirection direction, Layout layout, ref Boolean playing, System.Drawing.Point foodlocation, ref Boolean foodeated);
        void eat();
    }
}
