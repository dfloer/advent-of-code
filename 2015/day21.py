from collections import Iterable
from itertools import product, combinations
from math import ceil


shop_items = {'Weapons':
    {'Dagger': [8, 4, 0],
    'Shortsword': [10, 5, 0],
    'Warhammer': [25, 6, 0],
    'Longsword': [40, 7, 0],
    'Greataxe': [74, 8, 0]}
,
'Armor':
    {'None': [0, 0, 0],
    'Leather': [13, 0, 1],
    'Chainmail': [31, 0, 2],
    'Splintmail': [53, 0, 3],
    'Bandedmail': [75, 0, 4],
    'Platemail': [102, 0, 5]}
,
'Rings':
    {'None': [0, 0, 0],
    'Damage +1': [25, 1, 0],
    'Damage +2': [50, 2, 0],
    'Damage +3': [100, 3, 0],
    'Defense +1': [20, 0, 1],
    'Defense +2': [40, 0, 2],
    'Defense +3': [80, 0, 3]}
}


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, str):
            for sub in flatten(el):
                yield sub
        else:
            yield el


def day21(boss_hp=104, boss_damage=8, boss_armor=1):
    min_costs = []
    max_costs = []
    weapons = shop_items['Weapons']
    armors = shop_items['Armor']
    rings = shop_items['Rings']

    weapon_choices = weapons.keys()
    armor_choices = armors.keys()
    rings_choices = ['None'] + list(combinations(rings.keys(), 2))
    gear_choices = product(weapon_choices, armor_choices, rings_choices)
    for gear in gear_choices:
        gear = list(flatten(gear))
        weapon = weapons[gear[0]]
        armor = armors[gear[1]]
        ring1 = rings[gear[2]]
        ring2 = [0, 0, 0]
        if len(gear) == 4:
            ring2 = rings[gear[3]]
        cost, hero_damage, hero_armor = [sum(x) for x in zip(weapon, armor, ring1, ring2)]

        # if run_battle(boss_hp, boss_damage, boss_armor, 100, hero_damage, hero_armor):
        if calc_winner(boss_hp, boss_damage, boss_armor, 100, hero_damage, hero_armor):
            min_costs += [cost]
        else:
            max_costs += [cost]
    minimum = min(min_costs)
    maximum = max(max_costs)
    return minimum, maximum


def calc_winner(boss_hp, boss_damage, boss_armor, hero_hp, hero_damage, hero_armor):
    """
    Calculates the winner.
    """
    hero_turns = ceil(hero_hp / max(boss_damage - hero_armor, 1))
    boss_turns = ceil(boss_hp / max(hero_damage - boss_armor, 1))
    if hero_turns >= boss_turns:
        return True
    return False


def run_battle(boss_hp, boss_damage, boss_armor, hero_hp, hero_damage, hero_armor):
    """
    Runs the battle with the given stats. Returns True on a hero win, False on a boss win.
    """
    while True:
        # print(boss_hp, hero_hp)
        hero_hit = max(hero_damage - boss_armor, 1)
        boss_hp -= hero_hit
        if boss_hp <= 0:
            return True
        # print(boss_hp, hero_hp)
        boss_hit = max(boss_damage - hero_armor, 1)
        hero_hp -= boss_hit
        # print(boss_hp, hero_hp)
        if hero_hp <= 0:
            return False
