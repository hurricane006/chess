class Piece:

    # Will define all of the properties that a chess piece can have

    def __init__ (self, color, name):

        self.color = color
        self.name = name
    
    def promote(self, newName):

        self.name = newName