import os
import pickle

import pygame


def save_btn(self, data, name):
    data_file = open(self.save_folder + "/" + name + self.file_extension, "wb")
    pickle.dump(data, data_file)
    return os.path.exists(self.save_folder + "/" + name + self.file_extension)
    # if len(variables) > 1:
    #     return tuple(variables)
    # else:
    #     return variables[0]
    # for index, file in enumerate(data_to_save):
    #     self.save_data(file, file_names[index])


def load_btn(self, name):
    data_file = open(self.save_folder + "/" + name + self.file_extension, "rb")
    data = pickle.load(data_file)
    return data
    # variables = []
    # for index, file in enumerate(files_to_load):
    #     if self.check_for_file(file):
    #         variables.append(self.load_data(file))
    #     else:
    #         variables.append(default_data[index])
    #     if len(variables) > 1:
    #         return tuple(variables)
    #     else:
    #         return variables[0]


def volume_btn(background_music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.set_volume(float(input("volume? 0.0 - 1.0")))
    pygame.mixer.music.play()
