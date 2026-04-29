from .bases import BloodstainedTestBase


class TestBasicAccess(BloodstainedTestBase):
    """Test basic location access logic for Bloodstained"""

    def test_starting_region_accessible(self) -> None:
        """Test that the starting region has accessible locations"""
        starting_region = self.world.get_region("m01SIP_000")
        self.assertIsNotNone(starting_region, "Starting region should exist")

        accessible_locations = self.multiworld.get_reachable_locations(self.multiworld.state, self.player)
        starting_locations = [loc for loc in accessible_locations if loc.parent_region == starting_region]
        self.assertGreater(len(starting_locations), 0,
                          "Should be able to access at least one location in starting region")

    def test_can_reach_tutorial_chest(self) -> None:
        """Test that the tutorial chest is reachable from the start"""
        location = self.multiworld.get_location("Treasurebox_SIP000_Tutorial.0", self.player)
        self.assertTrue(location.can_reach(self.multiworld.state),
                       "Tutorial chest should be reachable from start")

    def test_item_pool_count(self) -> None:
        """Test that items are created in appropriate quantities"""
        items = [item for item in self.multiworld.itempool
                 if item.player == self.player]

        # Count progression items (should include weapons and important items)
        progression_items = [item for item in items if item.advancement]
        self.assertGreater(len(progression_items), 0,
                          "Should have progression items in pool")

        # Count filler items (ingredients, materials, etc.)
        filler_items = [item for item in items if item.filler]
        self.assertGreater(len(filler_items), 0,
                          "Should have filler items in pool")
