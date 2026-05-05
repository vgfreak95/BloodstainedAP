from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle, DeathLink, StartInventory

class StartChestHasWeapon(Toggle):
    """
    Guarantees Starting Chest will have a Weapon
    """

    display_name = "Starting Chest has Weapon"


class VerticalProgressiveMovement(Choice):
    """
    Use Progressive Vertical Movement, Double Jump -> High Jump -> Dimension Shift

    Dimension Shift is extremely overpowered, so this forces it to appear
    in later spheres.
    """

    display_name = "Vertical Progressive Movement"
    option_progressive = 0
    option_separate = 1
    default = 1

class DropExperienceMultiplier(Range):
    """
    Modifies Drop Experience Multiplier from any Enemies killed.

    When set to 2, the player will recieve double the experience from enemies.
    """

    display_name = "Experience Multiplier"
    range_start = 1
    range_end = 100
    default = 2

class DropMoneyMultiplier(Range):
    """
    Modifies Money Dropped Multiplier from any Enemies killed.

    When set to 2, the player will recieve double the experience from enemies.
    """

    display_name = "Drop Money Multiplier"
    range_start = 1
    range_end = 100
    default = 1

class DropShardMultipler(Range):
    """
    Modifies Shard Dropped Multiplier from any Enemies killed.

    When set to 2, the player will double the drop shard chance from enemies.
    """

    display_name = "Drop Shard Multiplier"
    range_start = 1
    range_end = 100
    default = 2

class DropItemMultiplier(Range):
    """
    Modifies Item Dropped Multiplier from any Enemies killed.

    When set to 2, the player will recieve double the items from enemies.
    """

    display_name = "Drop Item Multiplier"
    range_start = 1
    range_end = 100
    default = 1



@dataclass
class RitualOptions(PerGameCommonOptions):
    chest_starts_with_weapon: StartChestHasWeapon
    death_link: DeathLink
    start_inventory: StartInventory
    drop_experience_multiplier: DropExperienceMultiplier
    drop_money_multiplier: DropMoneyMultiplier
    drop_shard_multiplier: DropShardMultipler
    drop_item_multiplier: DropItemMultiplier
    # vertical_progressive_movement: VerticalProgressiveMovement
