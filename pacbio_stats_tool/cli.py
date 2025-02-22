import argparse
import json
from pacbio_stats_tool.io.bam_reader import read_bam_and_calculate_coverage
from pacbio_stats_tool.core.coverage import calculate_n50

def main():
    parser = argparse.ArgumentParser(description="Calculate coverage from a BAM file and output JSON.")
    parser.add_argument("bam_file", help="Path to the input BAM file")
    parser.add_argument("--output", "-o", help="Path to the output JSON file", default="coverage.json")
    args = parser.parse_args()

    coverage_data = read_bam_and_calculate_coverage(args.bam_file)
    n50_value = calculate_n50(coverage_data)  # Call to calculate_n50
    coverage_data["N50"] = n50_value  # Add N50 value to coverage data

    with open(args.output, "w") as f:
        json.dump(coverage_data, f, indent=4)
    print(f"Coverage data saved to {args.output}")

if __name__ == "__main__":
    main()