import pygame
import numpy as np

# game field coordinate ( (0,0) ..-> (8,8))
class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def equals(self, Coordinate):
        return self.x == Coordinate.x and self.y == Coordinate.y 
        
# game field coordinate ( (0,0) ..-> (8,8))
class PixPos():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Piece(pygame.sprite.Sprite):
    def __init__(self, startCoordinate, board):
        super().__init__()
        self.surf = pygame.Surface((75, 75))
        self.rect = self.surf.get_rect()

        self.currentCoordinate = startCoordinate
        self.rect.center = board.getPixPosition(startCoordinate)
    
    def moveVisually(self, new_pos):
        self.rect.center = new_pos

    def move(self, pieces, targetCoordinate):
        sameColorCollision = False
        
        for otherPiece in pieces:
            if self is otherPiece:
                continue
            if self.team_color == otherPiece.team_color:
                if targetCoordinate.equals(otherPiece.currentCoordinate):
                    sameColorCollision = True
                    break
                
        print("Same Color?", sameColorCollision)
        if(not self.isIllegalMove(targetCoordinate) 
           and not sameColorCollision):
            self.currentCoordinate = targetCoordinate
        self.rect.center = board.getPixPosition(piece.currentCoordinate)
        
    def isIllegalMove(self, coord):
        print("Base class illeg")
        raise NotImplementedError()

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
        return (coordinate.x * self.field_size + self.field_size/2, 
                     coordinate.y* self.field_size + self.field_size/2)
    def getCoordinate(self, pixPos):
        return Coordinate(np.floor(pixPos.x/self.field_size), np.floor(pixPos.y/self.field_size))

class Pawn(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
    

class King(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
    def isIllegalMove(self, coord):
        print("child class illeg")
        move_x = (coord.x - self.currentCoordinate.x) 
        move_y = (coord.y - self.currentCoordinate.y) 
        print(move_x)
        print(move_y)
        if abs(move_x) <= 1 and abs(move_y) <=1  and abs(move_x)+abs(move_y) !=0:
            return False
        print("ILLEGAL MOVE")
        return True
class Queen(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
    
class Rook(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
class Bishop(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        
class Knight(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)


class wPawn(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_plt60.png")
        self.team_color = "white"

class wKing(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_klt60.png")
        self.team_color = "white"
        
class wQueen(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_qlt60.png")
        self.team_color = "white"
        
class wRook(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_rlt60.png")
        self.team_color = "white"
        
class wBishop(Piece):
    def __init__(self, startPosition, board):
       super().__init__(startPosition, board)
       self.image = pygame.image.load("resources/pieces/Chess_blt60.png")
       self.team_color = "white"
        
class wKnight(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_nlt60.png")
        self.team_color = "white"
        
class bPawn(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_pdt60.png")
        self.team_color = "black"
        
class bKing(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_kdt60.png")
        self.team_color = "black"
        
class bQueen(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_qdt60.png")
        self.team_color = "black"
        
class bRook(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_rdt60.png")
        self.team_color = "black"
        
class bBishop(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_bdt60.png")
        self.team_color = "black"
        
class bKnight(Piece):
    def __init__(self, startPosition, board):
        super().__init__(startPosition, board)
        self.image = pygame.image.load("resources/pieces/Chess_kdt60.png")
        self.team_color = "black"

      
if __name__ =="__main__":
    pygame.init()
    
   
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    board = Board(SCREEN_HEIGHT)
    
    wPieces = []
    # for i in np.arange(8):
    #     wPieces.append(wPawn(Coordinate(1,i), board))
    # wPieces.append(wRook(Coordinate(0,0), board))
    # wPieces.append(wRook(Coordinate(0,7), board))
    # wPieces.append(wKnight(Coordinate(0,1), board))
    # wPieces.append(wKnight(Coordinate(0,6), board))
    # wPieces.append(wBishop(Coordinate(0,2), board))
    # wPieces.append(wBishop(Coordinate(0,5), board))
    # wPieces.append(wQueen(Coordinate(0,3), board))
    wPieces.append(wKing(Coordinate(0,4), board))
    
    pieces = wPieces    
    
    piece_is_moving = False
    moving_piece = pieces[0]
    # Run until the user asks to quit
    running = True
    while running:
    
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
              # get a list of all sprites that are under the mouse cursor
              clicked_pieces = [s for s in pieces if s.rect.collidepoint(pygame.mouse.get_pos())]
              
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
                      print("Pos:",pos_x, pos_y)
                      final_coord = board.getCoordinate(PixPos(pos_x, pos_y))
                      print("Final Coord %f, %f", final_coord.x, final_coord.y)
                      print(pieces)
                      moving_piece.move(pieces,final_coord)
                      piece_is_moving = False
                      print("Piece released")
        # Fill the background with white
        screen.fill((255, 255, 255))
        board.draw(screen)
        for piece in pieces:
            screen.blit(piece.image, piece.rect)
        # Flip the display
        pygame.display.flip()
    
    # Done! Time to quit.
    pygame.quit()