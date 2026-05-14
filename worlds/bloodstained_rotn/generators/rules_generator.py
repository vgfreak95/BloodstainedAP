import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from enum import Enum
import jinja2

from regions_here import ALL_REGIONS_DATA



with open("../data/Archipelago.json") as ap_file:
    ap = json.load(ap_file)

with open("../data/RoomRequirement.json") as room_req_file:
    room_requirements = json.load(room_req_file)

with open("../data/EnemyInfo.json") as enemy_file:
    enemy_info = json.load(enemy_file)

# Set of enemies that drop shards
ENEMIES_WITH_SHARDS = {
    enemy_id.replace("_Hard", "").replace("_Normal", "")
    for enemy_id, info in enemy_info.items()
    if info.get("HasShard", False) and enemy_id.startswith("N")
}

def build_entrance_exit_map() -> dict[str, list[tuple[str, str]]]:
    entrance_to_targets = {}
    
    for region_key, region_data in ALL_REGIONS_DATA.items():
        for entrance, exits in region_data.entrance.items():
            for exit_entrance in exits:
                target_room = None
                for r_key, r_data in ALL_REGIONS_DATA.items():
                    for room in r_data.entrance:
                        if room == exit_entrance:
                            target_room = [r for r in r_data.connections if r.split("_")[1] == exit_entrance.split("_")[1]][0]
                            break
                    if target_room:
                        break
                if target_room:
                    if entrance not in entrance_to_targets:
                        entrance_to_targets[entrance] = []
                    entrance_to_targets[entrance].append((exit_entrance, target_room))
    
    return entrance_to_targets

def find_room_for_entrance(target_entrance: str) -> str:
    target_num = target_entrance.split("_")[1]
    
    for region_key, region_data in ALL_REGIONS_DATA.items():
        for room in region_data.connections:
            room_num = room.split("_")[1]
            if room_num == target_num:
                return room
    
    return None

ENTRANCE_EXIT_MAP = build_entrance_exit_map()

def build_exit_to_target_map() -> dict[tuple[str, str], str]:
    exit_to_target = {}
    
    entrance_to_room = {}
    for region_key, region_data in ALL_REGIONS_DATA.items():
        for room in region_data.connections:
            for entrance in region_data.entrance:
                entrance_to_room[entrance] = room
    
    for region_key, region_data in ALL_REGIONS_DATA.items():
        for entrance, exits in region_data.entrance.items():
            for exit_entrance in exits:
                if exit_entrance in entrance_to_room:
                    exit_to_target[(entrance_to_room[entrance], exit_entrance)] = entrance_to_room[exit_entrance]
    
    return exit_to_target

EXIT_TO_TARGET = build_exit_to_target_map()

def find_target_rooms(entrance_name: str) -> list[tuple[str, str]]:
    if entrance_name not in ENTRANCE_EXIT_MAP:
        return []
    return ENTRANCE_EXIT_MAP[entrance_name]

def get_exit_num(exit_name: str) -> str:
    if "_" not in exit_name:
        return None
    return exit_name.split("_")[1]

def find_target_by_exit(exit_entrance: str) -> str:
    if exit_entrance not in ENTRANCE_EXIT_MAP:
        return None
    
    targets = ENTRANCE_EXIT_MAP[exit_entrance]
    if targets:
        return targets[0][1]
    return None

def build_entrance_rules():
    all_rules = {}
    
    for room_id, room_data in room_requirements.items():
        for entrance_name, exit_data in room_data.items():
            for exit_name, requirements in exit_data.items():
                if not requirements:
                    continue
                
                if exit_name.startswith("Treasurebox_") or exit_name.startswith("N") or exit_name.startswith("Wall_") or exit_name.startswith("Fam"):
                    continue
                
                to_room = find_target_by_exit(exit_name)
                
                if not to_room or to_room == room_id:
                    continue
                
                key = (room_id, to_room)
                if key not in all_rules:
                    all_rules[key] = requirements
    
    return all_rules


def build_location_rules():
    all_rules = {}
    
    for room_id, room_data in room_requirements.items():
        for entrance_name, exit_data in room_data.items():
            for exit_name, requirements in exit_data.items():
                location_type = ""
                if not requirements:
                    continue
                
                if exit_name.startswith("Treasurebox_"):
                    pass
                elif exit_name.startswith("Wall_"):
                    pass
                elif exit_name.startswith("N"):
                    pass
                elif exit_name.startswith("Fam"):
                    pass
                else:
                    continue
                
                key = (room_id, exit_name + location_type)
                if key not in all_rules:
                    # print(key)
                    all_rules[key] = requirements
    
    return all_rules

