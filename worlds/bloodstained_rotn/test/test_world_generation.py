from .bases import BloodstainedTestBase


class TestWorldGeneration(BloodstainedTestBase):
    """Test basic world generation for Bloodstained"""

    def test_world_creates_regions(self) -> None:
        """Test that the world creates regions properly"""
        self.assertGreater(len(self.world.multiworld.regions), 0,
                          "World should have regions")

    def test_world_has_locations(self) -> None:
        """Test that the world has locations"""
        locations = list(self.multiworld.get_locations(self.player))
        self.assertGreater(len(locations), 0, "World should have locations")

    def test_world_has_items(self) -> None:
        """Test that the world creates items"""
        items = [item for item in self.multiworld.itempool
                 if item.player == self.player]
        self.assertGreater(len(items), 0, "World should have items in pool")
