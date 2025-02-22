import pysam

def calculate_bam_coverage(bam_file):
    """
    Calculate coverage from a BAM file and return a dictionary with coverage data.
    """
    coverage_data = {}
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam:
            if read.reference_name not in coverage_data:
                coverage_data[read.reference_name] = 0
            coverage_data[read.reference_name] += 1
    return coverage_data