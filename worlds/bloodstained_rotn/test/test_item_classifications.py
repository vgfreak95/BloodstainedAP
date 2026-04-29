from .bases import BloodstainedTestBase


class TestItemClassifications(BloodstainedTestBase):
    """Test that items have correct classifications"""

    def test_weapons_are_useful(self) -> None:
        """Test that weapon items have useful classification"""
        weapon_items = self.get_items_by_name([
            "Knife", "Short Sword", "Baselard", "Ulfberht Sword"
        ])
        self.assertGreater(len(weapon_items), 0, "Should have weapon items")
        for item in weapon_items:
            self.assertTrue(item.useful or item.advancement,
                          f"{item.name} should be useful or progression")

    def test_potions_are_useful(self) -> None:
        """Test that potion items have useful classification"""
        potion_items = self.get_items_by_name([
            "Potion", "High Potion", "Ether", "Mithridate"
        ])
        self.assertGreater(len(potion_items), 0, "Should have potion items")
        for item in potion_items:
            self.assertTrue(item.useful or item.filler,
                          f"{item.name} should be useful or filler")

    def test_ingredients_are_filler(self) -> None:
        """Test that ingredient items are filler"""
        ingredient_items = self.get_items_by_name([
            "Bronze", "Iron", "Silver", "Gold"
        ])
        self.assertGreater(len(ingredient_items), 0, "Should have ingredient items")
