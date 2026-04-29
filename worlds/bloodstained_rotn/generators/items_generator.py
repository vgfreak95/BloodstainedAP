import json
from collections import Counter
from dataclasses import dataclass
from enum import Enum
import jinja2

# from BaseClasses import ItemClassification

class RitualItemCategory(Enum):
    POTION = "Potion",
    INGREDIENT = "Ingredient",
    WEAPON = "Weapon",
    HEAD = "Head",
    BODY = "Body",
    ACCESSORY = "Accessory1",
    MUFFLER = "Muffler"

@dataclass
class RitualItemData:
    id: int
    name: str
    category: RitualItemCategory
    count: int
    # classification: ItemClassification

class ItemClassification(Enum):
    filler = 0,
    progression = 1,
    useful = 2


with open("../data/Archipelago.json") as file:
    ap = json.load(file)

with open("../data/PB_DT_ItemMaster.json") as file:
    dt_item = json.load(file)

with open("../data/translation/Item.json") as file:
    item_translation_table = json.load(file)

with open("../data/translation/Shard.json") as file:
    shard_translation_table = json.load(file)


template = jinja2.Template("""# Auto-generated file

from dataclasses import dataclass
from enum import Enum

class ItemClassification(Enum):
    filler = 0,
    progression = 1,
    useful = 2


class RitualItemCategory(Enum):
    # Items
    POTION = "Potion",
    INGREDIENT = "Ingredient",
    FOOD = "Food",
    FOODSTUFF = "FoodStuff",
    KEY = "Key"

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

@dataclass
class RitualItemData:
    id: int
    name: str
    count: int
    category: RitualItemCategory
    classification: ItemClassification


ITEMS_DATA = {
{%- for item in items %}
    "{{ item['name'] }}": RitualItemData(id={{ item['id'] }}, name="{{ item['name'] }}", count={{ item['amount'] }}, category=RitualItemCategory.{{ item['category'] }}, classification={{ item['classification'] }}),
{%- endfor %}
}
""")


def get_items_count() -> dict[str, int]:
    items_to_count = []
    for ap_item in ap["Items"]:
        items_to_count.extend(ap["Items"][ap_item])
    item_counter = Counter(items_to_count)
    return item_counter

def get_items_category() -> dict[str, str]:
    items_to_category = {}
    for row in dt_item[0]["Rows"]:
        dt_row = dt_item[0]["Rows"][row]
        _, item_type = dt_row["ItemType"].split("::")
        is_dlc = dt_row["IsDLC"]
        if not is_dlc:
            items_to_category.update({row: item_type})
    return items_to_category


def get_shards_to_category() -> dict[str, str]:
    shard_to_category = {}

    key_shards = [
        "Doublejump",
        "HighJump",
        "Invert",
        "Deepsinker",
        "Dimensionshift",
        "Reflectionray",
        "Aquastream",
        "Demoniccapture",
        "Accelerator",
        "Bloodsteel",
    ]

    for shard in key_shards:
        for row in dt_item[0]["Rows"]:
            if row == shard:
                dt_row = dt_item[0]["Rows"][row]
                _, item_type = dt_row["ItemType"].split("::")
                shard_to_category.update({shard: item_type})
    return shard_to_category


if __name__ == "__main__":
    # output = template.render(items=item_counter)
    items_count = get_items_count()
    items_category = get_items_category()
    shards_category = get_shards_to_category()
    all_items = items_category.keys()
    all_shards = shards_category.keys()
    item_id = 0xb100d
    items_data = []


    for item in all_items:
        if items_count[item] == 0:
            continue
        item_category: str = items_category[item]
        if item_category == "FoodStuff" or item_category == "Ingredient" or item_category == "Food":
            items_data.append({"id": hex(item_id), "name": item_translation_table[item], "amount": items_count[item], "category": item_category.upper(), "classification": ItemClassification.filler})
        elif item_category == "Potion" or item_category == "Weapon" or item_category == "Head" or item_category == "Muffler" or item_category == "Accessory1" or item_category == "Body" or item_category == "Bullet" or item_category == "Key":
            items_data.append({"id": hex(item_id), "name": item_translation_table[item], "amount": items_count[item], "category": item_category.upper(), "classification": ItemClassification.useful})
        item_id += 1
    for shard in all_shards:
        items_data.append({"id": hex(item_id), "name": shard_translation_table[shard], "amount": 1, "category": shards_category[shard].upper(), "classification": ItemClassification.progression})
        item_id += 1


    items_data_output = template.render(items=items_data)

    with open("../generated/items.py", "w") as generated_items:
        generated_items.write(items_data_output)






