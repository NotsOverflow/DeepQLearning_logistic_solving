#              _            _
# |\| _ _|_ _ / \    _  ___|_ |  _
# | |(_) |__> \_/\_/(/_ |  |  | (_)\^/
#
# htest.py created December 1st 2020
# by richard juan (contact@richardjuan-business.com)
#
# ----------------------------------------------
#
# using Human to solve MCDO
#
# ----------------------------------------------

from mcdo import MacDo

if __name__ == '__main__':
    game = MacDo()
    action = 0
    while action != 33:
        game.render()
        print("\nchoices: '1-10' <- big mac  , '11-20' <- mc chicken, '21-30' <- special burger")
        action = int(input("\nwhat should be cooked ?  "))
        game.step(action)