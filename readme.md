### This repository contains scripts and data for analyzing the results of the DUCSU election.

## Structure

- analyze_winners.py: Python script to analyze winners for each post.
- `DUCSU Result - Updated.csv`: Main results data (required for analysis).
- `charts_svg/` & charts_png: Visualizations of results.
- `cadidates info.csv` & `cadidates info.json`: Candidate details.
- Other CSV files: Additional extracted and formatted results.

## Usage

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Run analysis**  
   ```
   python analyze_winners.py
   ```

   Output:  
   ```
   Post, Winner, Winner Votes, Total Votes, Percentage
   ...
   ```

## Data Sources

- Election results and candidate information are provided in CSV and JSON formats.
- Visualizations are available in SVG and PNG formats.

## Requirements

See requirements.txt for required Python packages.

## License

This project is for academic and research purposes. Please cite appropriately if used.