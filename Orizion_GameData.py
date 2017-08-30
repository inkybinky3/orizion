import os, random, sys

def give(x):
    for item in WEAPONS.values():
        if item.Name==x:
            item.Obtained="True"

def invCheck():
    x=1
    for item in WEAPONS.values():
        if item.Equipped=="True":
            currentWeapon=item
    print("Equipped:",currentWeapon.Name)
    print("")
    print("--- WEAPONS: ---")
    for item in WEAPONS.values():
        if item.Obtained=="True":
            print(str(x)+")",item.Name)
            x=x+1
    x=1
    print("")
    print("--- ITEMS: ---")
    for item in ITEMS.values():
        if item.Quantity>0:
            print(str(x)+")",item.Name)
            x=x+1
    print("_____________")
    print("___OPTIONS___")
    print("1> Change Equipped Weapon")
    print("2> Inspect Something")
    print("3> Save Progress")
    print("4> Exit")
    print("")
    z=input("[1/2/3/4]: ")
    z=str(z)
    if z=="1":
        success=0
        print("Enter the name of the weapon you would like to equip:")
        changeTo=input("[Weapon Name]: ")
        for item in WEAPONS.values():
            if item.Name==changeTo:
                if item.Obtained=="True":
                    currentWeapon.Equipped="False"
                    item.Equipped="True"
                    print("Changed Weapon Successfully!")
                    success=1
                else:
                    print("You do not have that weapon.")
        if success!=1:
            print("That is not a weapon.")
    elif z=="2":
        success=0
        print("1> Inspect A Weapon")
        print("2> Inspect An Item")
        tempVar=input("[1/2]: ")                    
        if tempVar=="1":
            
            print("")
            print("Enter the name of the weapon you would like to inspect:")
            inspect=input("[Weapon Name]: ")
            for item in WEAPONS.values():
                if item.Name==inspect:
                    if item.Obtained=="True":
                        print("___________________________________________________")
                        print("|",item.Name,"|"," ("+item.Type+")")
                        print("___________________________________________________")
                        print("")
                        print("'"+item.Description+"'")
                        print("")
                        print("Damage:",item.Damage)
                        print("Accuracy:",item.Accuracy)
                        print("")
                        success=1
                    else:
                        print("You do not have that weapon.")
        elif tempVar=="2":            
            print("")
            print("Enter the name of the item you would like to inspect:")
            inspect=input("[Item Name:] ")
            for item in ITEMS.values():
                if item.Name==inspect:
                    if item.Quantity>0:
                        print("___________________________________________________")
                        print("|",item.Name,"|"," ("+item.Type+")")
                        print("___________________________________________________")
                        print("")
                        print("'"+item.Description+"'")
                        print("")
                        print("You Have:",item.Quantity)
                        print("Sells for:",item.Value)
                        print("")
                        success=1
                    else:
                        print("You do not have that item.")
        else:
            print("Stopped Inspecting.")
        if success!=1:
            print("That is not a weapon or an item.")
    

####################################################################################################################################################################################
    

class weapon():
    def __init__(self, Name, Type, Description, Obtained, Equipped, Damage, Accuracy):
        self.Name=Name
        self.Type=Type
        self.Description=Description
        self.Obtained=Obtained
        self.Equipped=Equipped
        self.Damage=Damage
        self.Accuracy=Accuracy
        
WEAPONS = {

#LEGENDARY--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            "uber1":weapon("Sword Of The Almighty", "Legendary Sword", "One of the legendary swords. This one has an angelic design and a golden aura.", "False", "False", 100, 100),

            "uber2":weapon("Sword Of The Forgotten", "Legendary Sword", "One of the legendary swords. This one has a demonic design and a hellish aura.", "False", "False", 100, 100),

            "uber3":weapon("Sword Of The Freethinker", "Legendary Sword", "The secret legendary sword. This one has 'Lord Dawkins' enscribed into its blade.", "False", "False", 200, 100),

#SWORDS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
            "sword1":weapon("Wooden Sword", "Sword", "A reinforced stick that somewhat resembles a sword. Might as well call it a sword.", "True", "True", 10, 100),
            
            "sword2":weapon("Standard Sword", "Sword", "A sword that's so basic, it even tastes like Vanilla. Probably shouldn't lick it though.", "False", "False", 20, 100),

            "sword3":weapon("Long Sword", "Sword", "A long sword. You know you're only weilding it to compensate for something.", "False", "False", 30, 100),

            "sword4":weapon("Rapier", "Sword", "A slim bladed sword for the nimblest of swordsman. Sadly, it's you wielding it, instead.", "False", "False", 20, 100),           

#AXES-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            "axe1":weapon("Steel Axe", "Axe", "A brutal looking axe that has a terrifying edge. You definitely don't want to be hit with this.", "False", "False", 20, 90),

            "axe2":weapon("Handheld Guillotine", "Axe", "Heads will roll... The person who made this must have been slightly insane.", "False", "False", 30, 90),          

#KNIVES-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            "knife1":weapon("Butter Knife", "Knife", "A basic butter knife. At least it's stainless, so the blood slides off.", "True", "False", 5, 100),

            "knife2":weapon("Dagger Knife", "Knife", "A sharp knife with black tape around the handle. You mess with crabo, you get a stabo!", "False", "False", 15, 100),

#SCYTHES----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            "scythe1":weapon("Spooky Scythe", "Scythe", "A scythe with a shiny blade. It's looks quite rare. Perhaps you can pretend you're the Grim Reaper.", "False", "False", 40, 100),

#BOWS-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            "bow1":weapon("Wooden Bow", "Bow", "A basic looking bow with a simplistic design. KITTY knows why it has infinite arrows...", "False", "False", 20, 80),

#FLAILS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            "flail1":weapon("Makeshift Flail", "Flail", "You have a ball. You have a stick. That's everything required to have a good time.", "False", "False", 30, 50),

            "flail2":weapon("Military Flail", "Flail", "Swing drunkenly and pray you'll kill your enemies before you kill yourself. No, it's not just luck!", "False", "False", 50, 50)
           
            }
####################################################################################################################################################################################

class item():
    def __init__(self, Name, Type, Description, Quantity, Value):
        self.Name=Name
        self.Type=Type
        self.Description=Description
        self.Quantity=Quantity
        self.Value=Value

ITEMS = {

#COMMON-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    "coin1":item("Copper Coin", "Common Item", "A rusty old coin. Perhaps you should sell it?", 1, 10),

    "coin2":item("Silver Coin", "Common Item", "A shiny coin with interesting markings. Perhaps you should sell it?", 0, 50),

    "coin3":item("Golden Coin", "Common Item", "A lustorous coin with merticulous markings. Perhaps you should sell it? Or gloat about it... your choice.", 0, 150),

#RARE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    "potato1":item("Crystalised Potato", "Rare Item", "A phenomenal potato made from a mixture of diamond and carbon fibre.", 1, "False")

#UBER RARE--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        }
