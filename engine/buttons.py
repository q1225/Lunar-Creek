import os
import pickle
from typing import Any
from GameState import*
import pygame
from Player import current_bg,line,current_level
from constants import SAVE_FOLDER
from engine.Player import Player
from engine.constants import ROOT
from main import background_images,File
file_extension=ROOT
variables = []
data_to_save=[]
default_data=[0,0,0]
lines= [lines.strip()for lines in File]
file=[Player.current_bg,Player.line,Player.current_level]
file_names=[background_images[file[0]],lines,Player.current_level]
def notebook(scence):

    if scence == 4:
        pygame.time.set_timer(5000)
        GameState.Notebook
        pygame.display.text("News is different on the island")
        pygame.time.set_timer(3000)        

def save_data(file,file_names):
  if default_data==file: 
     return default_data 
  else:
      return file
def save_btn(data: Any, name: str):
   data_file = open(SAVE_FOLDER + "/" + name +file_extension, "wb")
   pickle.dump(data, data_file)
   for index, file in enumerate(data_to_save):
       save_data(file, file_names[index])
       return os.path.exists(SAVE_FOLDER + "/" + name +file_extension)
   if len(variables) > 1:
        return tuple(variables)
files_to_load=data_to_save
def check_for_file(file):
  if file==files_to_load:
    load_data(file)  
  else: 
      return default_data
def load_data(name: str):
 variables = []
 for index, file in enumerate(files_to_load):
   with open(os.path.join(SAVE_FOLDER, f"{name}.data"), "rb") as data_file:
        return pickle.load(data_file)  
 if check_for_file(file):
           variables.append(load_data(file))
 else:
             variables.append(default_data[index])
 if len(variables) > 1:
            return tuple(variables)
 else:
            return variables[0]
   

def volume_btn(background_music: str):
    pygame.mixer.init()
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.set_volume(float(input("volume? 0.0 - 1.0")))
    pygame.mixer.music.play()
