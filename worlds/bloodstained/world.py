from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from BaseClasses import Region

from . import items, locations, regions, rules


class RitualWorld(World):
    """
    Bloodstained: Ritual of the Night is a fantastic game!
    """

    game = "Bloodstained"

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "m01SIP_000"

    def create_region(self, region_name: str):
        return Region(region_name, self.player, self.multiworld)


    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)
        # print("MENU REGION CREATED: ", self.get_entrance("m01SIP_000"))

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    # We also put this in a different file, the same one that create_items is in.
    def create_item(self, name: str) -> items.RitualItem:
        place_item = items.place_item_in_ritual_world(self)
        return place_item(name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    # The way it does this is by calling get_filler_item_name.
    # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
    # You must override this function and return this infinitely repeatable item's name.
    # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    # def fill_slot_data(self) -> Mapping[str, Any]:
    #     # If you need access to the player's chosen options on the client side, there is a helper for that.
    #     return self.options.as_dict(
    #         "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
    #     )
