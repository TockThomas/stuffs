using System;
using System.Collections.Generic;
using System.Text;

namespace Test.ReferenceAndValueTypes
{
    public delegate void KeyPressHandler(char key);

    interface IUserActionsController
    {
        public event KeyPressHandler OnKeyPress;
        public void StartListenKeyPress();
        public void Activity(String key, ref MoveDirection direction);
    }
}
