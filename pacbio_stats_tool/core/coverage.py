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

def calculate_n50(coverage_data):
    """
    Calculate the N50 value from coverage data.
    The N50 is the minimum contig length such that the sum of the lengths of all contigs
    of that length or longer is at least half the total length of all contigs.
    """
    lengths = sorted(coverage_data.values(), reverse=True)
    total_length = sum(lengths)
    half_total = total_length / 2
    running_sum = 0

    for length in lengths:
        running_sum += length
        if running_sum >= half_total:
            return length
    return 0  # In case there are no reads