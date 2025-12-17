class Animal:
    def __init__(self, animal_id, name, species, age, health_status, adopted=False):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.health_status = health_status
        self.adopted = adopted

    def mark_adopted(self):
        self.adopted = True

    def __str__(self):
        status = "Adopted" if self.adopted else "Available"
        return f"{self.animal_id}: {self.name} ({self.species}, {self.age} yrs) - {status}"
