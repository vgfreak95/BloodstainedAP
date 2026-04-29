
import json
from enum import Enum
from jinja2 import Template


region_alias_lookup = {
    "SIP": "Galleon Minerva",
    "VIL": "Village",
    "ENT": "Entrance",
    "GDN": "Garden of Silence",
    "SAN": "Dian Cecht Cathedral",
    "LIB": "Livre Ex Machina",
    "TWR": "Tower of Twin Dragons",
    "TRN": "Runaway Train",
    "TAR": "Secret Sorcery Lab",
    "BIG": "Den of Behemoths",
    "JPN": "Oriental Sorcery Lab",
    "UGD": "Forbidden Underground Waterway",
    "RVA": "Inferno Cave",
    "SND": "Hidden Desert",
    "ARC": "Underground Sorcery Lab",
    "ICE": "Glacial Tomb",
    "EBT": "8 Bit Nightmare",
    "JRN": "The Tunnels",
    "LBP": "Bael Arena",
    "BKR": "Millionaires Room",
    "K2C": "Dead Lands",
    "KNG": "Hall of Termination",
}

vanilla_chests = [
    "Treasurebox_SIP000_Tutorial",
    "Treasurebox_SIP002_1",
    "Treasurebox_SIP003_1",
    "Treasurebox_SIP004_1",
    "Treasurebox_SIP005_1",
    "Treasurebox_SIP005_2",
    "Treasurebox_SIP006_1",
    "Treasurebox_SIP007_1",
    "Treasurebox_SIP007_2",
    "Treasurebox_SIP009_1",
    "Treasurebox_SIP011_1",
    "Treasurebox_SIP011_2",
    "Treasurebox_SIP011_3",
    "Treasurebox_SIP011_4",
    "Treasurebox_SIP012_1",
    "Treasurebox_SIP013_1",
    "Treasurebox_SIP014_1",
    "Treasurebox_SIP015_1",
    "Treasurebox_SIP016_1",
    "Treasurebox_SIP017_1",
    "Treasurebox_SIP018_1",
    "Treasurebox_SIP019_1",
    "Treasurebox_SIP020_1",
    "Treasurebox_SIP021_2",
    "Treasurebox_SIP024_1",
    "Treasurebox_SIP024_2",
    "Treasurebox_SIP025_1",
    "Treasurebox_SIP025_2",
    "Treasurebox_SIP026_1",
    "Treasurebox_VIL001_1",
    "Treasurebox_VIL003_1",
    "Treasurebox_VIL005_1",
    "Treasurebox_VIL006_1",
    "Treasurebox_VIL006_2",
    "Treasurebox_VIL006_3",
    "Treasurebox_VIL006_4",
    "Treasurebox_VIL007_1",
    "Treasurebox_VIL008_1",
    "Treasurebox_VIL008_2",
    "Treasurebox_VIL010_1",
    "Treasurebox_ENT002_1",
    "Treasurebox_ENT002_2",
    "Treasurebox_ENT002_3",
    "Treasurebox_ENT004_1",
    "Treasurebox_ENT005_1",
    "Treasurebox_ENT005_2",
    "Treasurebox_ENT007_1",
    "Treasurebox_ENT007_2",
    "Treasurebox_ENT007_3",
    "Treasurebox_ENT009_1",
    "Treasurebox_ENT011_1",
    "Treasurebox_ENT014_1",
    "Treasurebox_ENT014_2",
    "Treasurebox_ENT014_3",
    "Treasurebox_ENT018_1",
    "Treasurebox_ENT018_2",
    "Treasurebox_ENT020_1",
    "Treasurebox_ENT020_2",
    "Treasurebox_ENT021_1",
    "Treasurebox_ENT022_1",
    "Treasurebox_ENT024_1",
    "Treasurebox_ENT024_2",
    "Treasurebox_ENT024_3",
    "Treasurebox_GDN002_1",
    "Treasurebox_GDN004_1",
    "Treasurebox_GDN006_1",
    "Treasurebox_GDN006_2",
    "Treasurebox_GDN006_3",
    "Treasurebox_GDN006_4",
    "Treasurebox_GDN006_5",
    "Treasurebox_GDN007_1",
    "Treasurebox_GDN009_1",
    "Treasurebox_GDN009_2",
    "Treasurebox_GDN010_1",
    "Treasurebox_GDN012_1",
    "Treasurebox_GDN012_2",
    "Treasurebox_GDN013_1",
    "Treasurebox_GDN013_2",
    "Treasurebox_GDN013_3",
    "Treasurebox_GDN013_4",
    "Treasurebox_GDN014_1",
    "Treasurebox_SAN003_1",
    "Treasurebox_SAN003_2",
    "Treasurebox_SAN003_3",
    "Treasurebox_SAN003_4",
    "Treasurebox_SAN003_5",
    "Treasurebox_SAN003_6",
    "Treasurebox_SAN003_7",
    "Treasurebox_SAN003_8",
    "Treasurebox_SAN005_1",
    "Treasurebox_SAN005_2",
    "Treasurebox_SAN009_1",
    "Treasurebox_SAN009_2",
    "Treasurebox_SAN013_1",
    "Treasurebox_SAN013_2",
    "Treasurebox_SAN014_1",
    "Treasurebox_SAN015_2",
    "Treasurebox_SAN015_3",
    "Treasurebox_SAN016_1",
    "Treasurebox_SAN016_2",
    "Treasurebox_SAN016_3",
    "Treasurebox_SAN016_4",
    "Treasurebox_SAN016_5",
    "Treasurebox_SAN017_1",
    "Treasurebox_SAN019_1",
    "Treasurebox_SAN019_2",
    "Treasurebox_SAN019_3",
    "Treasurebox_SAN020_1",
    "Treasurebox_SAN021_1",
    "Treasurebox_SAN021_2",
    "Treasurebox_SAN021_3",
    "Treasurebox_SAN021_4",
    "Treasurebox_SAN021_5",
    "Treasurebox_SAN024_1",
    "Treasurebox_TWR000_1",
    "Treasurebox_TWR003_1",
    "Treasurebox_TWR004_1",
    "Treasurebox_TWR005_1",
    "Treasurebox_TWR006_1",
    "Treasurebox_TWR008_1",
    "Treasurebox_TWR009_1",
    "Treasurebox_TWR010_1",
    "Treasurebox_TWR012_1",
    "Treasurebox_TWR013_1",
    "Treasurebox_TWR016_1",
    "Treasurebox_TWR017_1",
    "Treasurebox_TWR017_2",
    "Treasurebox_TWR017_3",
    "Treasurebox_TWR017_4",
    "Treasurebox_TWR017_5",
    "Treasurebox_TWR017_6",
    "Treasurebox_TWR017_7",
    "Treasurebox_TWR018_1",
    "Treasurebox_TWR018_2",
    "Treasurebox_TWR018_3",
    "Treasurebox_TWR018_4",
    "Treasurebox_TWR018_5",
    "Treasurebox_TWR018_6",
    "Treasurebox_TWR018_7",
    "Treasurebox_TWR018_8",
    "Treasurebox_TWR019_1",
    "Treasurebox_TWR019_2",
    "Treasurebox_TWR019_4",
    "Treasurebox_LIB001_1",
    "Treasurebox_LIB002_1",
    "Treasurebox_LIB007_1",
    "Treasurebox_LIB009_1",
    "Treasurebox_LIB009_2",
    "Treasurebox_LIB011_1",
    "Treasurebox_LIB012_1",
    "Treasurebox_LIB017_1",
    "Treasurebox_LIB019_1",
    "Treasurebox_LIB022_1",
    "Treasurebox_LIB030_1",
    "Treasurebox_LIB032_1",
    "Treasurebox_LIB033_1",
    "Treasurebox_LIB040_1",
    "Treasurebox_LIB043_1",
    "Treasurebox_TRN002_1",
    "Treasurebox_TRN002_2",
    "Treasurebox_TRN002_3",
    "Treasurebox_TRN002_4",
    "Treasurebox_TRN002_5",
    "Treasurebox_KNG002_1",
    "Treasurebox_KNG002_2",
    "Treasurebox_KNG003_1",
    "Treasurebox_KNG006_1",
    "Treasurebox_KNG010_1",
    "Treasurebox_KNG011_1",
    "Treasurebox_KNG012_1",
    "Treasurebox_KNG012_2",
    "Treasurebox_KNG016_1",
    "Treasurebox_KNG017_1",
    "Treasurebox_KNG017_2",
    "Treasurebox_KNG017_3",
    "Treasurebox_KNG017_4",
    "Treasurebox_KNG017_5",
    "Treasurebox_KNG018_2",
    "Treasurebox_KNG018_3",
    "Treasurebox_KNG018_4",
    "Treasurebox_KNG021_1",
    "Treasurebox_KNG022_1",
    "Treasurebox_UGD001_1",
    "Treasurebox_UGD003_1",
    "Treasurebox_UGD003_2",
    "Treasurebox_UGD003_3",
    "Treasurebox_UGD003_4",
    "Treasurebox_UGD005_1",
    "Treasurebox_UGD005_2",
    "Treasurebox_UGD007_1",
    "Treasurebox_UGD009_1",
    "Treasurebox_UGD009_2",
    "Treasurebox_UGD009_3",
    "Treasurebox_UGD009_4",
    "Treasurebox_UGD010_1",
    "Treasurebox_UGD011_1",
    "Treasurebox_UGD021_1",
    "Treasurebox_UGD024_1",
    "Treasurebox_UGD024_2",
    "Treasurebox_UGD024_3",
    "Treasurebox_UGD025_1",
    "Treasurebox_UGD025_2",
    "Treasurebox_UGD025_3",
    "Treasurebox_UGD027_1",
    "Treasurebox_UGD030_1",
    "Treasurebox_UGD031_1",
    "Treasurebox_UGD031_2",
    "Treasurebox_UGD036_1",
    "Treasurebox_UGD036_2",
    "Treasurebox_UGD038_1",
    "Treasurebox_UGD040_1",
    "Treasurebox_UGD041_1",
    "Treasurebox_UGD042_1",
    "Treasurebox_UGD044_1",
    "Treasurebox_UGD044_2",
    "Treasurebox_UGD046_1",
    "Treasurebox_UGD046_2",
    "Treasurebox_UGD047_2",
    "Treasurebox_UGD048_1",
    "Treasurebox_UGD050_1",
    "Treasurebox_UGD051_1",
    "Treasurebox_UGD052_1",
    "Treasurebox_UGD052_2",
    "Treasurebox_UGD053_1",
    "Treasurebox_UGD054_1",
    "Treasurebox_UGD056_1",
    "Treasurebox_SND002_1",
    "Treasurebox_SND003_1",
    "Treasurebox_SND004_1",
    "Treasurebox_SND006_1",
    "Treasurebox_SND008_1",
    "Treasurebox_SND008_2",
    "Treasurebox_SND009_1",
    "Treasurebox_SND010_1",
    "Treasurebox_SND010_2",
    "Treasurebox_SND013_1",
    "Treasurebox_SND015_1",
    "Treasurebox_SND016_1",
    "Treasurebox_SND017_1",
    "Treasurebox_SND018_1",
    "Treasurebox_SND019_1",
    "Treasurebox_SND020_1",
    "Treasurebox_SND024_1",
    "Treasurebox_SND025_1",
    "Treasurebox_ARC000_1",
    "Treasurebox_ARC002_1",
    "Treasurebox_ARC003_1",
    "Treasurebox_ARC004_1",
    "Treasurebox_ARC006_1",
    "Treasurebox_ARC006_2",
    "Treasurebox_ARC007_1",
    "Treasurebox_ARC007_2",
    "Treasurebox_TAR001_1",
    "Treasurebox_TAR002_1",
    "Treasurebox_TAR006_1",
    "Treasurebox_TAR007_1",
    "Treasurebox_TAR010_1",
    "Treasurebox_JPN002_1",
    "Treasurebox_JPN002_2",
    "Treasurebox_JPN004_1",
    "Treasurebox_JPN005_1",
    "Treasurebox_JPN009_1",
    "Treasurebox_JPN010_1",
    "Treasurebox_JPN010_2",
    "Treasurebox_JPN013_1",
    "Treasurebox_JPN015_1",
    "Treasurebox_JPN017_1",
    "Treasurebox_JPN018_1",
    "Treasurebox_RVA001_1",
    "Treasurebox_RVA001_2",
    "Treasurebox_RVA002_1",
    "Treasurebox_RVA004_1",
    "Treasurebox_RVA006_1",
    "Treasurebox_RVA010_1",
    "Treasurebox_RVA011_1",
    "Treasurebox_RVA011_2",
    "Treasurebox_RVA012_1",
    "Treasurebox_RVA015_1",
    "Treasurebox_BIG002_1",
    "Treasurebox_BIG005_1",
    "Treasurebox_BIG006_1",
    "Treasurebox_BIG006_2",
    "Treasurebox_BIG006_3",
    "Treasurebox_BIG006_4",
    "Treasurebox_BIG006_5",
    "Treasurebox_BIG006_6",
    "Treasurebox_BIG007_1",
    "Treasurebox_BIG008_1",
    "Treasurebox_BIG010_1",
    "Treasurebox_BIG011_1",
    "Treasurebox_BIG012_1",
    "Treasurebox_BIG012_2",
    "Treasurebox_BIG012_3",
    "Treasurebox_BIG013_1",
    "Treasurebox_BIG014_1",
    "Treasurebox_BIG016_1",
    "Treasurebox_BIG016_2",
    "Treasurebox_BIG016_3",
    "Treasurebox_ICE001_1",
    "Treasurebox_ICE001_2",
    "Treasurebox_ICE002_1",
    "Treasurebox_ICE003_1",
    "Treasurebox_ICE003_2",
    "Treasurebox_ICE006_1",
    "Treasurebox_ICE008_1",
    "Treasurebox_ICE008_2",
    "Treasurebox_ICE010_1",
    "Treasurebox_ICE011_1",
    "Treasurebox_ICE013_1",
    "Treasurebox_ICE014_1",
    "Treasurebox_PureMiriam_Hair",
    "Treasurebox_PureMiriam_Tiare",
    "Treasurebox_PureMiriam_Dress",
    "Treasurebox_PureMiriam_Sword",
    "Wall_SIP004_1",
    "Wall_SIP009_1",
    "Wall_SIP014_1",
    "Wall_SIP016_1",
    "Wall_ENT002_1",
    "Wall_ENT012_1",
    "Wall_GDN006_1",
    "Wall_SAN000_1",
    "Wall_SAN005_1",
    "Wall_SAN019_1",
    "Wall_KNG000_1",
    "Wall_KNG007_1",
    "Wall_LIB004_1",
    "Wall_LIB019_1",
    "Wall_LIB025_1",
    "Wall_TWR006_1",
    "Wall_TWR013_1",
    "Wall_TWR016_1",
    "Wall_TRN005_1",
    "Wall_UGD000_1",
    "Wall_UGD003_1",
    "Wall_UGD006_1",
    "Wall_UGD012_1",
    "Wall_UGD020_1",
    "Wall_UGD031_1",
    "Wall_UGD037_1",
    "Wall_UGD046_1",
    "Wall_UGD056_1",
    "Wall_SND001_1",
    "Wall_SND019_1",
    "Wall_TAR007_1",
    "Wall_JPN011_1",
    "Wall_JPN013_1",
    "Wall_RVA011_1",
    "Wall_BIG002_1",
    "Wall_BIG012_1",
    "Wall_BIG016_1",
    "Wall_ICE003_1",
    "Wall_ICE010_1",
    "Wall_ICE017_1",
    "N3106_1ST_Treasure",
    "N3106_2ND_Treasure",
    "Treasurebox_JRN001_1",
    "Treasurebox_JRN001_2",
    "Treasurebox_JRN001_3",
    "Treasurebox_JRN002_1",
    "Treasurebox_JRN004_1"
]

