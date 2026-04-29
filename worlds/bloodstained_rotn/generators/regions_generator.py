import json
from collections import Counter
from dataclasses import dataclass
from enum import Enum
import jinja2


with open("../data/Archipelago.json") as ap_file:
    ap = json.load(ap_file)

with open("../data/PB_DT_RoomMaster.json") as item_dt:
    dt_room = json.load(item_dt)

template = jinja2.Template("""# Auto-generated file

from dataclasses import dataclass
from enum import Enum

@dataclass
class RitualRegion:
    alias: str
    connections: dict[str, list]
    entrances: dict[str, list]


ITEMS_DATA = {
{%- for name, region_data in regions.items() %}
    "{{ name }}": RitualRegion(alias="{{ region_data.alias }}", connections={{ region_data.connections }}, entrances={{ region_data.entrances }}),
{%- endfor %}
}
""")

@dataclass
class RitualRegion:
    alias: str
    connections: dict[str, list]
    entrances: dict[str, list]


areas_to_regions = {
    'SIP': RitualRegion(alias="Galleon Minerva", connections={}, entrances={}),
    'VIL': RitualRegion(alias='Village', connections={}, entrances={}),
    'ENT': RitualRegion(alias='Entrance', connections={}, entrances={}),
    'GDN': RitualRegion(alias='Garden of Silence', connections={}, entrances={}),
    'SAN': RitualRegion(alias='Dian Cecht Cathedral', connections={}, entrances={}),
    'LIB': RitualRegion(alias='Livre Ex Machina', connections={}, entrances={}),
    'TWR': RitualRegion(alias='Tower of Twin Dragons', connections={}, entrances={}), 
    'TRN': RitualRegion(alias='Runaway Train', connections={}, entrances={}), 
    'TAR': RitualRegion(alias='Secret Sorcery Lab', connections={}, entrances={}), 
    'BIG': RitualRegion(alias='Den of Behemoths', connections={}, entrances={}), 
    'JPN': RitualRegion(alias='Oriental Sorcery Lab', connections={}, entrances={}),
    'UGD': RitualRegion(alias='Forbidden Underground Waterway', connections={}, entrances={}),
    'RVA': RitualRegion(alias='Inferno Cave', connections={}, entrances={}),
    'SND': RitualRegion(alias='Hidden Desert', connections={}, entrances={}),
    'ARC': RitualRegion(alias='Underground Sorcery Lab', connections={}, entrances={}),
    'ICE': RitualRegion(alias='Glacial Tomb', connections={}, entrances={}),
    'EBT': RitualRegion(alias='8 Bit Nightmare', connections={}, entrances={}),
    'JRN': RitualRegion(alias='The Tunnels', connections={}, entrances={}),
    'LBP': RitualRegion(alias='Bael Arena', connections={}, entrances={}),
    'BKR': RitualRegion(alias='Millionaires Room', connections={}, entrances={}),
    'K2C': RitualRegion(alias='Dead Lands', connections={}, entrances={}),
    'KNG': RitualRegion(alias='Hall of Termination', connections={}, entrances={})
}

regions_lookup = {
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

region_to_area_id = {
    "ARC": "m13ARC",
    "BIG": "m10BIG",
    "BKR": "m88BKR",
    "EBT": "m51EBT",
    "ENT": "m03ENT",
    "GDN": "m04GDN",
    "ICE": "m18ICE",
    "JPN": "m15JPN",
    "JRN": "m20JRN",
    "K2C": "m19K2C",
    "KNG": "m06KNG",
    "LBP": "m77LBP",
    "LIB": "m07LIB",
    "RVA": "m17RVA",
    "SAN": "m05SAN",
    "SIP": "m01SIP",
    "SND": "m12SND",
    "TAR": "m14TAR",
    "TRN": "m09TRN",
    "TWR": "m08TWR",
    "UGD": "m11UGD",
    "VIL": "m02VIL"
}


def get_connecting_rooms_for_room(name: str) -> list[str]:
    adjactent_rooms = dt_room[0]["Rows"][name]["AdjacentRoomName"]
    return adjactent_rooms

def get_entrances_for_room(name: str) -> dict[str, list[str]]:
    entrances = ap["Doors"][name]
    return entrances

if __name__ == "__main__":

    regions_not_mapped = set()
    for room_name in dt_room[0]["Rows"]:
        rooms = get_connecting_rooms_for_room(room_name)
        entrances = get_entrances_for_room(room_name)
        if rooms == []:
            continue
        area_id = room_name[3:6]
        try: 
            ritual_region = areas_to_regions[area_id].connections.update({room_name: rooms})
            ritual_entrances = areas_to_regions[area_id].entrances.update(entrances)
        except:
            regions_not_mapped.add(area_id)
            continue
        
    # print(areas_to_regions["VIL"].entrances)

    items_data_output = template.render(regions=areas_to_regions)

    for area, data in areas_to_regions.items():
        if len(data.connections.keys()) != 0:
            compare_id = list(data.connections.keys())[0].split("_")[0]
            area_name = compare_id[:3]
            area_id = compare_id[3:]
            if area == area_id:
                region_to_area_id[area_id] = compare_id



    with open("../generated/regions.py", "w") as generated_items:
        generated_items.write(items_data_output)

    print(json.dumps(region_to_area_id, sort_keys=True, indent=4))
