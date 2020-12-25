using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Test.ReferenceAndValueTypes
{
    class UserActionsController : IUserActionsController 
    {
        public event KeyPressHandler OnKeyPress;

        public void StartListenKeyPress()
        {
            Task.Run(() =>
            {
                while (true)
                {
                    var key = Console.ReadKey().KeyChar;
                    OnKeyPress?.Invoke(key);
                }
            });
        }

        public void Activity(String key, ref MoveDirection direction)
        {
            if (key.Equals("w") && direction != MoveDirection.down)
            {
                direction = MoveDirection.up;
            }
            else if (key.Equals("s") && direction != MoveDirection.up)
            {
                direction = MoveDirection.down;
            }
            else if (key.Equals("d") && direction != MoveDirection.left)
            {
                direction = MoveDirection.right;
            }
            else if (key.Equals("a") && direction != MoveDirection.right)
            {
                direction = MoveDirection.left;
            }
        }
    }
}
