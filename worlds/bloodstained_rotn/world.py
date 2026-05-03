from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from BaseClasses import Region

from . import items, locations, regions, rules, options as ritual_options, web_world


class RitualWorld(World):
    """
    Bloodstained: Ritual of the Night is a fantastic game!
    """

    game = "Bloodstained: Ritual of the Night"

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "m01SIP_000"
    web = web_world.RitualWebWorld()

    options_dataclass = ritual_options.RitualOptions
    options: ritual_options.RitualOptions

    locations_without_progression = [
        "Treasurebox_SIP020_1",
        "Treasurebox_VIL005_1",
    ]

    def create_region(self, region_name: str):
        return Region(region_name, self.player, self.multiworld)

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)
        # print("MENU REGION CREATED: ", self.get_entrance("m01SIP_000"))

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def pre_fill(self) -> None:

        if self.options.chest_starts_with_weapon:
            item = self.create_item(self.items_to_remove["starting_weapon"])
            location = self.multiworld.get_location("Treasurebox_SIP000_Tutorial.0", self.player)
            location.place_locked_item(item)
            self.multiworld.itempool.remove(item)


        for location in self.locations_without_progression:
            filler_item = self.items_to_remove["locations_without_progression"].pop()
            location_without_progression = self.multiworld.get_location(location, self.player)
            location_without_progression.place_locked_item(filler_item)
            self.multiworld.itempool.remove(filler_item)


    def create_items(self) -> None:

        items.create_all_items(self)
        self.items_to_remove = {}

        if self.options.chest_starts_with_weapon:
            self.starting_weapon = items.get_random_starting_weapon(self)
            for item in self.multiworld.itempool:
                if item.player == self.player and item.name == self.starting_weapon:
                    self.items_to_remove["starting_weapon"] = item.name
                    break

        self.items_to_remove["locations_without_progression"] = []
        for _ in self.locations_without_progression:
            filler_item = items.get_random_filler_item_name(self)
            for item in self.multiworld.itempool:
                if item.player == self.player and item.name == filler_item:
                    self.items_to_remove["locations_without_progression"].append(item)
                    break

    def create_item(self, name: str) -> items.RitualItem:
        place_item = items.place_item_in_ritual_world(self)
        return place_item(name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