entrances = [

]

enemy_alias_lookup = None
with open("data/translation/Enemy.json", "r") as enemy_file:
    enemy_alias_lookup = json.load(enemy_file)

class Direction(Enum):
    START        = "Start"
    EXIT         = "Exit"
    LEFT         = "Left"
    BOTTOM       = "Bottom"
    RIGHT        = "Right"
    TOP          = "Top"
    LEFT_BOTTOM  = "Left Bottom"
    RIGHT_BOTTOM = "Right Bottom"
    LEFT_TOP     = "Left Top"
    RIGHT_TOP    = "Right Top"
    TOP_LEFT     = "Top Left"
    TOP_RIGHT    = "Top Right"
    BOTTOM_RIGHT = "Bottom Right"
    BOTTOM_LEFT  = "Bottom Left"

def full_region_alias(region="SIP_001"):
    region_code, room_id =region.split("_")
    aliased_region = region_alias_lookup[region_code]
    return f"{aliased_region} {room_id}"

def entrance_alias(entrance: str) -> str:

    parts = entrance.split("_")
    
    direction_found = False
    final_direction = ""
    # Try two-word direction first (e.g. LEFT_BOTTOM), greedy match
    if len(parts) >= 2:
        two_word_key = parts[-2] + "_" + parts[-1]
        try:
            final_direction = Direction[two_word_key].value
            direction_found = True
        except KeyError:
            pass
    
    # Fall back to single-word direction (e.g. LEFT)
    if not direction_found:
        try:
            final_direction = Direction[parts[-1]].value
        except KeyError:
            raise ValueError(f"No valid direction found in entrance: '{entrance}'")
        
    region_code = parts[0]
    room        = parts[1]
    region_name = region_alias_lookup.get(region_code, region_code)
        
    return f"{region_name} {room} - Entrance {final_direction}"



