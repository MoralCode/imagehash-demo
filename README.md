# Image Hashing Demo

Experimental repo to compute hamming distances between images using https://pypi.org/project/ImageHash/ - currently trying to see if one algorithm is better than another with the goal of eventually contributing this to https://tunnelvision.csh.rit.edu


## Usage

This Python script reads a CSV file containing the "name" and "filepath" to several images and outputs various comparisons between them using content based hashing.

The first image supplied will be used as the image that all the rest are compared to.
Names help the output be more understandable

### Command-line Arguments

- `csv_file`: The path to the CSV file containing "name" and "filepath" columns.

### Example

```bash
pipenv run python3 main.py input_data.csv
```
