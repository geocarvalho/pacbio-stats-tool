import argparse
import json
from pacbio_stats_tool.io.bam_reader import read_bam_and_calculate_coverage

def main():
    parser = argparse.ArgumentParser(description="Calculate coverage from a BAM file and output JSON.")
    parser.add_argument("bam_file", help="Path to the input BAM file")
    parser.add_argument("--output", "-o", help="Path to the output JSON file", default="coverage.json")
    args = parser.parse_args()

    coverage_data = read_bam_and_calculate_coverage(args.bam_file)
    with open(args.output, "w") as f:
        json.dump(coverage_data, f, indent=4)
    print(f"Coverage data saved to {args.output}")

if __name__ == "__main__":
    main()