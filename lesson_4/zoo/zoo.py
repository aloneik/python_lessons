from abc import ABCMeta  # , abstractmethod
from PIL import Image
import winsound
import pickle


class Animal():
    __metaclass__ = ABCMeta

    def __init__(
        self,
        name=None, type_=None, spec=None, weight=None,
        image_path=None, voice_path=None
            ):
        self.name = name
        self.type_ = type_
        self.spec = spec
        self.weight = weight
        self.image_path = image_path
        self.voice_path = voice_path

    def get_name(self):
        return self.name

    def show_image(self):
        with Image.open(self.image_path) as img:
            img.show()

    def play_voice(self):
        winsound.PlaySound(self.voice_path, winsound.SND_FILENAME)


class Mammal(Animal):
    def __init__(
        self, name, spec=None, weight=None,
        image_path=None, voice_path=None, LitterSize=1
            ):
        Animal.__init__(
            self, name, "Mammal", spec, weight, image_path, voice_path
            )
        if LitterSize < 1:
            raise ValueError("litter size must be >= 1")
        self.LitterSize = LitterSize

    def __str__(self):
        return "{0} {1} {2} {3} ({4}, {5}, {6})".format(
            self.name,
            self.type_,
            self.spec,
            self.weight,
            self.LitterSize,
            self.image_path,
            self.voice_path
        )


class Reptile(Animal):
    def __init__(
        self, name, spec=None, weight=None,
        image_path=None, voice_path=None, VenomousOrNot=None
            ):
        Animal.__init__(
            self, name, "Reptile", spec, weight, image_path, voice_path
            )
        self.VenomousOrNot = VenomousOrNot

    def __str__(self):
        return "{0} {1} {2} {3} ({4}, {5}, {6})".format(
            self.name,
            self.type_,
            self.spec,
            self.weight,
            self.VenomousOrNot,
            self.image_path,
            self.voice_path
        )


class Bird(Animal):
    def __init__(
        self, name, spec=None, weight=None,
        image_path=None, voice_path=None,
        Wingspan=1, TalksOrMute=None
            ):
        Animal.__init__(
            self, name, "Bird", spec, weight, image_path, voice_path
            )
        if Wingspan < 1:
            raise ValueError("Wingspan must be >= 1")
        self.Wingspan = Wingspan
        self.TalksOrMute = TalksOrMute

    def __str__(self):
        return "{0} {1} {2} {3} ({4}, {5}, {6}, {7})".format(
            self.name,
            self.type_,
            self.spec,
            self.weight,
            self.Wingspan,
            self.TalksOrMute,
            self.image_path,
            self.voice_path
        )


class Zoo():
    def __init__(self, animals=[]):
        self.animals = list(animals)

    def __iter__(self):
        return iter(self.animals)

    def __str__(self):
        string_repr = ""
        for animal in self:
            string_repr = string_repr + str(animal) + "\n"
        return string_repr

    def add_animal(self, animal):
        self.animals.append(animal)

    def save_to_file(self, filepath):
        with open(filepath, "wb") as file:
            pickle.dump(self, file)


if __name__ == "__main__":
    m = Mammal(
        "antosha", "bear", 200,
        "f:/max/python/python_lessons-master/lesson_4/zoo/bimg.png",
        "f:/max/python/python_lessons-master/lesson_4/zoo/bv.wav",
        2
        )

    b = Bird(
        "petya", "eagle", 4,
        "f:/max/python/python_lessons-master/lesson_4/zoo/bimg.png",
        "f:/max/python/python_lessons-master/lesson_4/zoo/bv.wav",
        3, True
    )

    r = Reptile(
        "andrei", "snake", 2,
        "f:/max/python/python_lessons-master/lesson_4/zoo/bimg.png",
        "f:/max/python/python_lessons-master/lesson_4/zoo/bv.wav",
        False
    )

    print m
    print b
    print r
