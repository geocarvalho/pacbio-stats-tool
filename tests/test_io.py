import unittest
from pacbio_stats_tool.core.coverage import calculate_n50

class TestCoverage(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.simple_coverage = {
            'contig1': 10,
            'contig2': 20,
            'contig3': 15,
            'contig4': 5
        }

    def test_calculate_n50(self):
        # Test with a simple coverage dataset
        n50 = calculate_n50(self.simple_coverage)
        self.assertEqual(n50, 15)
        
    def test_calculate_n50_empty(self):
        # Test with empty coverage data
        coverage_data = {}
        n50 = calculate_n50(coverage_data)
        self.assertEqual(n50, 0)
        
    def test_calculate_n50_single_contig(self):
        # Test with a single contig
        coverage_data = {'contig1': 100}
        n50 = calculate_n50(coverage_data)
        self.assertEqual(n50, 100)

    def test_discovery(self):
        """Simple test to verify test discovery"""
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main(verbosity=2)