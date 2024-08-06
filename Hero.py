class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health = health
        self.catchphrase = catchphrase

    def prints_name(self):
        print(self.name)

    def double_health(self):
        self.health *= 2

    def __str__(self):
        return (f"{self.nickname}\n  "
                f"Суперспособность:{self.superpower}\n "
                f"Здоровье: {self.health}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero(name="Рексар", nickname="Повелитель зверей", superpower="призывать животных", health=100,
                 catchphrase="Смелее мой юный друг!")
hero.prints_name()
print(hero)
hero.double_health()
print("здоровье после баффа:",hero.health)
print(len(hero))