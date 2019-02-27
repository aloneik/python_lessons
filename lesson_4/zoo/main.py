from sys import argv
import zoo


def add_animal_from_kwargs(park, kwargs):
    if "Name" not in kwargs:
        raise Exception("Animal Name must be specified")
    if "Type" not in kwargs:
        raise Exception("Animal Type must be specified")

    animal = None
    if kwargs["Type"] == "Mammal":
        animal = zoo.Mammal(kwargs["Name"])
        if "LitterSize" in kwargs:
            animal.LitterSize = kwargs["LitterSize"]
    elif kwargs["Type"] == "Reptile":
        animal = zoo.Reptile(kwargs["Name"])
        if "VenomousOrNot" in kwargs:
            animal.VenomousOrNot = bool(kwargs["VenomousOrNot"])
    elif kwargs["Type"] == "Bird":
        animal = zoo.Bird(kwargs["Name"])
        if "Wingspan" in kwargs:
            animal.Wingspan = kwargs["Wingspan"]
        if "TalksOrMute" in kwargs:
            animal.TalksOrMute = bool(kwargs["TalksOrMute"])

    if "Species" in kwargs:
        animal.spec = kwargs["Species"]
    if "Weight" in kwargs:
        animal.weight = kwargs["Weight"]
    if "Image" in kwargs:
        animal.image_path = kwargs["Image"]
    if "Voice" in kwargs:
        animal.voice_path = kwargs["Voice"]

    park.add_animal(animal)


def add_animal_from_file(park, filepath):
    with open(filepath) as file:
        for line in file:
            line = line.split()
            kwargs = {
                line[i][:-1]: line[i + 1] for i in range(1, len(line) - 1, 2)
                }
            add_animal_from_kwargs(park, kwargs)


z = zoo.Zoo()
if len(argv) > 1:
    if argv[1] == "Animal":
        kwargs = {
            argv[i][:-1]: argv[i + 1] for i in range(2, len(argv) - 1, 2)
            }
        add_animal_from_kwargs(z, kwargs)
    elif argv[1] == "File":
        add_animal_from_file(z, argv[2])

print z
