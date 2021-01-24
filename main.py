import pygame
import numpy as np
from enum import Enum  

class Color(Enum):
    white = 1
    black = 2
 
def getOpponentColor(color):
    if color == Color.white:
        return Color.black
    elif color == Color.black:
        return Color.white
    return None

# game field coordinate ( (0,0) ..-> (8,8))
class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def equals(self, Coordinate):
        return self.x == Coordinate.x and self.y == Coordinate.y 
    def name(self):
        dict_namey = ["a", "b", "c", "d", "e", "f", "g","h"]
        name = dict_namey[int(self.y)]
        name += str(int(self.x +1))
        return name
        
# game field coordinate ( (0,0) ..-> (8,8))
class PixPos():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def isBishopMove(startcoord, endcoord, game):
    
    move_x = (endcoord.x - startcoord.x) 
    move_y = (endcoord.y - startcoord.y) 
    if not abs(move_x) == abs(move_y):
        return False
    xrange = np.arange(0,1)
    yrange = np.arange(0,1)
    if move_x > 0:
        xrange = np.arange(startcoord.x +1 , endcoord.x)
    elif move_x < 0:
        xrange = np.arange(endcoord.x + 1, startcoord.x)
        
    if move_y > 0:
        yrange = np.arange(startcoord.y +1 , endcoord.y)
    elif move_y < 0:
        yrange = np.arange(endcoord.y + 1, startcoord.y)
        

    for x in xrange:
        for y in yrange:
            coord = Coordinate(x,y)
            if coord.equals(startcoord):
                continue
            move_x = (coord.x - startcoord.x) 
            move_y = (coord.y - startcoord.y) 
            if not abs(move_x) == abs(move_y):
                continue
            if game.getPiece(coord):
                return False
        
    return  True

def isRookMove(startcoord, endcoord, game):
    
    move_x = (endcoord.x - startcoord.x) 
    move_y = (endcoord.y - startcoord.y) 
    if not ((abs(move_x) > 0 and abs(move_y) ==0) or
            abs(move_x) == 0 and abs(move_y) >0):
        return False
    xrange = np.arange(0,1)
    yrange = np.arange(0,1)
    if move_x > 0:
        xrange = np.arange(startcoord.x +1 , endcoord.x)
        yrange = np.arange(startcoord.y, startcoord.y + 1)
    elif move_x < 0:
        xrange = np.arange(endcoord.x + 1, startcoord.x)
        yrange = np.arange(startcoord.y, startcoord.y + 1)
        
    elif move_y > 0:
        xrange = np.arange(startcoord.x, startcoord.x + 1)
        yrange = np.arange(startcoord.y +1 , endcoord.y)
    elif move_y < 0:
        xrange = np.arange(startcoord.x, startcoord.x + 1)
        yrange = np.arange(endcoord.y + 1, startcoord.y)
        
   
    for x in xrange:
        for y in yrange:
            if Coordinate(x,y).equals(startcoord):
                continue
            if game.getPiece(Coordinate(x,y)):
                return False
    return True
            

class Piece(pygame.sprite.Sprite):
    def __init__(self, startCoordinate, board):
        super().__init__()
        self.surf = pygame.Surface((75, 75))
        self.rect = self.surf.get_rect()

        self.currentCoordinate = startCoordinate
        self.rect.center = board.getPixPosition(startCoordinate)
    
    def moveVisually(self, new_pos):
        self.rect.center = new_pos
        
    def isLegalMove(self, coord, game):
        otherPiece = game.getPiece(coord, self.team_color)
        if self is otherPiece:
            return True
        if otherPiece:
            return False
        move_x = (coord.x - self.currentCoordinate.x) 
        move_y = (coord.y - self.currentCoordinate.y)         
        
        return abs(move_x)+abs(move_y) !=0