def convert_strings_to_lists(requirements):
    converted = []
    for req in requirements:
        if isinstance(req, str) and req.startswith("["):
            converted.append(eval(req))
        else:
            converted.append(req)
    return converted


def flatten_single_nested_list(requirements):
    if not isinstance(requirements, list):
        return requirements
    list_elements = [x for x in requirements if isinstance(x, list)]
    if len(list_elements) == 1:
        result = []
        for req in requirements:
            if isinstance(req, list):
                result.extend(req)
            else:
                result.append(req)
        return result
    return requirements


def flatten_requirements(rules):
    flattened = {}
    for (from_room, to_room), requirements in rules.items():
        converted = convert_strings_to_lists(requirements)
        flattened_list = flatten_single_nested_list(converted)
        flattened[(from_room, to_room)] = flattened_list
    return flattened

ALL_ENTRANCE_RULES = build_entrance_rules()

MACRO_MAP = {
    "Doublejump": "HAS_DOUBLE_JUMP",
    "HighJump": "HAS_HIGH_JUMP",
    "Invert": "HAS_INVERT",
    "Dimensionshift": "HAS_DIMENSION_SHIFT",
    "Reflectionray": "HAS_REFLECTION_RAY",
    "Aquastream": "HAS_AQUASTREAM",
    "Accelerator": "HAS_ACCELERATOR",
    "BreastplateofAguilar": "HAS_AEGIS_PLATE",
    "Demoniccapture": "HAS_CRAFTWORK",
    "Bloodsteal": "HAS_BLOODSTEAL",
    "Deepsinker": "HAS_DEEPSINKER",
    "Bloodsteel": "HAS_BLOODSTEAL",
    "Height": "HAS_HEIGHT",
    "Flight": "HAS_FLIGHT",
    "WaterM": "HAS_WATER_MOVEMENT",
}


def format_rule(requirements):
    if not requirements:
        return "True"

    def parse_req(req):
        if isinstance(req, list):
            if not req:
                return "True"
            if len(req) == 1:
                return parse_req(req[0])
            parts = [parse_req(r) for r in req]
            return "(" + " & ".join(parts) + ")"
        else:
            macro = MACRO_MAP.get(req)
            if macro:
                return macro
            return f'Has("{req}")'

    if isinstance(requirements, list):
        if len(requirements) == 1:
            return parse_req(requirements[0])
        parts = [parse_req(r) for r in requirements]
        return "(" + " | ".join(parts) + ")"
    return parse_req(requirements)

def get_difficulty_key(enemy_region: str) -> tuple[str, str]:
    """Returns (dict_key, clean_region_name) after stripping _Hard/_Normal suffixes."""
    clean = enemy_region.replace("_Shard", "").replace("_Region", "")
    
    if "_Hard" in clean:
        return ("Hard_Enemies", clean.replace("_Hard", "") + "_Region")
    elif "_Normal" in clean:
        return ("Normal_Enemies", clean.replace("_Normal", "") + "_Region")
    return ("Enemies", clean + "_Region")

def build_enemy_regions_split(location_rules):
    """Build three separate enemy region dicts by difficulty, only including shard-dropping enemies."""
    enemies_base = {}      # base regions (no suffix)
    enemies_normal = {}    # _Normal_Region variants
    enemies_hard = {}     # _Hard_Region variants
    
    for (from_room, to_room), requirements in location_rules.items():
        if not to_room.startswith("N"):
            continue
        
        key, clean_region = get_difficulty_key(to_room)
        
        # Extract base enemy ID (e.g., "N3029" from "N3029_Region" or "N3029_Hard_Region")
        base_id = clean_region.replace("_Region", "").split("_")[0]
        
        # Only include enemies that drop shards
        if base_id not in ENEMIES_WITH_SHARDS:
            continue
        
        target_dict = {
            "Enemies": enemies_base,
            "Normal_Enemies": enemies_normal,
            "Hard_Enemies": enemies_hard,
        }[key]
        
        if from_room not in target_dict:
            target_dict[from_room] = []
        
        if clean_region not in target_dict[from_room]:
            target_dict[from_room].append(clean_region)
    
    # Deduplicate destinations per room
    for d in [enemies_base, enemies_normal, enemies_hard]:
        for room in d:
            d[room] = list(set(d[room]))
    
    return {
        "Enemies": enemies_base,
        "Normal_Enemies": enemies_normal,
        "Hard_Enemies": enemies_hard,
    }