def enemy_alias(enemy_room_and_id: str) -> str:

    region_code_and_room_id, enemy_id = enemy_room_and_id.split(".")
    region_code, room_id = region_code_and_room_id.split("_")
    region_name = region_alias_lookup.get(region_code)
    if isinstance(enemy_alias_lookup, dict):
        alias = enemy_alias_lookup[enemy_id]

    return f"{region_name} {room_id} - Enemy {alias}"

def get_all_chests_for_region(region):
    global vanilla_chests

    chests_in_region = []
    for chest in vanilla_chests:
        region_for_chest = chest.split("_")[1][:3]
        print(region_for_chest)
        if region_for_chest == region:
            chests_in_region.append(chest)

    return chests_in_region

def get_all_entrances_for_region(region):
    room_requirements = None
    with open("data/RoomRequirement.json") as file:
        room_requirements = json.load(file)

    regions = set()
    region_dot_entrances = set()

    # generate region and unique entrances
    for room in room_requirements:
        region_name, _ = room.split("_")

        entrance_locations = room_requirements[room]
        for entrance in entrance_locations:
            if entrance[:3] == region:
                entrance_name = f"{entrance}"
                region_dot_entrances.add(entrance_name)
        
        regions.add(region_name)

    return region_dot_entrances



def generate_locations_file():
    locations_template = Template("""\
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import RitualWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.

LOCATION_ENEMY_TO_ID = {
{%- for location in enemy_locations %}
    "{{ location.name }}": {{ location.id }},
{%- endfor %}
}

LOCATION_CHEST_TO_ID = {
{%- for location in chest_locations %}
    "{{ location.name }}": {{ location.id }},
{%- endfor %}
}

LOCATION_NAME_TO_ID = LOCATION_ENEMY_TO_ID | LOCATION_CHEST_TO_ID



# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class RitualLocation(Location):
    game = "Bloodstained"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: RitualWorld) -> None:
    create_regular_locations(world)
    # create_events(world)


def create_regular_locations(world: RitualWorld) -> None:
{%- for region in regions %}
    {{ region.name }} = world.get_region("{{ region.full_name }}")
    {{ region.name }}_locations = get_location_names_with_ids([
{%- for location in region.locations %}
        "{{ location }}",
{%- endfor %}
    ])
    {{ region.name }}.add_locations({{ region.name }}_locations)

{%- endfor %}


def create_events(world: RitualWorld) -> None:
    pass
""")

    enemy_locations = [
        {"name": "Tutorial Enemy", "id": 1}
    ]

    chest_locations = [
        {"name": chest_name, "id": i}
    for i, chest_name in enumerate(get_all_chests_for_region("SIP"), start=1000)]

    print(chest_locations)
            
    # chest_locations = [
    #     {"name": "Tutorial Chest Pickup 1", "id": 1000},
    #     {"name": "Tutorial Chest Pickup 2", "id": 1001},
    # ]
    #
    regions = [
        {
            "name": "tutorial_room",
            "full_name": "Galleon Minerva",
            "locations": ["Tutorial Enemy", "Tutorial Chest Pickup 1", "Tutorial Chest Pickup 2"]
        }
    ]

    output = locations_template.render(
        enemy_locations=enemy_locations,
        chest_locations=chest_locations,
        regions=regions
    )

    with open("generated_locations.py", "w") as f:
        f.write(output)

    print("Generated generated_locations.py")


