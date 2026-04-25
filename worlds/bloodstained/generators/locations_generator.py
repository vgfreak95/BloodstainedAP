import json
from collections import Counter
from dataclasses import dataclass
from enum import Enum
import jinja2

class LocationType(Enum):
    CHEST = 0
    ENEMY = 1
    WALL = 2

@dataclass
class RitualLocationData:
    id: int
    name: str
    type: LocationType
    item_count: int = 1

# RitualLocationData(id=0xb100d, name="Treasurebox_SIP000_Tutorial", region="SIP" type=LocationType.GREEN_CHEST, item_count=2)


with open("../data/Archipelago.json") as ap_file:
    ap = json.load(ap_file)

with open("../data/PB_DT_ItemMaster.json") as item_dt:
    dt_item = json.load(item_dt)

template = jinja2.Template("""# Auto-generated file

from dataclasses import dataclass
from enum import Enum


ITEMS_DATA = {
{%- for location in locations %}
    "{{ location['name'] }}": RitualLocationData(id={{ location['id'] }}, name="{{ location['name'] }}", type={{ location['type'] }}, region="{{ location['region'] }}"),
{%- endfor %}
}
""")

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

def get_location_check_count() -> dict[str, int]:
    location_checks_count = []
    for ap_item in ap["Items"]:
        for _ in ap["Items"][ap_item]:
            location_checks_count.append(ap_item)

    location_counter = Counter(location_checks_count)
    return location_counter

def get_locations_and_rooms(locations: list[str]) -> dict[str, str]:

    locations_to_rooms = {}
    for location in locations:
        try:
            print(location)
            _, area_id, _ = location.split("_")
            room_id = area_id[3:]
            full_area = region_to_area_id[area_id[:3]]
            room_of_location = f"{full_area}_{room_id}"
            locations_to_rooms.update({location: room_of_location})
        except:
            continue
    return locations_to_rooms

if __name__ == "__main__":
    # output = template.render(items=item_counter)
    locations = []

    locations_count = get_location_check_count()
    locations_to_rooms = get_locations_and_rooms(list(locations_count))

    id = 0xb100d
    for location, count in locations_count.items():
        # RitualLocationData(id=0xb100d, name="Treasurebox_SIP000_Tutorial", region="SIP" type=LocationType.GREEN_CHEST, item_count=2)
        try:
            if count == 1:
                locations.append({"name": f"{location}", "id": hex(id), "region": locations_to_rooms[location], "type": LocationType.CHEST})
                id += 1
            elif count > 1:
                for num in range(count):
                    locations.append({"name": f"{location}.{num}", "id": hex(id), "region": locations_to_rooms[location], "type": LocationType.CHEST})
                    id += 1
        except:
            continue

    # print(json.dumps(locations, sort_keys=True, indent=4))
    #print(locations)

    locations_data_output = template.render(locations=locations)
    print(locations_data_output)


    with open("../generated/locations.py", "w") as generated_items:
        generated_items.write(locations_data_output)






