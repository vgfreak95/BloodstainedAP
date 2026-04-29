from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import RitualWorld

class RitualItemCategory(Enum):
    # Items
    POTION = "Potion",
    INGREDIENT = "Ingredient",
    FOOD = "Food",
    FOODSTUFF = "FoodStuff",
    KEY = "Key"
    MONEY = "Money"

    # Equipment
    WEAPON = "Weapon",
    BULLET = "Bullet",
    HEAD = "Head",
    BODY = "Body",
    ACCESSORY1 = "Accessory1",
    MUFFLER = "Muffler"

    # Shard types
    SKILL = "Skill"
    DIRECTIONALSHARD = "DirectionalShard"
    TRIGGERSHARD = "TriggerShard"
    EFFECTIVESHARD = "EffectiveShard"
    FAMILIARSHARD = "FamiliarShard"

    #Stat Upgrades
    STAT_UPGRADE = "Stat Upgrade"


@dataclass
class RitualItemData:
    id: int
    name: str
    count: int
    category: RitualItemCategory
    classification: ItemClassification

CHEST_AND_WALL_ITEMS = {
    "Potion": RitualItemData(id=0xb100d, name="Potion", count=5, category=RitualItemCategory.POTION, classification=ItemClassification.useful),
    "High Potion": RitualItemData(id=0xb100e, name="High Potion", count=2, category=RitualItemCategory.POTION, classification=ItemClassification.useful),
    "Ether": RitualItemData(id=0xb100f, name="Ether", count=2, category=RitualItemCategory.POTION, classification=ItemClassification.useful),
    "Mithridate": RitualItemData(id=0xb1010, name="Mithridate", count=17, category=RitualItemCategory.POTION, classification=ItemClassification.useful),
    "Waystone": RitualItemData(id=0xb1011, name="Waystone", count=16, category=RitualItemCategory.POTION, classification=ItemClassification.useful),
    "Bronze": RitualItemData(id=0xb1012, name="Bronze", count=6, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Iron": RitualItemData(id=0xb1013, name="Iron", count=6, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Obsidian": RitualItemData(id=0xb1014, name="Obsidian", count=4, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Steel": RitualItemData(id=0xb1015, name="Steel", count=4, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Silver": RitualItemData(id=0xb1016, name="Silver", count=7, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Damascus": RitualItemData(id=0xb1017, name="Damascus", count=5, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Mithril": RitualItemData(id=0xb1018, name="Mithril", count=11, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Platinum": RitualItemData(id=0xb1019, name="Platinum", count=24, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Crystal": RitualItemData(id=0xb101a, name="Crystal", count=52 - 26, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Gold": RitualItemData(id=0xb101b, name="Gold", count=12, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Crimsonite": RitualItemData(id=0xb101c, name="Crimsonite", count=3, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Orichalcum": RitualItemData(id=0xb101d, name="Orichalcum", count=11, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Cotton": RitualItemData(id=0xb101e, name="Cotton", count=5, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Hemp": RitualItemData(id=0xb101f, name="Hemp", count=4, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Wool": RitualItemData(id=0xb1020, name="Wool", count=8, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Silk": RitualItemData(id=0xb1021, name="Silk", count=9, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Cashmere": RitualItemData(id=0xb1022, name="Cashmere", count=11, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Halite": RitualItemData(id=0xb1023, name="Halite", count=4, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Elm": RitualItemData(id=0xb1024, name="Elm", count=5, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Oak": RitualItemData(id=0xb1025, name="Oak", count=4, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Walnut": RitualItemData(id=0xb1026, name="Walnut", count=5, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Mahogany": RitualItemData(id=0xb1027, name="Mahogany", count=32, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Cypress": RitualItemData(id=0xb1028, name="Cypress", count=6, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Ruby": RitualItemData(id=0xb1029, name="Ruby", count=17, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Sapphire": RitualItemData(id=0xb102a, name="Sapphire", count=12, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Emerald": RitualItemData(id=0xb102b, name="Emerald", count=12, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Diamond": RitualItemData(id=0xb102c, name="Diamond", count=21, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Alexandrite": RitualItemData(id=0xb102d, name="Alexandrite", count=23, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "8-bit Coin": RitualItemData(id=0xb102e, name="8-bit Coin", count=1, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "8-bit Nightmare": RitualItemData(id=0xb102f, name="8-bit Nightmare", count=1, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Kung Fu Shoes": RitualItemData(id=0xb1033, name="Kung Fu Shoes", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Lethal Boots": RitualItemData(id=0xb1034, name="Lethal Boots", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Knife": RitualItemData(id=0xb1035, name="Knife", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Baselard": RitualItemData(id=0xb1036, name="Baselard", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Short Sword": RitualItemData(id=0xb1037, name="Short Sword", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Ulfberht Sword": RitualItemData(id=0xb1038, name="Ulfberht Sword", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Invisible Blade": RitualItemData(id=0xb1039, name="Invisible Blade", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Red Umbrella": RitualItemData(id=0xb103a, name="Red Umbrella", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Blutgang": RitualItemData(id=0xb103b, name="Blutgang", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Fragarach": RitualItemData(id=0xb103c, name="Fragarach", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Valkyrie Sword": RitualItemData(id=0xb103d, name="Valkyrie Sword", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Morgenstern": RitualItemData(id=0xb103e, name="Morgenstern", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Macuahuitl": RitualItemData(id=0xb103f, name="Macuahuitl", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Flying Edge": RitualItemData(id=0xb1040, name="Flying Edge", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Claymore": RitualItemData(id=0xb1041, name="Claymore", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Carnot's Rebuke": RitualItemData(id=0xb1042, name="Carnot's Rebuke", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Gram": RitualItemData(id=0xb1043, name="Gram", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Lohengrin": RitualItemData(id=0xb1044, name="Lohengrin", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Steel Lightning": RitualItemData(id=0xb1045, name="Steel Lightning", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Honebami": RitualItemData(id=0xb1046, name="Honebami", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Swordfish": RitualItemData(id=0xb1047, name="Swordfish", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Zangetsuto": RitualItemData(id=0xb1048, name="Zangetsuto", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.progression),
    "Partisan": RitualItemData(id=0xb1049, name="Partisan", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Sanjiegun": RitualItemData(id=0xb104a, name="Sanjiegun", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Whip": RitualItemData(id=0xb104b, name="Whip", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Musketoon": RitualItemData(id=0xb104c, name="Musketoon", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Blunderbuss": RitualItemData(id=0xb104d, name="Blunderbuss", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Culverin": RitualItemData(id=0xb104e, name="Culverin", count=1, category=RitualItemCategory.WEAPON, classification=ItemClassification.useful),
    "Hairband": RitualItemData(id=0xb104f, name="Hairband", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Pirate Hat": RitualItemData(id=0xb1050, name="Pirate Hat", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Santa Hat": RitualItemData(id=0xb1051, name="Santa Hat", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Beast Beret": RitualItemData(id=0xb1052, name="Beast Beret", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Thunder Circlet": RitualItemData(id=0xb1053, name="Thunder Circlet", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Crow Hat": RitualItemData(id=0xb1054, name="Crow Hat", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Gadget Band": RitualItemData(id=0xb1055, name="Gadget Band", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Feather Crown": RitualItemData(id=0xb1056, name="Feather Crown", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Diabolist's Cap": RitualItemData(id=0xb1057, name="Diabolist's Cap", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Traveler's Hat": RitualItemData(id=0xb1058, name="Traveler's Hat", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Kitsune Mask": RitualItemData(id=0xb1059, name="Kitsune Mask", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Valkyrie Tiara": RitualItemData(id=0xb105a, name="Valkyrie Tiara", count=1, category=RitualItemCategory.HEAD, classification=ItemClassification.useful),
    "Tattered Scarf": RitualItemData(id=0xb105b, name="Tattered Scarf", count=1, category=RitualItemCategory.MUFFLER, classification=ItemClassification.useful),
    "Faerie Scarf": RitualItemData(id=0xb105c, name="Faerie Scarf", count=1, category=RitualItemCategory.MUFFLER, classification=ItemClassification.useful),
    "Flame Scarf": RitualItemData(id=0xb105d, name="Flame Scarf", count=1, category=RitualItemCategory.MUFFLER, classification=ItemClassification.useful),
    "Talisman Scarf": RitualItemData(id=0xb105e, name="Talisman Scarf", count=1, category=RitualItemCategory.MUFFLER, classification=ItemClassification.useful),
    "Elf Ears": RitualItemData(id=0xb105f, name="Elf Ears", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Crow Mask": RitualItemData(id=0xb1060, name="Crow Mask", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Sunglasses": RitualItemData(id=0xb1061, name="Sunglasses", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Dance Mask": RitualItemData(id=0xb1062, name="Dance Mask", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Hyperventilator": RitualItemData(id=0xb1063, name="Hyperventilator", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Gauge Glasses": RitualItemData(id=0xb1064, name="Gauge Glasses", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Nose Glasses": RitualItemData(id=0xb1065, name="Nose Glasses", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Voice Changer": RitualItemData(id=0xb1066, name="Voice Changer", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Ofuda Talisman": RitualItemData(id=0xb1067, name="Ofuda Talisman", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Gebel's Glasses": RitualItemData(id=0xb1068, name="Gebel's Glasses", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Rusted Ring": RitualItemData(id=0xb1069, name="Rusted Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Safe Ring": RitualItemData(id=0xb106a, name="Safe Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Unicorn Ring": RitualItemData(id=0xb106b, name="Unicorn Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Critical Ring": RitualItemData(id=0xb106c, name="Critical Ring", count=2, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Traverser's Ring": RitualItemData(id=0xb106d, name="Traverser's Ring", count=2, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Moon Belt": RitualItemData(id=0xb106e, name="Moon Belt", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Strider Belt": RitualItemData(id=0xb106f, name="Strider Belt", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Silver Power Ring": RitualItemData(id=0xb1070, name="Silver Power Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Rose Ring": RitualItemData(id=0xb1071, name="Rose Ring", count=2, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Skull Necklace": RitualItemData(id=0xb1072, name="Skull Necklace", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Weighted Ring": RitualItemData(id=0xb1073, name="Weighted Ring", count=2, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Cutpurse's Ring": RitualItemData(id=0xb1074, name="Cutpurse's Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Plunderer's Ring": RitualItemData(id=0xb1075, name="Plunderer's Ring", count=2, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Risk Ring": RitualItemData(id=0xb1076, name="Risk Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Adversity Ring": RitualItemData(id=0xb1077, name="Adversity Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Black Belt": RitualItemData(id=0xb1078, name="Black Belt", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Lethality Ring": RitualItemData(id=0xb1079, name="Lethality Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Gambler's Ring": RitualItemData(id=0xb107a, name="Gambler's Ring", count=1, category=RitualItemCategory.ACCESSORY1, classification=ItemClassification.useful),
    "Tunic": RitualItemData(id=0xb107b, name="Tunic", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Leather Chestguard": RitualItemData(id=0xb107c, name="Leather Chestguard", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Country Dress": RitualItemData(id=0xb107d, name="Country Dress", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Kung Fu Vest": RitualItemData(id=0xb107e, name="Kung Fu Vest", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Crusader's Armor": RitualItemData(id=0xb107f, name="Crusader's Armor", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Riding Habit": RitualItemData(id=0xb1080, name="Riding Habit", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Crystal Armor": RitualItemData(id=0xb1081, name="Crystal Armor", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Aegis Plate": RitualItemData(id=0xb1082, name="Aegis Plate", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.progression),
    "Spiked Breastplate": RitualItemData(id=0xb1083, name="Spiked Breastplate", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Valkyrie Dress": RitualItemData(id=0xb1084, name="Valkyrie Dress", count=1, category=RitualItemCategory.BODY, classification=ItemClassification.useful),
    "Sugar": RitualItemData(id=0xb1085, name="Sugar", count=4, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Soy Sauce": RitualItemData(id=0xb1086, name="Soy Sauce", count=3, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Miso": RitualItemData(id=0xb1087, name="Miso", count=3, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Black Pepper": RitualItemData(id=0xb1088, name="Black Pepper", count=2, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Ginger": RitualItemData(id=0xb1089, name="Ginger", count=4, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Garlic": RitualItemData(id=0xb108a, name="Garlic", count=4, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Rennet": RitualItemData(id=0xb108b, name="Rennet", count=5, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Curry Powder": RitualItemData(id=0xb108c, name="Curry Powder", count=8, category=RitualItemCategory.FOODSTUFF, classification=ItemClassification.filler),
    "Fried Egg": RitualItemData(id=0xb108d, name="Fried Egg", count=1, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Scrambled Eggs": RitualItemData(id=0xb108e, name="Scrambled Eggs", count=1, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Egg Soufflé": RitualItemData(id=0xb108f, name="Egg Soufflé", count=1, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Fried Fish": RitualItemData(id=0xb1090, name="Fried Fish", count=16, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Macaroni & Cheese": RitualItemData(id=0xb1091, name="Macaroni & Cheese", count=1, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Manju": RitualItemData(id=0xb1092, name="Manju", count=1, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Sponge Cake": RitualItemData(id=0xb1093, name="Sponge Cake", count=8, category=RitualItemCategory.FOOD, classification=ItemClassification.filler),
    "Galleon Map": RitualItemData(id=0xb1097, name="Galleon Map", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Silver Bromide": RitualItemData(id=0xb1098, name="Silver Bromide", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Carpenter's Key": RitualItemData(id=0xb1099, name="Carpenter's Key", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Warhorse's Key": RitualItemData(id=0xb109a, name="Warhorse's Key", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Millionaire's Key": RitualItemData(id=0xb109b, name="Millionaire's Key", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Celeste's Key": RitualItemData(id=0xb109c, name="Celeste's Key", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent I": RitualItemData(id=0xb109d, name="Hair Apparent I", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent II": RitualItemData(id=0xb109e, name="Hair Apparent II", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent VI": RitualItemData(id=0xb109f, name="Hair Apparent VI", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent VII": RitualItemData(id=0xb10a0, name="Hair Apparent VII", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent VIII": RitualItemData(id=0xb10a1, name="Hair Apparent VIII", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent X": RitualItemData(id=0xb10a2, name="Hair Apparent X", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent XI": RitualItemData(id=0xb10a3, name="Hair Apparent XI", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Hair Apparent XII": RitualItemData(id=0xb10a4, name="Hair Apparent XII", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Fine Healing Item/R": RitualItemData(id=0xb10a5, name="Fine Healing Item/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Ultimate Healing Item/R": RitualItemData(id=0xb10a6, name="Ultimate Healing Item/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Faerie Healing Item/R": RitualItemData(id=0xb10a7, name="Faerie Healing Item/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Elemental Ammunition/R": RitualItemData(id=0xb10a8, name="Elemental Ammunition/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Special Ammunition/R": RitualItemData(id=0xb10a9, name="Special Ammunition/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Potent Ammunition/R": RitualItemData(id=0xb10aa, name="Potent Ammunition/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Ultimate Ammunition/R": RitualItemData(id=0xb10ab, name="Ultimate Ammunition/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Steel Equipment/R": RitualItemData(id=0xb10ac, name="Steel Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Obsidian Equipment/R": RitualItemData(id=0xb10ad, name="Obsidian Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Damascus Equipment/R": RitualItemData(id=0xb10ae, name="Damascus Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Gold Equipment/R": RitualItemData(id=0xb10af, name="Gold Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Crimsonite Equipment/R": RitualItemData(id=0xb10b0, name="Crimsonite Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Cashmere Equipment/R": RitualItemData(id=0xb10b1, name="Cashmere Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Fine Equipment/R": RitualItemData(id=0xb10b2, name="Fine Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Very Fine Equipment/R": RitualItemData(id=0xb10b3, name="Very Fine Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Legendary Equipment/R": RitualItemData(id=0xb10b4, name="Legendary Equipment/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Ramen/R": RitualItemData(id=0xb10b5, name="Ramen/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Curry Dish/R": RitualItemData(id=0xb10b6, name="Curry Dish/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Pasta Dish/R": RitualItemData(id=0xb10b7, name="Pasta Dish/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Meat Dish/R": RitualItemData(id=0xb10b8, name="Meat Dish/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Fish Dish/R": RitualItemData(id=0xb10b9, name="Fish Dish/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Sweets/R": RitualItemData(id=0xb10ba, name="Sweets/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Cookies/R": RitualItemData(id=0xb10bb, name="Cookies/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Cake/R": RitualItemData(id=0xb10bc, name="Cake/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Drink/R": RitualItemData(id=0xb10bd, name="Drink/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Ultimate Dish/R": RitualItemData(id=0xb10be, name="Ultimate Dish/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "Supreme Dish/R": RitualItemData(id=0xb10bf, name="Supreme Dish/R", count=1, category=RitualItemCategory.KEY, classification=ItemClassification.useful),
    "SP Rounds": RitualItemData(id=0xb10c0, name="SP Rounds", count=2, category=RitualItemCategory.BULLET, classification=ItemClassification.useful),
    "HP Rounds": RitualItemData(id=0xb10c1, name="HP Rounds", count=1, category=RitualItemCategory.BULLET, classification=ItemClassification.useful),
    "Melting Bone": RitualItemData(id=0xb10c2, name="Melting Bone", count=1, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Imbrued Bone": RitualItemData(id=0xb10c3, name="Imbrued Bone", count=1, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
    "Small Webbing": RitualItemData(id=0xb10c4, name="Small Webbing", count=1, category=RitualItemCategory.INGREDIENT, classification=ItemClassification.filler),
}

SHARD_ITEMS = {
    "Double Jump": RitualItemData(id=0xb10c5, name="Double Jump", count=1, category=RitualItemCategory.SKILL, classification=ItemClassification.progression),
    "High Jump": RitualItemData(id=0xb10c6, name="High Jump", count=1, category=RitualItemCategory.SKILL, classification=ItemClassification.progression),
    "Invert": RitualItemData(id=0xb10c7, name="Invert", count=1, category=RitualItemCategory.SKILL, classification=ItemClassification.progression),
    "Deep Sinker": RitualItemData(id=0xb10c8, name="Deep Sinker", count=1, category=RitualItemCategory.SKILL, classification=ItemClassification.progression),
    "Dimension Shift": RitualItemData(id=0xb10c9, name="Dimension Shift", count=1, category=RitualItemCategory.DIRECTIONALSHARD, classification=ItemClassification.progression),
    "Reflector Ray": RitualItemData(id=0xb10ca, name="Reflector Ray", count=1, category=RitualItemCategory.DIRECTIONALSHARD, classification=ItemClassification.progression),
    "Aqua Stream": RitualItemData(id=0xb10cb, name="Aqua Stream", count=1, category=RitualItemCategory.DIRECTIONALSHARD, classification=ItemClassification.progression),
    "Craftwork": RitualItemData(id=0xb10cc, name="Craftwork", count=1, category=RitualItemCategory.EFFECTIVESHARD, classification=ItemClassification.progression),
    "Accelerator": RitualItemData(id=0xb10cd, name="Accelerator", count=1, category=RitualItemCategory.EFFECTIVESHARD, classification=ItemClassification.progression),
    "Blood Steal": RitualItemData(id=0xb10ce, name="Blood Steal", count=1, category=RitualItemCategory.TRIGGERSHARD, classification=ItemClassification.progression),
}

STAT_ITEMS = {
    "MaxHPUP": RitualItemData(id=0xb10cf, name="MaxHPUP", count=31, category=RitualItemCategory.STAT_UPGRADE, classification=ItemClassification.useful),
    "MaxMPUP": RitualItemData(id=0xb10d0, name="MaxMPUP", count=30, category=RitualItemCategory.STAT_UPGRADE, classification=ItemClassification.useful),
    "MaxBulletUP": RitualItemData(id=0xb10d1, name="MaxBulletUP", count=23, category=RitualItemCategory.STAT_UPGRADE, classification=ItemClassification.useful),
}

MONEY_ITEMS = {
    # Gold
    "500G": RitualItemData(id=0xb10d4, name="500G", count=8, category=RitualItemCategory.MONEY, classification=ItemClassification.filler),
    "1000G": RitualItemData(id=0xb10d5, name="1000G", count=4, category=RitualItemCategory.MONEY, classification=ItemClassification.filler),
    "2000G": RitualItemData(id=0xb10d6, name="2000G", count=9, category=RitualItemCategory.MONEY, classification=ItemClassification.filler),
}

ALL_RITUAL_ITEMS = CHEST_AND_WALL_ITEMS | SHARD_ITEMS | STAT_ITEMS | MONEY_ITEMS

ITEM_NAME_TO_ID = {name: data.id for name, data in ALL_RITUAL_ITEMS.items()}

FILLER_ITEMS = {name: data.id for name, data in ALL_RITUAL_ITEMS.items() if data.classification == ItemClassification.filler}


class RitualItem(Item):
    game = "Bloodstained: Ritual of the Night"

def get_random_filler_item_name(world: RitualWorld) -> str:
    random_number = world.random.randint(0, len(FILLER_ITEMS)-1)
    return list(FILLER_ITEMS)[random_number]

def get_random_starting_weapon(world: RitualWorld):
    potential_weapons = [item for item in ALL_RITUAL_ITEMS.values() if item.category == RitualItemCategory.WEAPON]
    random_number = world.random.randint(0, len(potential_weapons)-1)

    # remove weapon from dict
    return potential_weapons[random_number].name


def place_item_in_ritual_world(world: RitualWorld):
    def inner(ritual_item_name: str):
        ritual_item_data = ALL_RITUAL_ITEMS[ritual_item_name]
        ritual_item = RitualItem(name=ritual_item_data.name, classification=ritual_item_data.classification, code=ritual_item_data.id, player=world.player)
        return ritual_item
    return inner

# def apply_item_options(world: RitualWorld) -> None:
#     if world.options.vertical_progressive_movement == "progressive":
#         ALL_RITUAL_ITEMS.pop("Double Jump", None)
#         ALL_RITUAL_ITEMS.pop("High Jump", None)
#         ALL_RITUAL_ITEMS["Progressive Vertical"] = RitualItemData(id=0xb10d6, name="Progressive Vertical", count=3, category=RitualItemCategory.SKILL, classification=ItemClassification.progression)

def create_all_items(world: RitualWorld) -> None:
    itempool: list[Item] = []
    # Iterate over all items
    for key, item in ALL_RITUAL_ITEMS.items():

        # Add a number dependent on count
        for _ in range(item.count):
            itempool.append(world.create_item(key))

    # apply_item_options(world)

    world.multiworld.itempool += itempool

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool_filler = [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool_filler
