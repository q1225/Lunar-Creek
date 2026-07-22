import os
from typing import Iterable

from constants import ROOT


def create_media_array(media_folder: str, valid_extensions: Iterable[str]) -> list[str]:
    return [
        os.path.join(ROOT, media_folder, file)
        for file in os.listdir(os.path.join(ROOT, media_folder))
        if os.path.splitext(file)[1].lower() in valid_extensions
    ]


background_images = create_media_array("background_images", (".jpg", ".png"))
background_music = create_media_array("background_music", (".wav",))
sound_effects = create_media_array("sound_effects", (".wav",))
character_images = create_media_array("character_images", (".jpg", ".png"))
voice_acting = create_media_array("voice_acting", (".wav",))

File = "Cult_of_Seal_VN_lines_Final.txt"