def initPiecesOnBoard():
    pieces = []
    for i in np.arange(8):
        pieces.append(wPawn(Coordinate(1,i), board))
    pieces.append(wRook(Coordinate(0,0), board))
    pieces.append(wRook(Coordinate(0,7), board))
    pieces.append(wKnight(Coordinate(0,1), board))
    pieces.append(wKnight(Coordinate(0,6), board))
    pieces.append(wBishop(Coordinate(0,2), board))
    pieces.append(wBishop(Coordinate(0,5), board))
    pieces.append(wQueen(Coordinate(0,3), board))
    pieces.append(wKing(Coordinate(0,4), board))
    
    for i in np.arange(8):
        pieces.append(bPawn(Coordinate(6,i), board))
    pieces.append(bRook(Coordinate(7,0), board))
    pieces.append(bRook(Coordinate(7,7), board))
    pieces.append(bKnight(Coordinate(7,1), board))
    pieces.append(bKnight(Coordinate(7,6), board))
    pieces.append(bBishop(Coordinate(7,2), board))
    pieces.append(bBishop(Coordinate(7,5), board))
    pieces.append(bQueen(Coordinate(7,3), board))
    pieces.append(bKing(Coordinate(7,4), board))
    return pieces

class Game():
    def __init__(self):
        self.pieces = initPiecesOnBoard()
        
        self.whosTurnIsIt = Color.white
    def move(self, piece, targetCoordinate):
            if(piece.isLegalMove(targetCoordinate, self) and 
               self.whosTurnIsIt == piece.team_color):
                piece.currentCoordinate = targetCoordinate
                opponentPiece = self.getPiece(targetCoordinate, getOpponentColor(piece.team_color))
                if(opponentPiece):
                    self.pieces.remove(opponentPiece)
                self.whosTurnIsIt = getOpponentColor(self.whosTurnIsIt)
            piece.rect.center = board.getPixPosition(piece.currentCoordinate)
        
    def getPiece(self, coord, color = None):
        for piece in self.pieces:
                if (color != None and color != piece.team_color):
                    continue
                if coord.equals(piece.currentCoordinate):
                    return piece
        return None

class Board():
    def __init__(self, size):
        self.size = size
        self.field_size = self.size /8
    def draw(self, screen):
        
        for i in np.arange(0,8):
            for j in np.arange(0,8):
                if(np.mod(i+j,2 ) == 0):
                    pygame.draw.rect(screen, (0, 0, 255),pygame.Rect(i * self.field_size, j * self.field_size, self.field_size, self.field_size))


    def getPixPosition(self, coordinate):
        return (coordinate.y * self.field_size + self.field_size/2, 
                     self.size - (coordinate.x* self.field_size + self.field_size/2))
    def getCoordinate(self, pixPos):
        return Coordinate( 7 - np.floor(pixPos.y/self.field_size), np.floor(pixPos.x/self.field_size))