def generate_locations_file(region: str = None, include_enemies: bool = True):
    locations_template = Template("""\
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import RitualWorld

LOCATION_ENEMY_TO_ID = {
{%- for loc in enemy_locations %}
    "{{ loc.name }}": {{ loc.id }},
{%- endfor %}
}

LOCATION_CHEST_TO_ID = {
{%- for loc in chest_locations %}
    "{{ loc.name }}": {{ loc.id }},
{%- endfor %}
}

LOCATION_NAME_TO_ID = LOCATION_ENEMY_TO_ID | LOCATION_CHEST_TO_ID



class RitualLocation(Location):
    game = "Bloodstained"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: RitualWorld) -> None:
    create_regular_locations(world)


def create_regular_locations(world: RitualWorld) -> None:
{%- for region_data in region_locations %}
    {{ region_data.name }} = world.get_region("{{ region_data.entrance }}")
    {{ region_data.name }}_locations = get_location_names_with_ids([
{%- for loc in region_data.locations %}
        "{{ loc }}",
{%- endfor %}
    ])
    {{ region_data.name }}.add_locations({{ region_data.name }}_locations)

{%- endfor %}
""")

    with open("data/RoomRequirement.json", "r") as f:
        room_requirements = json.load(f)

    region_prefix = region.upper() if region else None
    region_keys = [k for k in room_requirements.keys() if region_prefix is None or region_prefix in k]

    all_locations = set()
    locations_by_entrance = {}
    location_to_first_entrance = {}
    
    for region_key in region_keys:
        entrances = room_requirements[region_key]
        for entrance, connections in entrances.items():
            for location_name, requirements in connections.items():
                is_chest = location_name.startswith("Treasurebox_")
                is_wall = location_name.startswith("Wall_")
                is_enemy = location_name.startswith("N")
                
                if is_chest or is_wall or (is_enemy and include_enemies):
                    if location_name not in location_to_first_entrance:
                        location_to_first_entrance[location_name] = entrance
                    if entrance not in locations_by_entrance:
                        locations_by_entrance[entrance] = []
                    if location_name not in locations_by_entrance[entrance]:
                        locations_by_entrance[entrance].append(location_name)
                    all_locations.add(location_name)

    sorted_locations = sorted(all_locations)
    chest_locations = [{"name": loc, "id": 1000 + i} for i, loc in enumerate(sorted_locations)]
    enemy_locations = []
    
    region_locations = []
    for entrance, locs in locations_by_entrance.items():
        filtered_locs = [loc for loc in locs if location_to_first_entrance.get(loc) == entrance]
        if filtered_locs:
            region_name = entrance.lower().replace("-", "_").replace(" ", "_")
            region_locations.append({
                "name": region_name,
                "entrance": entrance,
                "locations": filtered_locs
            })
    
    output = locations_template.render(
        enemy_locations=enemy_locations,
        chest_locations=chest_locations,
        region_locations=region_locations
    )

    with open("generated_locations.py", "w") as f:
        f.write(output)

    print(f"Generated generated_locations.py with {len(sorted_locations)} locations")


