import random


def day22(boss_hp, boss_dmg, hardcore=False):
    spells = {
        'Magic Missile': {'mana': 53, 'damage': 4, 'turns': 0, 'heal': 0, 'armor': 0, 'regen': 0},
        'Drain': {'mana': 73, 'damage': 2, 'turns': 0, 'heal': 2, 'armor': 0, 'regen': 0},
        'Shield': {'mana': 113, 'damage': 0, 'turns': 6, 'heal': 0, 'armor': 7, 'regen': 0},
        'Poison': {'mana': 173, 'damage': 3, 'turns': 6, 'heal': 0, 'armor': 0, 'regen': 0},
        'Recharge': {'mana': 229, 'damage': 0, 'turns': 5, 'heal': 0, 'armor': 0, 'regen': 101}
    }
    best_mana_use = 1E10

    # This needs to be relatively high for an answer to be found. Yeah, random brute force is painful.
    iterations = 100000000
    for _ in range(iterations):
        timers = {'Shield': 0, 'Poison': 0, 'Recharge': 0}
        hero_stats = {'mana': 500, 'hp': 50, 'armor': 0}
        boss_stats = {'hp': boss_hp, 'damage': boss_dmg}

        mana = simulation(spells, hero_stats, boss_stats, timers, hardcore)
        if mana < best_mana_use:
            best_mana_use = mana
    return best_mana_use


def simulation(spells, hero_stats, boss_stats, timers, hardcore):
    mana_use_counter = 0
    player_turn = True
    while True:
        start_turn(spells, hero_stats, boss_stats, timers)

        if player_turn:
            # hard mode has a -1 hp loss by the player per turn.
            if hardcore:
                hero_stats['hp'] -= 1
                if hero_stats['hp'] <= 0:
                    return 1E11

            # Choose a random spell, because it's the first way that came to mind.
            # Maybe BFS would have been better.
            spell_to_use = random.choice(list(spells.keys()))
            # If the spell is still active, we can't start it again.
            while spell_to_use not in ("Magic Missile", "Drain") and timers[spell_to_use] != 0:
                spell_to_use = random.choice(list(spells.keys()))
            mana_use_counter = use_spell(spells, hero_stats, boss_stats, timers, mana_use_counter, spell_to_use)
            if boss_stats['hp'] <= 0:
                return mana_use_counter
            if hero_stats['mana'] < 0:
                return 1E11
        else:  # boss's turn.
            damage_player(hero_stats, boss_stats['damage'])
            if hero_stats['hp'] <= 0:
                return 1E11
        end_turn(spells, hero_stats, timers)
        player_turn = not player_turn


def damage_player(hero_stats, boss_dmg):
    """
    Damages the player.
    """
    armor = hero_stats['armor']
    damage = max(1, boss_dmg - armor)
    hero_stats['hp'] -= damage


def use_spell(spells, hero_stats, boss_stats, timers, mana_use_counter, spell):
    """
    Casts the given spell and modifies global vars as necessary.
    """
    mana_cost = spells[spell]['mana']
    hero_stats['mana'] -= mana_cost
    if spell in ("Magic Missile", "Drain"):
        boss_damage = max(1, spells[spell]['damage'])
        boss_stats['hp'] -= boss_damage
    duration = spells[spell]['turns']
    hero_stats['hp'] += spells[spell]['heal']
    hero_stats['armor'] += spells[spell]['armor']
    mana_use_counter += mana_cost

    if duration > 0:
        timers[spell] += duration

    return mana_use_counter


def end_turn(spells, hero_stats, timers):
    """
    Does tasks as needed at the end of a turn, like applying damage from sustained spells.
    Also decrements turn counters for the sustained spells.
    """
    for k, v in timers.items():
        if k == "Shield" and timers[k] == 1:
            hero_stats['armor'] -= spells[k]['armor']


def start_turn(spells, hero_stats, boss_stats, timers):
    """
        Does tasks as needed at the end of a turn, like applying damage from sustained spells.
    """
    for k, v in timers.items():
        if v >= 1:
            timers[k] = v - 1
        if k == "Poison" and v > 0:
            damage = spells[k]['damage']
            boss_stats['hp'] -= damage
        if k == "Recharge" and v > 0:
            regen = spells[k]['regen']
            hero_stats['mana'] += regen
        if k == "Shield" and v > 0:
            pass
