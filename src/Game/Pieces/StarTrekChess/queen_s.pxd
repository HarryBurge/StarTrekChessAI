from src.Game cimport piece_class

cdef class Queen(piece_class.Piece):
    cdef list valid_move_coords(self, object board, int x, int y, int z):