from pacbio_stats_tool.core.coverage import calculate_bam_coverage

def read_bam_and_calculate_coverage(bam_file):
    """
    Read a BAM file and calculate coverage.
    """
    return calculate_bam_coverage(bam_file)