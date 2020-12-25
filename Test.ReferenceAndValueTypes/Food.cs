using System;
using System.Collections.Generic;
using System.Text;

namespace Test.ReferenceAndValueTypes
{
    class Food : IFood
    {
        public Boolean eated = true;
        public System.Drawing.Point location;
        Random random = new Random();

        public void PlaceFood(Layout layout)
        {
            this.location = new System.Drawing.Point(random.Next(2, layout.x - 1), (random.Next(2, layout.y - 1)));
            this.eated = false;
        }
    }
}
