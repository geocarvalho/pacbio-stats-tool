import unittest
from pacbio_stats_tool.io.bam_reader import read_bam_and_calculate_coverage

class TestBamReader(unittest.TestCase):
    def test_read_bam_and_calculate_coverage(self):
        # Mock BAM file or use a small test BAM file
        bam_file = "tests/data/test.bam"
        coverage_data = read_bam_and_calculate_coverage(bam_file)
        self.assertIsInstance(coverage_data, dict)
        self.assertTrue(len(coverage_data) > 0)

if __name__ == "__main__":
    unittest.main()