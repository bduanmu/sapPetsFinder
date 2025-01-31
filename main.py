import random
import requests as requests
from bs4 import BeautifulSoup

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
ICON_INDICATOR = "{{IconSAP|"
ICON_END = "}}"

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
            packs[i] = (packs[i][0].upper() + packs[i][1:]).rstrip("custom") + ' Pack'
        if "Weekly Pack" in packs and len(packs) != 1:
            packs.remove("Weekly Pack")
        pet['pack'] = packs
        pets.append(pet)
        line = sap_wiki.readline()
        lvl1 = 'Other'
        if ABILITY_INDICATOR in line:
            lvl1 = line[5:line.find(ABILITY_INDICATOR)]
            if ICON_INDICATOR in lvl1:
                lvl1 = lvl1[:lvl1.find(ICON_INDICATOR)] + lvl1[lvl1.find(ICON_INDICATOR) + len(ICON_INDICATOR):lvl1.find(ICON_END)] + lvl1[lvl1.find(ICON_END) + len(ICON_END):]
        line = sap_wiki.readline()
        lvl2 = 'Other'
        if ABILITY_INDICATOR in line:
            lvl2 = line[5:line.find(ABILITY_INDICATOR)]
            if ICON_INDICATOR in lvl2:
                lvl2 = lvl2[:lvl2.find(ICON_INDICATOR)] + lvl2[lvl2.find(ICON_INDICATOR) + len(ICON_INDICATOR):lvl2.find(ICON_END)] + lvl2[lvl2.find(ICON_END) + len(ICON_END):]
        line = sap_wiki.readline()
        lvl3 = 'Other'
        if ABILITY_INDICATOR in line:
            lvl3 = line[5:line.find(ABILITY_INDICATOR)]
            if ICON_INDICATOR in lvl3:
                lvl3 = lvl3[:lvl3.find(ICON_INDICATOR)] + lvl3[lvl3.find(ICON_INDICATOR) + len(ICON_INDICATOR):lvl3.find(ICON_END)] + lvl3[lvl3.find(ICON_END) + len(ICON_END):]
        ability = 'Mixed'
        if lvl1 == lvl2 == lvl3:
            ability = lvl1
        pet['ability'] = ability
        print(pet)
    line = sap_wiki.readline()

print(pets)
pet_names = [pet['name'] for pet in pets]
print(pet_names)
print([pet['name'].lower() for pet in pets])
print(pets[random.randint(1, 254)])
answer_list = [i for i in range(len(pets))]
random.shuffle(answer_list)
print(answer_list)

max_length = 0
max_name = []
for name in pet_names:
    if len(name) > max_length:
        max_name = [name]
        max_length = len(name)
    elif len(name) == max_length:
        max_name.append(name)
print(max_name)

IMAGE_LINK_INDICATOR = 'src="/images'

result = requests.get("https://superautopets.wiki.gg/wiki/File:Mantis Shrimp.png")
doc = BeautifulSoup(result.text, 'html.parser')
images = doc.find_all("img")
# print(images)
pet_images = []
for pet_name in pet_names:
    URL = "https://superautopets.wiki.gg/wiki/File:" + pet_name + ".png"
    result = requests.get(URL)
    doc = BeautifulSoup(result.text, 'html.parser')
    # beg_ind = doc.find(IMAGE_LINK_INDICATOR)
    # print(beg_ind)
    # pet_images.append("https://superautopets.wiki.gg" + doc[beg_ind + 5:doc.find('?', beg_ind + len(IMAGE_LINK_INDICATOR) + 1)])
    # print(URL)

    name = doc.find_all("img")[1]['src']
    pet_images.append("https://superautopets.wiki.gg" + name[:name.find('?')])
    print(name[:name.find('?')])

print(pet_images)
