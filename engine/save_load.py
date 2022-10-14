import os
import pickle
from typing import Any

from constants import SAVE_FOLDER


def save_btn(data: Any, name: str):
    with open(os.path.join(SAVE_FOLDER, f"{name}.data"), "wb") as data_file:
        pickle.dump(data, data_file)

    return os.path.exists(os.path.join(SAVE_FOLDER, f"{name}.data"))
    
    # if len(variables) > 1:
    #     return tuple(variables)
    # else:
    #     return variables[0]
    # for index, file in enumerate(data_to_save):
    #     self.save_data(file, file_names[index])


def load_btn(name: str):
    with open(os.path.join(SAVE_FOLDER, f"{name}.data"), "rb") as data_file:
        return pickle.load(data_file)

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
