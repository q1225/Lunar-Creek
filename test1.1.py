from enum import Enum
import pygame
import pygame.mixer
import pygame.freetype
from pygame.rect import Rect
from pygame.sprite import RenderUpdates, Sprite,LayeredUpdates
import os
from plistlib import Image
import pickle
import audioop as music
import wave, glob
white = (255, 255, 255)
Orange = [255, 165, 0]
Red = [255, 0, 0]
Purple = [159, 43, 104]
MB = [199, 9, 70]
X=0
Y=0
FBG=[]
path = "/lunarcreek/lunarcreek/FBG"
valid_images = [".JPG"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    FBG.append(Image.open(os.path.join(path,f)))
   
bm=[]
path = "/lunarcreek/lunarcreek/bm"
valid = [".wav"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid:
        continue
    bm.append(wave.open(os.path.join(path,f)))
SE=[]
path = "/lunarcreek/lunarcreek/SE"
valid1 = [".wav"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid1:
        continue
    SE.append(wave.open(os.path.join(path,f)))
C=[]
path = "/lunarcreek/lunarcreek/C"
valid2 = [".png"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid2:
        continue
    C.append(Image.open(os.path.join(path,f)))
vc=[]
path = "/lunarcreek/lunarcreek/VC"
valid3 = [".wav"]
for f in os.listdir(path):
    ext =Image.os.path.splitext(f)[1]
    if ext.lower() not in valid3:
        continue
    vc.append(wave.open(os.path.join(path,f)))
display_surface= pygame.display.set_mode((X, Y))
os.listdir()
class UIElement(Sprite):
    """A user interface element that can be added to a surface"""

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
          """
            Args:
             center_position - tuple (x, y)
             text - string of text to write
             font_size - int
             bg_rgb (background colour) - tuple (r, g, b)
             text_rgb (text colour) - tuple (r, g, b)
             action - the gamestate change associated with this button
          """
          self.mouse_over = False

          default_image = create_surface_with_text(
           text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
             )

          highlighted_image = create_surface_with_text(
              text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
            )
          self.images = [default_image, highlighted_image]
          self.rects = [
             default_image.get_rect(center=center_position),highlighted_image.get_rect(center=center_position),
            ]

          self.action = action
          super().__init__()

    @property
    def image(self):
           self.images[1] if self.mouse_over else self.images[0]
    @property
    def rect(self):
          return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """Updates the element's appearance depending on the mouse position
        and returns the button's action if clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
    def draw(self, surface):
        """Draws element onto a surface"""
        surface.blit(self.image, self.rect)

        # def __init__(self, center_position, text, font_size, text_rgb, action=None):
        #     self.action = action


def dialog(n,x2,y2):
 def feeling(f,ch,x1,y1):
    #n==1 fannie f==cp==0-5
    #n==2 bea f==cp==6-11
    #n==3 innkeeper f==cp==13-19
    #n==4 musuem guide f==cp== 20
    #n==5 boss f==cp==12
    #n==6  f==cp==                  
  def voice(f):
      for i in range (0,len (vc)):
        for a in range (0,f):
         if(f!=0):
          pygame.image.load(C[ch+f])
         if (n%2==0):
          X+=100
          Y=400
          LayeredUpdates.move_to_front()
          pygame.time.set_timer(5000)
          display_surface.blit(image, (0, 0)) 
          pygame.mixer.load(vc[i])  
         else:
          X=700
          Y=400
          LayeredUpdates.move_to_front()
          pygame.time.set_timer(5000)
          display_surface.blit(image, (0, 0)) 
          sound=pygame.mixer.load(vc[i])
      for c in range (0,n): 
         channel3 = pygame.mixer.Channel(c)
         pygame.mixer.Channel.play()
         pygame.mixer.Channel.stop() 
         return print(lines)
      with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
           speech=create_surface_with_text("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx",32,Orange,MB)
      for x2 in range (x2,y2,+2):
        lines = [line.rstrip() for line in fl]
      else:
        pygame.image.load(C[ch+1])
        X+=100
        Y=400
        LayeredUpdates.move_to_front()
        pygame.time.set_timer(5000)
        display_surface.blit(image, (0, 0)) 
        sound=pygame.mixer.load(vc[ch[i]])
        channel3 = pygame.mixer.Channel(n)
        pygame.mixer.Channel.play()
        pygame.mixer.Channel.stop() 
      with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
         speech=create_surface_with_text("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx",32,Orange,MB)
      for x1 in range (x1+1,y1,+2):
          lines = [line.rstrip() for line in fl]
          return print(lines) 
      for cp in range (0,n):
         ch=(input("who"))
         f=(input("How is the charater feeling"))
         feeling(f,ch,x1,y1) 
          #minor characters
      if ch==5:
        sc1=[127,129]
        with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
           for x2 in range (0,len(sc1)):
            lines = [line.rstrip() for line in fl]
        return print(lines) 
      if ch==6:
       sc1=[128,130]
       with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
          for x3 in range (0,len(sc1)):
           lines = [line.rstrip() for line in fl]
          return print(lines)  
      if ch==7:
         sc=[241,243,245,247]
        
         with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
           for x4 in range (0,len(sc1)):
            lines = [line.rstrip() for line in fl]
           return print(lines)
      if ch==8:
         sc=[260,264]
        
         with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
          for x2 in range (0,len(sc1)):
           lines = [line.rstrip() for line in fl] 
          return print(lines)
class Scence(Sprite): 
     def Scence(imaged,dialog):
          """
            Args:
             image - list (b[])
             sound-list (bm[])
             sounde-list(SE[])
             dialogue (txt) -list dialog ([n,x,y])
          """ 
        
        
def imaged(x,y):
             for x in range(x,y):
              v=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
              pygame.image.load(FBG[x])
              screen=display_surface
              screen.fill(white)
              X=800
              Y=600
              display_surface.blit(image, (0, 0))
              sound=pygame.mixer.load(bm[1])
              channel1 = pygame.mixer.Channel(0)
              pygame.mixer.Channel.play()
              pygame.mixer.Channel.stop()
              
              
def seal(x):
        for k in range(0,3):
            seal=[17,104,128]
        with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
            lines=seal[k] 
        if x==seal[k]:
            screen=display_surface
            screen.fill(white)
            pygame.image.load(C[25])
            X=400
            Y=400
            display_surface.blit(image, (0, 0))        
            LayeredUpdates.move_to_front()
def ts (x,self):
        for l in range (0,13):
         ts=[4,31,40,57,61,62,68,85,89,91,137,152,154,177]
        with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
           lines=ts[l] 
        if x<20 :
           screen=display_surface
           screen.fill(white)
           nextlevel_btn = UIElement(
            center_position=(400, 400),
            font_size=30,
            bg_rgb=white,
            image =pygame.image.load (FBG[x]),   
            action=pygame.Gamestate.NEXT_LEVEL
         )  
           buttons = RenderUpdates(nextlevel_btn)
          
           X=800
           Y=600
           display_surface.blit(image, (0, 0))
           self.soundb=pygame.mixer.load(m[1])
           channel1 = pygame.mixer.Channel(0)
           pygame.mixer.Channel.play()
           pygame.mixer.Channel.stop()
           return game_loop(screen, buttons)
def sounde(n,soundeffect,x4,self):
          if soundeffect==True:
           self.sound=pygame.mixer.load(SE[n]) 
           channel2 = pygame.mixer.Channel(4)
           pygame.mixer.Channel.play()
           pygame.mixer.Channel.stop()
           with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
            lines=ts1[i]
          for i in range (0,3):
           ts1=[44,31,40]
          if sounde(n,True,x4==ts1[i]):
            sounde(2,True,ts1[i])
            sounde(5,True,ts1[i])
          for xs in range (4,270):
           with open("C:\lunarcreek\lunarcreek\Cult of Seal VN lines Final.docx","r") as fl:
            lines=(xs)
          self.sound=pygame.mixer.load(bm[1])
          channel1 = pygame.mixer.Channel(0)
          pygame.mixer.Channel.play()
          pygame.mixer.Channel.stop()
          self.dialogue=dialog(n,x2,y2)
def notebook(scence):
        if scence==4:
         pygame.time.set_timer(5000)
         pygame.gamestate.notebook
         pygame.display.text("News is different on the island")
         pygame.time.set_timer(3000)
         pygame.gamestate.NEXTlEVEL()
#0
Scence.Scence(imaged(1,2),dialog(2,4,15))
voice(5)
voice(4)
feeling(0,0,6,14)
feeling(10,2,8,15)
sounde(5,True,8)
sounde(0,True,8)
#1
Scence(imaged(3,3),SE(8),dialog(2,17,43))
feeling(14,2,23,25)
sounde(8,True,23)
voice(6)
voice(14)
#2
Scence(imaged(4,6),dialog(1,44,49))
voice(6)
choice=(input("Town Hall or Museum ?"))
if choice== 1:
  #3
  Scence(imaged(7,7),dialog(1,50,60))
  voice(7)
  feeling(5,0,54,60)
  sounde(4,True,54)
  sounde(5,True,54)
  image = pygame.image.load(c[27])
  X=400
  Y=400
  display_surface.blit(image, (0, 0))
  LayeredUpdates.move_to_front()
  LayeredUpdates.move_to_bacK()
  for i in range (225):
   pygame.background.fill((0,0,0))
   image = pygame.image.load(c[28,26])
   image.set_alpha(i)
   logoimage = pygame.screen.blit(image,(0,0))  
   pygame.display.flip()  
   display_surface.blit(image, (0, 0))
   LayeredUpdates.move_to_front()
   LayeredUpdates.move_to_bacK()
elif choice==2:
  #4
  Scence(imaged(10,15),dialog(2,61,84))
  sounde(2,True,78)
  sounde(5,True,78)
  voice(8)
  voice(16)
  feeling(5,0,76,83) 
  X=700
  for t in range (0,5):
   image = pygame.image.load(c[19])
   X-=100
   Y=400
   display_surface.blit(image, (0, 0))
   LayeredUpdates.move_to_front()
   LayeredUpdates.move_to_back()
  for i in range (225):
   pygame.background.fill((0,0,0))
   image = pygame.image.load(C[20])
   image.set_alpha(i)
   logoimage = pygame.screen.blit(image,(0,0))
   pygame.display.flip()
   display_surface.blit(image, (0, 0))
   LayeredUpdates.move_to_front()
#5
Scence(imaged(16,16),dialog(2,85,115))
voice(9)
voice(1)
sounde(4,True,90)
#114
if choice==1 and x1==114 and "________":
  print("doll")  
elif choice==2 and x1==114 and "________": 
  print ("statue")
feeling(3,0,95,106)
feeling(6,1,99,106)
#6
Scence(imaged(16,16),dialog(3,116,123))
voice(10)
voice(15)
feeling(8,1,119,122)
feeling(14,4,118,122)
sounde(3,True,119)
#6_5
scence(imaged(16,16),dialog(3,125,136))
feeling(15,5,127,129)
voice(17)
for p in range (0,9):
 channel1 = pygame.mixer.Channel(p+1)
 pygame.mixer.Channel.play()
 pygame.mixer.Channel.stop()
 voice(19)
 feeling(16,6,128,130)
 sounde(3,True,127)
voice(11)
#7
Scence(imaged(3,3),dialog([2,138,154]))
voice(12)
voice(2)
feeling(8,1,140,154)
sounde(3,True,140)
#8
Scence(image(17,19),dialog(3,156,270))
voice(13)
voice(3)
voice(18)
feeling(8,1,160,270)
feeling(5,0,192,195)
feeling(18,8,160,270)
sounde(3,True,160)
def save_btn(self, data, name):
        data_file = open(self.save_folder+"/"+name+self.file_extension, "wb")
        pickle.dump(data, data_file)
       
        if len(self.variables) > 1:
            return tuple(pickle.variables)
        else:
           for index, file in enumerate(self.data_to_save):
            self.save_data(file, pickle.file_names[index])
            return pickle.variables[0]
        return os.path.exists(self.save_folder+"/"+name+self.file_extension)
def load_btn(self, name):   
        data_file = open(self.save_folder+"/"+name+self.file_extension, "rb")
        data = pickle.load(data_file)
        variables = []
        for index, file in enumerate(self.files_to_load):
          if self.check_for_file(file):
            variables.append(self.load_data(file))
          else:
            variables.append(self.default_data[index])
          if len(variables) > 1:
            return tuple(variables)
          else:
            return variables[0]
        return data
def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """Returns surface with text written on"""
    font = pygame.freetype.SysFont("Gypsy_Curse.ttf", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()
def volume_btn (M):
    pygame.mixer.init()
    pygame.mixer.music.load(M)
    pygame.mixer.music.set_volume(input("volume? 0-.1.0"))
    pygame.mixer.music.play()

class Player:
    """Stores information about a player"""

    def __init__(self, score=0, current_level=1):
        self.score = score
        self.current_level = current_level

    image = pygame.image.load('b[0]')
def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    game_state = GameState.TITLE
    pygame.display.set_caption("Lunar Creek")

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        elif game_state == GameState.Options:
            game_state = options_screen(screen)
        elif game_state == GameState.Credits:
            game_state =Credits() 
        elif game_state == GameState.NEW_GAME:
            player = Player()
            game_state = play_level(screen, player)
        elif game_state == GameState.NEXT_LEVEL:
            player.current_level += 1
            game_state = play_level(screen, player)

        elif game_state == GameState.QUIT:
            pygame.quit()
            return


def title_screen(screen):
    t = UIElement(
        center_position=(300, 300),
        font_size=30,
        bg_rgb=Red,
        text_rgb=Orange,
        text="Lunar Creek",
        )
    options_btn = UIElement(
        center_position=(600, 500),
        font_size=30,
        bg_rgb=Red,
        text_rgb=Orange,
        text="Options",
        action=GameState.OPTIONS,
        )
    start_btn = UIElement(
        center_position=(600, 400),
        font_size=30,
        bg_rgb=Red,
        text_rgb=MB,
        text="Start",
        action=GameState.NEW_GAME,
        )
    quit_btn = UIElement(
        center_position=(600, 600),
        font_size=30,
        bg_rgb=Red,
        text_rgb=Purple,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = RenderUpdates(t,start_btn,options_btn, quit_btn)
    return game_loop(screen, buttons)
def options_screen(screen):
    volume_btn=UIElement(
        center_position=(400, 400),
        font_size=20,
        bg_rgb=Red,
        text_rgb=MB,
        text="To turn up /down volume",
        )
    save_btn=UIElement(
        center_position=(400,500),
        font_size=20,
        bg_rgb=white,
        text_rgb=MB,
        text="Save game",
        )
    load_btn=UIElement(
        center_position=(400, 600),
        font_size=20,
        bg_rgb=Red,
        text_rgb=MB,
        text="Load game",
       action=GameState.LOAD,
        )
    MM_btn=UIElement(
        center_position=(400,700),
        font_size=20,
        bg_rgb=Red,
        text_rgb=MB,
        text="main menu",
       action=GameState.TITLE,
        )
    credits_btn=UIElement(
       center_position=(400,800),
       font_size=20,
       bg_rgb=Red,
       text_rgb=MB,
       text="credits",
       action=GameState.Credits,
        )
     
    buttons = RenderUpdates(MM_btn,volume_btn,credits_btn, save_btn,load_btn)
    return game_loop(screen, buttons)
def Credits(screen):
    sound=pygame.mixer.load(bm[2])
    channel0 = pygame.mixer.Channel(0)
    pygame.mixer.Channel.play()
    pygame.mixer.Channel.stop() 
    with open("C:\lunarcreek\lunarcreek\Credits.docx","r") as fl:
     lines = [line.rstrip() for line in fl]
     
def play_level(screen, player):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=white,
        text_rgb=MB,
        text="Return to options",
        action=GameState.OPTIONS,
    )
    next_levelbtn = UIElement(  center_position=(140, 570),
        font_size=20,
        bg_rgb=white,
        text_rgb=MB,
        text="Return to options",
        action=GameState.NEXT_LEVEL,
    )
    buttons = RenderUpdates(return_btn,next_levelbtn )
    return game_loop(screen, buttons)

def game_loop(screen, buttons):
    """Handles game loop until an action is return by a button in the
    buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(white)
        display_surface.blit(image, (0, 0)) 
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
             return ui_action
        buttons.draw(screen)
        pygame.display.flip()
        pygame.mixer.music.stop()
        break
class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEW_GAME = 1
    NEXT_LEVEL = 2
    OPTIONS=3
    Notebook=4
    Credits=5
if __name__ == "__main__":
    main()