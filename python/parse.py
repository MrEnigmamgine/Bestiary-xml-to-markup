import xml.etree.ElementTree as ET  
xmlp = ET.XMLParser(encoding='ISO-8859-1')

tree= ET.parse('db.xml',parser=xmlp)
root = tree.getroot()
npcdata = root.find('reference/npcdata')

if(npcdata.find('balhannoth')):
    for npc in npcdata:
        if(npc.find('name')):
            name = npc.find('name').text
            print(name)
        npctype = npc.find('type').text # I think "type" is a reserved word
        size = npc.find('size').text
        alignment = npc.find('alignment').text
        ac = npc.find('ac').text
        actext = npc.find('actext').text
        hp = npc.find('hp').text
        hd = npc.find('hd').text
        speed = npc.find('speed').text
        strength = npc.find('abilities/strength/score').text
        strengthmod = npc.find('abilities/strength/bonus').text
        dexterity = npc.find('abilities/dexterity/score').text
        dexteritymod = npc.find('abilities/dexterity/bonus').text
        constitution = npc.find('abilities/constitution/score').text
        constitutionmod = npc.find('abilities/constitution/bonus').text
        wisdom = npc.find('abilities/wisdom/score').text
        wisdommod = npc.find('abilities/wisdom/bonus').text
        charisma = npc.find('abilities/charisma/score').text
        charismamod = npc.find('abilities/charisma/bonus').text
        print(npc.find('skills'),npc)
        if(npc.find('skills')):
            print("I found it!")
    # savingthrows = npc.find('savingthrows').text
    #  skills = npc.find('skills').text
    #  conditionimmunities = npc.find('conditionimmunities').text
        senses = npc.find('senses').text
    #  languages = npc.find('languages').text
        cr = npc.find('cr').text
        xp = npc.find('xp').text

        


#for child in root:
#        print(att.tag, att.value)
#    for att in child.iter('name'):
#/

#print(root[0].find('name').text)
#for actions in root[0].find('actions'):
#    print(actions.find('name').text)
#    print(actions.find('desc').text)
