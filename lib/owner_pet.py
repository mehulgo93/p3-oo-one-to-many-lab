class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet_type. Allowed types are: {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all_pets.append(self)

    @classmethod
    def get_all_pets(cls):
        return cls.all_pets


class Owner:
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def pets(self):
        return self.owned_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet. Only instances of the Pet class can be added as pets.")
        pet.owner = self
        self.owned_pets.append(pet)

    def sort_pets_by_name(self):
        return sorted(self.owned_pets, key=lambda pet: pet.name)



