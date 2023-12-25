from random import randint

sap_wiki = open("SAP_wiki_pets_page.txt", "r")

TIER_INDICATOR = "<!-- TIER "
PET_INDICATOR = "{{:Pets/row\n"
NAME_INDEX = 18
NAME_SEP = '|'
ATTACK_INDEX = 11
HEALTH_INDICATOR = '| health = '
PACK_SEP = ' | '
PACK_INDICATOR = 'pack'
ABILITY_INDICATOR = "''' â†"

line = sap_wiki.readline()
pets = []
current_tier = 0
while line != '':
    if TIER_INDICATOR in line:
        current_tier += 1
    if line == PET_INDICATOR:
        line = sap_wiki.readline()
        pet = {
            'name': line[NAME_INDEX:line[NAME_INDEX:].find(NAME_SEP) + NAME_INDEX],
            'tier': current_tier
        }
        line = sap_wiki.readline()
        pet['attack'] = int(line[ATTACK_INDEX:line.find(HEALTH_INDICATOR)])
        pet['health'] = int(line[line.find(HEALTH_INDICATOR) + ATTACK_INDEX:].strip())
        line = sap_wiki.readline()
        packs = line[2:].split(PACK_SEP)
        for i in range(len(packs)):
            packs[i].strip()
            packs[i] = packs[i][:packs[i].find(PACK_INDICATOR)]
            packs[i] = packs[i][0].upper() + packs[i][1:] + ' Pack'
        pet['pack'] = packs
        pets.append(pet)
        line = sap_wiki.readline()
        lvl1 = 'Other'
        if ABILITY_INDICATOR in line:
            lvl1 = line[5:line.find(ABILITY_INDICATOR)]
        line = sap_wiki.readline()
        lvl2 = 'Other'
        if ABILITY_INDICATOR in line:
            lvl2 = line[5:line.find(ABILITY_INDICATOR)]
        line = sap_wiki.readline()
        lvl3 = 'Other'
        if ABILITY_INDICATOR in line:
            lvl3 = line[5:line.find(ABILITY_INDICATOR)]
        ability = 'Mixed'
        if lvl1 == lvl2 == lvl3:
            ability = lvl1
        pet['ability'] = ability
        print(pet)
    line = sap_wiki.readline()

print(pets)
print(pets[randint(1, 254)])
