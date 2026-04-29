"""
Extract regions, entrances, and locations from Archipelago world JSON.

Structure:
  {
    "ROOM_KEY": {                    <- room (emitted as region)
      "ENTRANCE_KEY": {              <- entrance (has children)
        "LOCATION_KEY": [],          <- location (leaf, value is [])
        "ENTRANCE_KEY": []           <- reachable entrance (also a leaf)
      },
      "ENTRANCE_KEY": []             <- entrance (leaf at depth 1)
    }
  }

Rules:
  - depth 0  -> region  (the room key)
  - depth 1  -> entrance (whether leaf or block)
  - depth 2+ leaf ([]) -> location
  - depth 2+ block ({}) -> entrance (reachable from parent entrance)
"""

import json
import sys
from collections import defaultdict


def walk(obj, depth=0, regions=None, entrances=None, locations=None,
         seen_entrances=None, seen_locations=None):
    if regions is None:
        regions = []
        entrances = []
        locations = []
        seen_entrances = set()
        seen_locations = set()

    for key, value in obj.items():
        is_leaf = isinstance(value, list)

        if depth == 0:
            regions.append(key)

        elif depth == 1:
            if key not in seen_entrances:
                seen_entrances.add(key)
                entrances.append(key)

        else:
            # depth 2+
            if is_leaf:
                if key not in seen_locations:
                    seen_locations.add(key)
                    locations.append(key)
            else:
                # block at depth 2+ = reachable entrance
                if key not in seen_entrances:
                    seen_entrances.add(key)
                    entrances.append(key)

        if not is_leaf:
            walk(value, depth + 1, regions, entrances, locations,
                 seen_entrances, seen_locations)

    return regions, entrances, locations


def format_output(regions, entrances, locations):
    lines = []

    def section(kind, keys):
        lines.append(f"# {'=' * 50}")
        lines.append(f"# {kind.upper()}S ({len(keys)})")
        lines.append(f"# {'=' * 50}")
        lines.append(f"{kind}_aliases = {{")
        for k in keys:
            lines.append(f'    "{k}": "",')
        lines.append("}")
        lines.append("")

    section("region", regions)
    section("entrance", entrances)
    section("location", locations)
    return "\n".join(lines)


EXAMPLE = {
    "m01SIP_000": {
        "SIP_000_START": {
            "SIP_000_1_0_RIGHT_BOTTOM": [],
            "Treasurebox_SIP000_Tutorial": []
        },
        "SIP_000_1_0_RIGHT_BOTTOM": {
            "Treasurebox_SIP000_Tutorial": []
        }
    }
}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        print("No file provided — running on built-in example.\n")
        data = EXAMPLE

    regions, entrances, locations = walk(data)
    print(format_output(regions, entrances, locations))
    generate_locations_file()
