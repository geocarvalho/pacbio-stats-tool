import unittest
from pacbio_stats_tool.core.coverage import calculate_bam_coverage

class TestCoverage(unittest.TestCase):
    def test_calculate_bam_coverage(self):
        bam_file = "tests/data/test.bam"
        coverage_data = calculate_bam_coverage(bam_file)
        self.assertIsInstance(coverage_data, dict)
        self.assertEqual(coverage_data["chr1"], 2)
        self.assertEqual(coverage_data["chr2"], 1)

if __name__ == "__main__":
    unittest.main()