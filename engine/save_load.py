
def save_btn(self, data, name):
    data_file = open(self.save_folder + "/" + name + self.file_extension, "wb")
    pickle.dump(data, data_file)
    for index, file in enumerate(data_to_save):
       self.save_data(file, file_names[index])
       return os.path.exists(self.save_folder + "/" + name + self.file_extension
    if len(variables) > 1:
        return tuple(variables)
    else:
        return variables[0]                       
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
                             
    def notebook(scence):
    if scence == 4:
        pygame.time.set_timer(5000)
        gamestate.notebook
        pygame.display.text("News is different on the island")
        pygame.time.set_timer(3000)
        
