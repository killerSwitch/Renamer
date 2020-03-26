# Renamer
A simple python script to rename all files in the specified path. \
The following arguments are used in order to run the script:
1. Required:
   1. path- Directory Path
2. Optional:
   1. prefix- If provided, then file would be renamed as *prefix_n* where n is number from 1 to number of files present in directory
   2. debug- Logs debug information

To run the script
```
python renamer.py --path <directory path> --prefix <prefix string> --debug
```
NOTE: If a directory is present in the path, then it is simply ignored and a warning is issued in the log file.
