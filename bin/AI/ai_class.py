__authour__ = 'Harry Burge'
__date_created__ = '20/06/2020'
__last_updated_by__ = 'Harry Burge'
__last_updated_date__ = '20/06/2020'


class AI:

    def __init__(self):
        pass


    def suggest_move(self, board, team):
        pass


    def get_unsafe_pieces_on_team(self, board, team):
        unsafe_pieces = []

        for coords1, piece1 in board.get_pieces_of_team(team):

            unsafe = False

            for coords2, piece2 in board.get_all_pieces():

                if {'coords':coords1, 'mv_type':'Take'} in piece2.valid_move_coords(board, *coords2):
                    unsafe = True

            if unsafe:
                unsafe_pieces.append((coords1, piece1))

        return unsafe_pieces

    def get_safe_pieces_on_team(self, board, team):
        unsafe_pieces = self.get_unsafe_pieces_on_team(board, team)
        team_pieces = board.get_pieces_of_team(team)

        safe_pieces = [piece for piece in team_pieces if piece not in unsafe_pieces]
        
        return safe_pieces