# enemy_regions_by_difficulty = build_enemy_regions_split()


enemy_dict_template = jinja2.Template("""# Auto-generated enemy regions dict
ENEMY_REGIONS = {
{%- for key, regions in enemy_regions.items() %}
    "{{ key }}": RitualRegion(alias="Enemy Regions", connections={
{%- for room, destinations in regions.items() | sort %}
        "{{ room }}": {{ destinations | tojson }},
{%- endfor %}
    }, entrance={}),
{%- endfor %}
}

# Flattened list for location generation (deduplicated)
ENEMY_FLATTENED_REGIONS = [
{%- for region in enemy_flattened %}
    "{{ region }}",
{%- endfor %}
]
""")






entrance_rule_template = jinja2.Template("""{%- for (from_room, to_room), requirements in entrance_rules.items() %}
{# {{ from_room }} to {{ to_room }} requires {{ requirements }} #}
tmp_entrance = world.get_entrance("{{ from_room }} to {{ to_room }}")
tmp_rule = {{ format_rule(requirements) }}
world.set_rule(tmp_entrance, tmp_rule)
{%- endfor %}
""")

entrance_dict_template = jinja2.Template("""# Auto-generated entrance rules dict
ENTRANCE_RULES = {
{%- for (from_room, to_room), requirements in entrance_rules.items() %}
    "{{ from_room }} to {{ to_room }}": {{ format_rule(requirements) }},
{%- endfor %}
}
""")

location_dict_template = jinja2.Template("""# Auto-generated location rules dict
LOCATION_RULES = {
{%- for (from_room, location), requirements in location_rules.items() %}
    "{{ location }}": {{ format_rule(requirements) }},
{%- endfor %}
}
""")

def build_location_with_or_without_rules():
    all_rules = {}
    
    for room_id, room_data in room_requirements.items():
        for entrance_name, exit_data in room_data.items():
            for exit_name, requirements in exit_data.items():
                location_type = ""
                
                if exit_name.startswith("Treasurebox_"):
                    continue
                elif exit_name.startswith("Wall_"):
                    continue
                elif exit_name.startswith("N"):
                    location_type = "_Shard"
                elif exit_name.startswith("Fam"):
                    location_type = "_Shard"
                else:
                    continue
                
                key = (room_id, exit_name + location_type)
                if key not in all_rules:
                    # print(key)
                    all_rules[key] = requirements
    
    return all_rules

if __name__ == "__main__":

    flat_rules = flatten_requirements(ALL_ENTRANCE_RULES)
    
    location_rules = build_location_rules()
    locations_with_or_without_rules = build_location_with_or_without_rules()
    flat_location_rules = flatten_requirements(location_rules)
    print(flat_location_rules)
    
    dict_output = entrance_dict_template.render(entrance_rules=flat_rules, format_rule=format_rule)
    with open("../generated/rules.py", "w") as file:
        file.write(dict_output)

    dict_output = location_dict_template.render(location_rules=flatten_requirements(locations_with_or_without_rules), format_rule=format_rule)
    with open("../generated/enemies.py", "w") as file:
        file.write(dict_output)

    location_output = location_dict_template.render(location_rules=flat_location_rules, format_rule=format_rule)
    with open("../generated/rules_location.py", "w") as file:
        file.write(location_output)
        file.write(".")

    # Generate split enemy regions by difficulty using all locations (with or without rules)
    flat_locs_no_rules = flatten_requirements(locations_with_or_without_rules)
    enemy_regions_split = build_enemy_regions_split(flat_locs_no_rules)
    
    # Compute flattened list in Python (deduplicated)
    enemy_flattened = sorted(set(
        region 
        for regions in enemy_regions_split.values() 
        for dests in regions.values() 
        for region in dests
    ))
    
    enemy_output = enemy_dict_template.render(enemy_regions=enemy_regions_split, enemy_flattened=enemy_flattened)
    with open("../generated/enemy_regions.py", "w") as file:
        file.write(enemy_output)
