from .bases import BloodstainedTestBase


class TestLocationAccess(BloodstainedTestBase):
    """Test location access and logic for Bloodstained"""

    def test_all_chest_locations_exist(self) -> None:
        """Test that chest locations are properly defined"""
        locations = list(self.multiworld.get_locations(self.player))
        chest_locations = [loc for loc in locations if "Treasurebox" in loc.name]

        self.assertGreater(len(chest_locations), 0,
                          "Should have chest locations")

    def test_location_ids_valid(self) -> None:
        """Test that all locations have valid IDs"""
        locations = list(self.multiworld.get_locations(self.player))
        for location in locations:
            if location.address:  # Only check locations with actual IDs
                self.assertGreater(location.address, 0,
                                  f"Location {location.name} should have valid ID")

    def test_locations_have_regions(self) -> None:
        """Test that all locations are assigned to valid regions"""
        locations = list(self.multiworld.get_locations(self.player))
        for location in locations:
            self.assertIsNotNone(location.parent_region,
                               f"Location {location.name} should have a parent region")
