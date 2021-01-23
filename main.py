import pygame
import numpy as np

class Piece(pygame.sprite.Sprite):
    def __init__(self, startPosition):
        super(Piece, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 100, 155))
        self.rect = self.surf.get_rect()
        self.rect.center = startPosition

        self.
    def move(self, new_pos):
        self.rect.center = new_pos
        
    def isRestricted(self, coord):
        return False
class Board():
    def __init__(self, size):
        self.size = size
        self.field_size = self.size /8
    def draw(self, screen):
        
        for i in np.arange(0,8):
            for j in np.arange(0,8):
                if(np.mod(i+j,2 ) == 0):
                    pygame.draw.rect(screen, (0, 0, 255),pygame.Rect(i * self.field_size, j * self.field_size, self.field_size, self.field_size))


    def getPixPosition(self,row, col):
        return (col * self.field_size + self.field_size/2, 
                     row* self.field_size + self.field_size/2)
    def getCoordinate(self, xPos, yPos):
        return(np.floor(x_pos/self.field_size * 8), np.floor(y_pos/self.field_size * 8))

class Pawn(Piece):
    def __init__(self, startPosition):
        super(Pawn, self).__init__(startPosition)
        self.surf.fill((255, 0, 155))


class King(Piece):
    def __init__(self, startPosition):
        super(Pawn, self).__init__(startPosition)
        self.surf.fill((255, 20, 155))

class Queen(Piece):
    def __init__(self, startPosition):
        super(Pawn, self).__init__(startPosition)
        self.surf.fill((255, 40, 155))
    
class Rook(Piece):
    def __init__(self, startPosition):
        super(Pawn, self).__init__(startPosition)
        self.surf.fill((255, 60, 155))
        
class Bishop(Piece):
    def __init__(self, startPosition):
        super(Pawn, self).__init__(startPosition)
        self.surf.fill((255, 800, 155))
        

class Knight(Piece):
    def __init__(self, startPosition):
        super(Pawn, self).__init__(startPosition)
        self.surf.fill((255, 10, 155))
      
if __name__ =="__main__":
    pygame.init()
    
   
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    board = Board(SCREEN_HEIGHT)
    
    pawns = []
    for i in np.arange(8):
        pawns.append(Pawn(board.getPixPosition(0,i)))
    
    pieces = pawns
    
    piece_is_moving = False
    moving_piece = pawns[0]
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
                    moving_piece.move(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                  if(piece_is_moving):
                      pos = pygame.mouse.get_pos()
                      final_coord = board.getCoordinate(pos.x, pos.y)
                      
                      moving_piece.move()
                      piece_is_moving = False
                      print("Piece released")
        # Fill the background with white
        screen.fill((255, 255, 255))
        board.draw(screen)
        for pawn in pawns:
            screen.blit(pawn.surf, pawn.rect)
        # Flip the display
        pygame.display.flip()
    
    # Done! Time to quit.
    pygame.quit()