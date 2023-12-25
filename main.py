sap_wiki = open("SAP_wiki_pets_page.txt", "r")
line = sap_wiki.readline()
pets = []
current_tier = 0
while line != '':
    if "<!-- TIER " in line:
        current_tier += 1
    if line == "{{:Pets/row\n":
        line = sap_wiki.readline()
        pet = {
            'name': line[18:line[18:].find('|') + 18],
            'tier': current_tier
        }
        line = sap_wiki.readline()
        pet['attack'] = int(line[11:line.find('| health = ')])
        pet['health'] = int(line[line.find('| health = ') + 11:].strip())
        line = sap_wiki.readline()
        packs = line[2:].split(' | ')
        for i in range(len(packs)):
            packs[i].strip()
            packs[i] = packs[i][:packs[i].find('pack')]
            packs[i] = packs[i][0].upper() + packs[i][1:] + ' Pack'
        pet['pack'] = packs
        pets.append(pet)
        line = sap_wiki.readline()
        lvl1 = 'Other'
        if "''' â†" in line:
            lvl1 = line[5:line.find("''' â†")]
        line = sap_wiki.readline()
        lvl2 = 'Other'
        if "''' â†" in line:
            lvl2 = line[5:line.find("''' â†")]
        line = sap_wiki.readline()
        lvl3 = 'Other'
        if "''' â†" in line:
            lvl3 = line[5:line.find("''' â†")]
        ability = 'Mixed'
        if lvl1 == lvl2 == lvl3:
            ability = lvl1
        pet['ability'] = ability
        print(pet)
    line = sap_wiki.readline()

print(pets)
