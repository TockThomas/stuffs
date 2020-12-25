using System;
using System.Collections.Generic;
using System.Text;

namespace Test.ReferenceAndValueTypes
{
    interface ILayout
    {
        public void Print(List<System.Drawing.Point> snakebody, System.Drawing.Point food);
        void AddBorder();
    }
}
