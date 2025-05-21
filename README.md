# DNA Analysis Based on Genetic Markers

## Project Overview

This Python-based application performs DNA profiling by analyzing Short Tandem Repeats (STRs) in DNA sequences. The program identifies individuals by comparing their DNA STR counts against a database of known profiles, similar to how forensic DNA analysis and genetic genealogy work in real-world applications.

## How It Works

The program takes two command-line arguments:
1. A CSV file containing STR counts for a list of individuals
2. A text file containing the DNA sequence to identify

The algorithm:
1. Reads the database of individuals and their STR counts
2. Reads the target DNA sequence
3. For each STR pattern, computes the longest run of consecutive repeats in the DNA sequence
4. Compares the computed STR counts against each individual in the database
5. Outputs the name of the matching individual, or "No match" if no match is found

## Technical Implementation

The core of the application relies on the `longest_match` function, which identifies the maximum number of times a specific STR pattern repeats consecutively in a DNA sequence. This is a common bioinformatics challenge that requires efficient string pattern matching.

The program uses:
- Python's CSV module for database handling
- Efficient string manipulation techniques
- Command-line argument processing

## Usage

```
python dna.py databases/large.csv sequences/5.txt
```

## Files in the Repository

- `dna.py`: Main Python script that performs the DNA analysis
- `sequences/`: Directory containing DNA sequence files for testing
  - Each numbered text file contains a different DNA sequence to analyze

## Future Development Potential

This project could be extended for digital health applications in several ways:

1. Integration with electronic health records for genetic risk assessment
2. Development of a web interface for clinical use
3. Expansion to analyze more complex genetic markers relevant to disease risk
4. Implementation of machine learning algorithms to improve matching accuracy
5. Application in pharmaceutical care for medication selection based on genetic profiles

## Skills Demonstrated

- Computational biology algorithms
- Genetic data processing
- Python programming
- Command-line application development
- Bioinformatics concepts relevant to digital health
- Data analysis techniques applicable to healthcare datasets


This project demonstrates:

1. Application of data engineering concepts to biological information
2. Understanding of the intersection between IT and healthcare/medicine
3. Practical implementation of algorithms relevant to personalized medicine
4. Experience with healthcare data processing and analysis
5. Interdisciplinary thinking connecting programming, genetics, and pharmaceutical care

The project showcases my ability to work at the interface between computer science and healthcare, which is a core focus of the Digital Health program. The techniques demonstrated here have direct applications in the evolving field of precision medicine, where genetic information increasingly guides healthcare decisions and treatment approaches.
