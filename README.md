# NBI GridFS
> This Repository contains python scripts to import NBI media files in MongoDB


## About NBI

National Bridge Inventory (NBI) represents bridge data submitted annually to FHWA by the States, Federal agencies, and Tribal governments.The data conforms to the [Recording and Coding Guide for the Structure Inventory and Appraisal of the Nations Bridges](https://www.fhwa.dot.gov/bridge/mtguide.pdf). Each data set is submitted in the spring, and may be corrected or updated throughout the year. The data is considered final and is published on this website at the end of each calendar year. [Source: [Federal Highway Administration](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm)]

The Python script downloads CSV and zip file directly from the FHWA website. This features ensures that all transformations to the dataset are accounted for. 

## Simple Crawler: Download NBI and Convert to JSON at the same time 

```bash

python3 NbiCrawler.py

```
## Advanced Crawler: Separate scripts to download and then process NBI data

This crawler creates a local copy of NBI files. This prevents uncessary requests to the server during the processing stage.

```bash
# Change Directory to nbiSeparateFiles
cd nbiSeparateFiles

# Start NBI File Download for all years
python3 Downloadv1.py

# Decompress Zip files and convert CSV files to JSON
python3 ProcessMain.py

```
### Download Configuration

Downloadv1.py, contains two global lists to configure the states and years for which files are to downloaded. By default the  two lists includes all states and years.

```python
states = ['NE','AL','AK',..]
years = [1992,1993,1994..]
```
Downloadv1.py output includes the following items:  
1. `NBIDATA` folder. This folder includes all bridge inspection files for all states and years in the configuration list. The files are renamed following this convention: `XXYYYY.txt`. `XX` representes the two digit state code and `YYYY` represents the year of reporting into NBI.


### Processing Configuration

ProcessMain.py, contains two global lists to configure the states and years for which files are to downloaded. To limit processing time, by default the states list only includes Nebraska ['NE']. The years list by default includes all years.

```python
states = ['NE']
years = [1992,1993,1994..]
```
ProcessMain.py output includes the following items:  
1. `missinggeo.txt` This text file will include all structure Number and year, where geo coordinates are invalid
2. `Summary.txt` This text file will include basic summary of this processing run
3. `mergedNBI.json` This text file includes JSON objects converted from csv rows
