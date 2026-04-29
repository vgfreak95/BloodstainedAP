from .bases import BloodstainedTestBase
from .. import items as ritual_items


class TestChestStartsWithWeaponOff(BloodstainedTestBase):
    options = {
        "chest_starts_with_weapon": False,
    }

    run_default_tests = False

    def test_tutorial_chest_not_locked(self) -> None:
        """Test that when chest_starts_with_weapon is off, the tutorial chest is not pre-filled"""
        location = self.multiworld.get_location("Treasurebox_SIP000_Tutorial.0", self.player)
        # When chest_starts_with_weapon is off, pre_fill doesn't place a locked item
        # The item will be placed during normal fill phase
        self.assertIsNone(location.item, "Tutorial chest should not have a locked item when option is off")


class TestChestStartsWithWeaponOn(BloodstainedTestBase):
    options = {
        "chest_starts_with_weapon": True,
    }

    def test_tutorial_chest_has_weapon(self) -> None:
        """Test that when chest_starts_with_weapon is on, the tutorial chest has a weapon"""
        # pre_fill should have been called during setUp/world_setup
        location = self.multiworld.get_location("Treasurebox_SIP000_Tutorial.0", self.player)
        self.assertIsNotNone(location.item, "Tutorial chest should have a weapon")
        if location.item:
            # Get all weapon names from the items module
            weapon_names = [name for name, data in ritual_items.ALL_RITUAL_ITEMS.items()
                          if data.category == ritual_items.RitualItemCategory.WEAPON]
            self.assertIn(location.item.name, weapon_names,
                          f"Tutorial chest should contain a weapon, got {location.item.name}")
