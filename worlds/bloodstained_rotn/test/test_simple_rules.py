from BaseClasses import CollectionState
from .bases import BloodstainedTestBase


class TestSimpleRules(BloodstainedTestBase):
    """Simple tests to verify rules are working"""

    def test_san003_requires_dimension_shift(self) -> None:
        """Test that Treasurebox_SAN003_1 requires Dimension Shift or Reflector Ray"""
        location = self.multiworld.get_location("Treasurebox_SAN003_1", self.player)
        
        # With empty state, should NOT be reachable
        state = CollectionState(self.multiworld)
        self.assertFalse(location.can_reach(state),
                       "Should not reach SAN003 without Dimension Shift or Reflector Ray")
        
        # With Dimension Shift, should be reachable
        self.collect_by_name("Dimension Shift")
        self.assertTrue(location.can_reach(self.multiworld.state),
                      "Should reach SAN003 with Dimension Shift")

    def test_gdn006_1_requires_dimension_shift_or_craftwork(self) -> None:
        """Test that Treasurebox_GDN006_1 requires Dimension Shift or Craftwork"""
        location = self.multiworld.get_location("Treasurebox_GDN006_1", self.player)
        
        # With empty state, should NOT be reachable
        state = CollectionState(self.multiworld)
        self.assertFalse(location.can_reach(state),
                       "Should not reach GDN006_1 without Dimension Shift or Craftwork")
        
        # With Dimension Shift, should be reachable
        self.collect_by_name("Dimension Shift")
        self.assertTrue(location.can_reach(self.multiworld.state),
                      "Should reach GDN006_1 with Dimension Shift")

    def test_all_state_can_reach_everything(self) -> None:
        pass

    def test_empty_state_can_reach_something(self) -> None:
        pass

    def test_fill(self) -> None:
        pass
