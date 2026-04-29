from BaseClasses import CollectionState
from .bases import BloodstainedTestBase


class TestRulesSet(BloodstainedTestBase):
    """Test that rules are properly set for locations and entrances"""

    def test_dimension_shift_access(self) -> None:
        """Test that locations requiring Dimension Shift need Dimension Shift"""
        # From rules.py, Treasurebox_SAN003_1 requires Dimension Shift OR Reflector Ray
        self.assertAccessDependency(
            ["Treasurebox_SAN003_1"],
            [["Dimension Shift"], ["Reflector Ray"]],
            only_check_listed=True,
        )

    def test_gdn006_1_requires_dimension_shift_or_craftwork(self) -> None:
        """Test that Treasurebox_GDN006_1 requires Dimension Shift OR Craftwork"""
        self.assertAccessDependency(
            ["Treasurebox_GDN006_1"],
            [["Dimension Shift"], ["Craftwork"]],
            only_check_listed=True,
        )

    def test_starting_area_accessible(self) -> None:
        """Test that starting area (m01SIP_000) is accessible without any items"""
        state = CollectionState(self.multiworld)
        location = self.multiworld.get_location("Treasurebox_SIP000_Tutorial.0", self.player)
        self.assertTrue(location.can_reach(state),
                       "Starting area should be accessible without items")

    def test_all_state_can_reach_everything(self) -> None:
        """Override to skip - already tested in base"""
        pass

    def test_empty_state_can_reach_something(self) -> None:
        """Override to skip - already tested in base"""
        pass

    def test_fill(self) -> None:
        """Override to skip - already tested in base"""
        pass