def generate_rules_file(region: str = None, include_enemies: bool = True):
    rules_template = Template("""\
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import RitualWorld


def set_all_rules(world: RitualWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: RitualWorld) -> None:
    pass



def set_all_location_rules(world: RitualWorld) -> None:
{%- for rule in rules %}
    {{ rule.location }} = world.get_location("{{ rule.location_name }}")
    set_rule({{ rule.location }}, lambda state: {{ rule.condition }})

{%- endfor %}

def set_completion_condition(world: RitualWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(("Knife", "Boots", "Shard"), world.player)
""")

    with open("data/RoomRequirement.json", "r") as f:
        room_requirements = json.load(f)

    region_prefix = region.upper() if region else None
    region_keys = [k for k in room_requirements.keys() if region_prefix is None or region_prefix in k]

    location_requirements = {}
    for region_key in region_keys:
        entrances = room_requirements[region_key]
        for entrance, connections in entrances.items():
            for location_name, requirements in connections.items():
                is_chest = location_name.startswith("Treasurebox_")
                is_wall = location_name.startswith("Wall_")
                is_enemy = location_name.startswith("N")
                
                if is_chest or is_wall or (is_enemy and include_enemies):
                    if location_name not in location_requirements:
                        location_requirements[location_name] = requirements
                    elif not location_requirements[location_name] and requirements:
                        location_requirements[location_name] = requirements

    print(f"Unique locations found: {len(location_requirements)}")

    rules = []
    seen_names = {}
    for location, requirements in location_requirements.items():
        if not requirements:
            continue
        condition = parse_requirements(requirements)
        
        base_name = location.lower().replace("treasurebox_", "").replace("wall_", "").replace("-", "_").replace(" ", "_")
        if base_name in seen_names:
            seen_names[base_name] += 1
            var_name = f"{base_name}_{seen_names[base_name]}"
        else:
            seen_names[base_name] = 0
            var_name = base_name
            
        rules.append({
            "location": var_name,
            "location_name": location,
            "condition": condition
        })

    output = rules_template.render(rules=rules)

    with open("generated_rules.py", "w") as f:
        f.write(output)

    print(f"Generated generated_rules.py with {len(rules)} rules")


