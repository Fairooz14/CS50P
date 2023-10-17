import unittest
from project import calculate_lunar_phase_for_date, display_lunar_phase
import ephem

class TestLunarPhaseTracker(unittest.TestCase):
    def test_calculate_lunar_phase_for_date(self):
        # Test for a known phase (Full Moon) using ephem
        date = "2023-10-20"  # A known Full Moon date
        expected_phase = ephem.Moon(date).phase // 100  # Calculate the expected phase using ephem
        self.assertEqual(calculate_lunar_phase_for_date(date), expected_phase)

    def test_display_lunar_phase(self):
        # Test for displaying the phase name
        self.assertEqual(display_lunar_phase(0), "New Moon")
        self.assertEqual(display_lunar_phase(1), "First Quarter")
        self.assertEqual(display_lunar_phase(2), "Full Moon")
        self.assertEqual(display_lunar_phase(3), "Last Quarter")

if __name__ == '__main__':
    unittest.main()