class Pawn(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
    def isLegalMove(self, coord, game):
        print("Target field:")
        print(coord.name())
        print("Starting")
        print(self.currentCoordinate.name())
        print(self.currentCoordinate.x)
        legal = super().isLegalMove(coord, game)
        if not legal:
            return False
        
        if self.isDoublePawnMove(coord, game) or self.isSinglePawnMove(coord, game):
            return True
        return False
    def pawnMoveDirection(self):
        raise(NotImplementedError)
    def startingRow(self):
        raise(NotImplementedError)
        
    def isDoublePawnMove(self, coord, game):
        move_x = (coord.x - self.currentCoordinate.x) 
        move_y = (coord.y - self.currentCoordinate.y) 
        print("Move direction (x/y):")
        print(move_x)
        print(move_y)
        if (int(move_x) == 2 * int(self.pawnMoveDirection()) and
            (self.startingRow() == self.currentCoordinate.x) and 
            move_y == 0 and 
            not game.getPiece(coord) and
            not game.getPiece(Coordinate(self.currentCoordinate.x + self.pawnMoveDirection(), coord.y))):
            return True
        
    def isSinglePawnMove(self, coord, game):
        move_x = (coord.x - self.currentCoordinate.x) 
        move_y = (coord.y - self.currentCoordinate.y) 
        if int(move_x) != int(self.pawnMoveDirection()):
            return False
        if move_y == 0 and not game.getPiece(coord):
            return True
        elif abs(move_y) == 1:
            if(game.getPiece(coord, getOpponentColor(self.team_color))):
               return True    
            

class King(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
    def isLegalMove(self, coord, game):
        legal = super().isLegalMove(coord, game)
        if not legal:
            return False
        move_x = (coord.x - self.currentCoordinate.x) 
        move_y = (coord.y - self.currentCoordinate.y) 

        if abs(move_x) <= 1 and abs(move_y) <=1:
            return True 
        
        return False
    
class Queen(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
    
    def isLegalMove(self, coord, game):
        legal = super().isLegalMove(coord, game)
        if not legal:
            return False

        if (isBishopMove(self.currentCoordinate, coord, game) or 
            isRookMove(self.currentCoordinate, coord, game)):
            return True 
        
        return False
    
class Rook(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
    def isLegalMove(self, coord, game):
        print(coord.x, coord.y)
        legal = super().isLegalMove(coord, game)
        if not legal:
            return False
       
        if isRookMove(self.currentCoordinate, coord, game):
            return True 
        
        return False
        
class Bishop(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
    def isLegalMove(self, coord, game):
        legal = super().isLegalMove(coord, game)
        if not legal:
            return False

        if isBishopMove(self.currentCoordinate, coord, game):
            return True 
        
        return False
        
class Knight(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
    def isLegalMove(self, coord, game):
        legal = super().isLegalMove(coord, game)
        if not legal:
            return False
        move_x = (coord.x - self.currentCoordinate.x) 
        move_y = (coord.y - self.currentCoordinate.y) 

        if ((abs(move_x) == 2 and abs(move_y) ==1)  or
        (abs(move_x) == 1 and abs(move_y) ==2)):
            return True 
        
        return False


class wPawn(Pawn):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_plt60.png")
        self.team_color = Color.white
        
    def pawnMoveDirection(self):
        return 1
    def startingRow(self):
        return 1
    
class wKing(King):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_klt60.png")
        self.team_color = Color.white
        
class wQueen(Queen):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_qlt60.png")
        self.team_color = Color.white
        
class wRook(Rook):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_rlt60.png")
        self.team_color = Color.white
        
class wBishop(Bishop):
    def __init__(self, startPosition, board):
       super().__init__(startPosition, board)
       self.image = pygame.image.load("resources/pieces/Chess_blt60.png")
       self.team_color = Color.white
        
class wKnight(Knight):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_nlt60.png")
        self.team_color = Color.white
        
class bPawn(Pawn):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_pdt60.png")
        self.team_color = Color.black
        
    def pawnMoveDirection(self):
        return -1
    def startingRow(self):
        return 6
        
class bKing(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_kdt60.png")
        self.team_color = Color.black
        
class bQueen(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_qdt60.png")
        self.team_color = Color.black
        
class bRook(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_rdt60.png")
        self.team_color = Color.black
        
class bBishop(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_bdt60.png")
        self.team_color = Color.black
        
class bKnight(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_kdt60.png")
        self.team_color = Color.black

      
if __name__ =="__main__":
    pygame.init()
    
   
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    board = Board(SCREEN_HEIGHT)
    
    game = Game()
    piece_is_moving = False
    moving_piece = game.pieces[0]
    # Run until the user asks to quit
    running = True
    while running:
    
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
              # get a list of all sprites that are under the mouse cursor
              clicked_pieces = [s for s in game.pieces if s.rect.collidepoint(pygame.mouse.get_pos())]
              
              assert len(clicked_pieces)< 2
              if len(clicked_pieces) == 1:
                  piece_is_moving = True
                  moving_piece = clicked_pieces[0]
                  print("Piece Clicked")
                  
            elif event.type == pygame.MOUSEMOTION:
                if(piece_is_moving):
                    moving_piece.moveVisually(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                  if(piece_is_moving):
                      [pos_x, pos_y] = pygame.mouse.get_pos()
                      final_coord = board.getCoordinate(PixPos(pos_x, pos_y))
                      game.move(moving_piece, final_coord)
                      piece_is_moving = False

        # Fill the background with white
        screen.fill((255, 255, 255))
        board.draw(screen)
        for piece in game.pieces:
            screen.blit(piece.image, piece.rect)
        # Flip the display
        pygame.display.flip()
    
    # Done! Time to quit.
    pygame.quit()