def parse_requirements(requirements):
    if not requirements:
        return "True"

    if isinstance(requirements, list):
        parts = []
        for req in requirements:
            if isinstance(req, list):
                and_parts = " and ".join(f'state.has("{item}", world.player)' for item in req)
                parts.append(f"({and_parts})")
            else:
                parts.append(f'state.has("{req}", world.player)')
        return " or ".join(parts)
    else:
        return f'state.has("{requirements}", world.player)'


if __name__ == "__main__":
    import sys
    region = None
    include_enemies = True
    
    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            if arg == "--no-enemies":
                include_enemies = False
            elif arg == "--include-enemies":
                include_enemies = True
        else:
            region = arg
    
    generate_rules_file(region, include_enemies)


def generate_regions_file(region: str = None):
    regions_template = Template("""\
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region, Entrance

if TYPE_CHECKING:
    from .world import RitualWorld


REGIONS = [
{%- for region in regions %}
    "{{ region }}",
{%- endfor %}
]

def create_and_connect_regions(world: RitualWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_region_helper(world: RitualWorld):
    def inner(region_name):
        return Region(region_name, world.player, world.multiworld)
    return inner


def create_all_regions(world: RitualWorld) -> None:
    create_ritual_region = create_region_helper(world)
    world.multiworld.regions += [create_ritual_region(region) for region in REGIONS]


def connect_regions(world: RitualWorld) -> None:
{%- for connection in connections %}
    {{ connection.from_region }} = world.get_region("{{ connection.from_region }}")
    {{ connection.to_region }} = world.get_region("{{ connection.to_region }}")
    {{ connection.from_region }}.connect({{ connection.to_region }}, "{{ connection.entrance_name }}")

{%- endfor %}
""")

    with open("data/RoomRequirement.json", "r") as f:
        room_requirements = json.load(f)

    region_prefix = region.upper() if region else None
    region_keys = [k for k in room_requirements.keys() if region_prefix is None or region_prefix in k]

    unique_regions = set()
    connections = []
    
    for region_key in region_keys:
        entrances = room_requirements[region_key]
        for entrance, connections_dict in entrances.items():
            unique_regions.add(entrance)
            
            for target, requirements in connections_dict.items():
                if not target.startswith("Treasurebox_") and not target.startswith("Wall_") and not target.startswith("N"):
                    entrance_name = f"{entrance} to {target}"
                    connections.append({
                        "from_region": entrance,
                        "to_region": target,
                        "entrance_name": entrance_name
                    })
                    unique_regions.add(target)

    regions_list = sorted(unique_regions)
    
    output = regions_template.render(
        regions=regions_list,
        connections=connections
    )

    with open("generated_regions.py", "w") as f:
        f.write(output)

    print(f"Generated generated_regions.py with {len(regions_list)} regions and {len(connections)} connections")


if __name__ == "__main__":
    import sys
    region = None
    include_enemies = True
    generate_regions = False
    generate_locations = False
    
    for arg in sys.argv[1:]:
        if arg == "--regions":
            generate_regions = True
        elif arg == "--locations":
            generate_locations = True
        elif arg == "--no-enemies":
            include_enemies = False
        elif arg == "--include-enemies":
            include_enemies = True
        else:
            region = arg
    
    if generate_locations:
        print("Generating locations...")
        generate_locations_file(region, include_enemies)
        sys.exit(0)
    
    if generate_regions:
        print("Generating regions...")
        generate_regions_file(region)
        sys.exit(0)
    
    print("Generating rules...")
    generate_rules_file(region, include_enemies)
