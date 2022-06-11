from entities.base_entity import BaseEntity
import random
from helpers_and_utilities.verification_mixin import VerificationMixin
from resources.constants.names import ENEMY_NAMES, SPELL_NAMES
from items.spell import Spell

class Enemy(BaseEntity, VerificationMixin):
    def __init__(self, health: int = 1, mana: int = 0, damage: int = 0):
        super().__init__(health, mana)
        self.name = random.choice(ENEMY_NAMES)
        self.verify_attributes(damage)
        self.damage = damage
        self.spell = Spell.create_spell(random.choice(SPELL_NAMES))

    def attack(self):
        spell_is_most_powerful = self.damage <= self.spell.damage >= self.weapon.damage

        if spell_is_most_powerful and self.can_cast():
            self.reduce_mana()
            return self.spell.damage

        return max(self.weapon.damage, self.damage)

    @classmethod
    def spawn_enemy(cls):
        health = random.randint(1, 100)
        mana = random.randint(1, 100)
        damage = random.randint(1, 20)
        return cls(health=health, mana=mana, damage=damage)
