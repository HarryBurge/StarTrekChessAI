from bin.Game.Pieces import bishop, castle, king, knight, pawn, queen

map_size = (6, 10, 4)

map_array = [[[castle.Castle(team='Black'),knight.Knight(team='Black'),'x','x',knight.Knight(team='Black'),castle.Castle(team='Black')],
              [pawn.Pawn((0,1,0), team='Black'),pawn.Pawn((0,1,0), team='Black'),'x','x',pawn.Pawn((0,1,0), team='Black'),pawn.Pawn((0,1,0), team='Black')],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x']],

             [['x','x','x','x','x','x'],
              ['x',bishop.Bishop(team='Black'),queen.Queen(team='Black'),king.King(team='Black'),bishop.Bishop(team='Black'),'x'],
              ['x',pawn.Pawn((0,1,0), team='Black'),pawn.Pawn((0,1,0), team='Black'),pawn.Pawn((0,1,0), team='Black'),pawn.Pawn((0,1,0), team='Black'),'x'],
              ['x','@','@','@','@','x'],
              ['x','@','@','@','@','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x']],

             [['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x',bishop.Bishop(team='Black'),'@','@','@','x'],
              ['x','@','@','@','@','x'],
              ['x','@','@','@','@','x'],
              ['x','@','@','@','@','x'],
              ['x','x','x','x','x','x'],
              [pawn.Pawn((0,-1,0), team='White'),pawn.Pawn((0,-1,0), team='White'),'x','x',pawn.Pawn((0,-1,0), team='White'),pawn.Pawn((0,-1,0), team='White')],
              [castle.Castle(team='White'),knight.Knight(team='White'),'x','x',knight.Knight(team='White'),castle.Castle(team='White')]],

             [['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','x','x','x','x','x'],
              ['x','@','@','@','@','x'],
              ['x','@','@','@','@','x'],
              ['x',pawn.Pawn((0,-1,0), team='White'),pawn.Pawn((0,-1,0), team='White'),pawn.Pawn((0,-1,0), team='White'),pawn.Pawn((0,-1,0), team='White'),'x'],
              ['x',bishop.Bishop(team='White'),queen.Queen(team='White'),king.King(team='White'),bishop.Bishop(team='White'),'x'],
              ['x','x','x','x','x','x']]]
