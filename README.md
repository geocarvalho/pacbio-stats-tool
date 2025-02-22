# PacBio Stats Tool

A tool to calculate coverage from PacBio BAM files and output the results as JSON.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pacbio-stats-tool.git
cd pacbio-stats-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```bash
python pacbio_stats_tool/cli.py <bam_file> --output <output_file>
```

Example:
```bash
python pacbio_stats_tool/cli.py test.bam --output coverage.json
```

## Testing

To run the tests:
```bash
python -m unittest discover -s tests
```
