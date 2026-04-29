from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle

class StartChestHasWeapon(Toggle):
    """
    Guarantees Starting Chest will have a Weapon
    """

    display_name = "Starting Chest has Weapon"


class VerticalProgressiveMovement(Choice):
    """
    Guarantees Starting Chest will have a Weapon
    Use Progressive Vertical Movement, Double Jump -> High Jump -> Dimension Shift

    Dimension Shift is extremely overpowered, so this forces it to appear
    in later spheres.
    """

    display_name = "Vertical Progressive Movement"
    option_progressive = 0
    option_separate = 1
    default = 1


@dataclass
class RitualOptions(PerGameCommonOptions):
    chest_starts_with_weapon: StartChestHasWeapon
    # vertical_progressive_movement: VerticalProgressiveMovement
