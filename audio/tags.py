from audio.tag import Tag
from audio.converters.mp3 import mp3_convert_tags
from audio.converters.mp4 import m4a_itunes_convert_tags
import mutagen
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

class Tags:

    filepath: str
    data: list[Tag]

    def __init__(self, filepath: str=''):
        self.filepath: str = filepath
        self.data = list[Tag]()
        audio_file = mutagen.File(filepath)
        match audio_file:
            case MP3(): self.data = mp3_convert_tags(audio_file)
            case MP4(): self.data = m4a_itunes_convert_tags(audio_file)
            case _: raise ValueError("Unsupported audio format")

    def has(self, key) -> bool:
        for item in self.data:
            if item.key == key:
                return True
        return False

    def add(self, tag: Tag):
        if not tag:
            raise "Attempt to add invalid tag"
        self.data.append(tag)

    def __repr__(self) -> str:
        res = ''
        for item in self.data:
            res += str(item) + '\n'
        return res
