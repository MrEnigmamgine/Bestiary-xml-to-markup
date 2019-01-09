import xml.etree.ElementTree as ET  
import time
xmlp = ET.XMLParser(encoding='ISO-8859-1')

tree= ET.parse('db.xml',parser=xmlp)
root = tree.getroot()
npcdata = root.find('reference/npcdata')

for npc in npcdata:
    file= open('./test/'+npc.tag+'.markdown','w+')
    name = npc.find('name').text        
    npctype = npc.find('type').text # I think "type" is a reserved word
    size = str(npc.find('size').text)
    alignment = npc.find('alignment').text
    ac = str(npc.find('ac').text)
    actext = '' #Element always exists, but is not always populated with data
    if(not npc.find('actext').text is None):
        actext = npc.find('actext').text
    hp = npc.find('hp').text
    hd = npc.find('hd').text
    speed = npc.find('speed').text

    def addplus(string): #Check if the modifier is above zero and if so add a plus sign to it
        num = int(string)
        return "+"+string if num > 0 else string

    strength = npc.find('abilities/strength/score').text #I think 'str' is reserved
    strmod = addplus(npc.find('abilities/strength/bonus').text)
    dex = npc.find('abilities/dexterity/score').text
    dexmod = addplus(npc.find('abilities/dexterity/bonus').text)
    con = npc.find('abilities/constitution/score').text
    conmod = addplus(npc.find('abilities/constitution/bonus').text)
    intel = npc.find('abilities/intelligence/score').text
    intmod = addplus(npc.find('abilities/intelligence/bonus').text)
    wis = npc.find('abilities/wisdom/score').text
    wismod = addplus(npc.find('abilities/wisdom/bonus').text)
    cha = npc.find('abilities/charisma/score').text
    chamod = addplus(npc.find('abilities/charisma/bonus').text)
    cr = npc.find('cr').text
    senses = npc.find('senses').text
    languages = npc.find('languages').text
    xp = npc.find('xp').text

    file.write(
        '---\nlayout: post\n'+
        'title: "'+name+'"\n'+
        'date: '+time.strftime("%Y-%m-%d")+'\n'+
        'tags: ['+size.lower()+', '+npctype.split(' ')[0]+', cr'+cr+', mordenkainens-tome-of-foes]\n'+
        'page_number: 999\n'+
        '---\n\n'+
        '**'+size+' '+npctype+', '+alignment+'**\n\n'+
        '**Armor Class** '+ac+' '+actext+'\n\n'+
        '**Hit Points** '+hp+'  '+hd+'\n\n'+
        '**Speed** '+speed+'\n\n'+
        '|   STR   |   DEX   |   CON   |   INT   |   WIS   |   CHA   |\n'+
        '|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|\n'+
        '| '+strength+' ('+strmod+') | '+dex+' ('+dexmod+') | '+con+' ('+conmod+') | '+intel+' ('+intmod+') | '+wis+' ('+wismod+') | '+cha+' ('+chamod+') |\n\n'
        )

    if(not npc.find('savingthrows') is None):   
        savingthrows = npc.find('savingthrows').text
        file.write('**Saving Throws** '+savingthrows+'\n\n')
    if(not npc.find('skills') is None):
        skills = npc.find('skills').text
        file.write('**Skills** '+skills+'\n\n')
    if(not npc.find('damageresistances') is None):
        damageresistances = npc.find('damageresistances').text
        file.write('**Damage Resistances** '+damageresistances+'\n\n')
    if(not npc.find('damageimmunities') is None):
        damageimmunities = npc.find('damageimmunities').text
        file.write('**Damage Immunities** '+damageimmunities+'\n\n')
    if(not npc.find('conditionimmunities') is None):
        conditionimmunities = npc.find('conditionimmunities').text
        file.write('**Condition Immunities** '+conditionimmunities+'\n\n')

    file.write(
        '**Senses** '+senses+'\n\n'+
        '**Languages** '+languages+'\n\n'+
        '**Challenge** '+cr+' ('+xp+' XP)'
    )
    
    if(not npc.find('traits') is None):
        for child in npc.find('traits'):
            childname = str(child.find('name').text)
            childdesc = str(child.find('desc').text)
            file.write('\n\n***'+childname+'.*** '+childdesc)
    if(not npc.find('actions') is None):
        file.write('\n\n**Actions**')
        for child in npc.find('actions'):
            childname = str(child.find('name').text)
            childdesc = str(child.find('desc').text)
            file.write('\n\n***'+childname+'*** '+childdesc)
    if(not npc.find('legendaryactions') is None):
        file.write('\n\n**Legendary Actions**')
        for child in npc.find('legendaryactions'):
            childname = str(child.find('name').text)
            childdesc = str(child.find('desc').text)
            if(childname == 'Options'):
                file.write('\n\n'+childdesc)
            else:
                file.write('\n\n***'+childname+'*** '+childdesc)
    file.close()