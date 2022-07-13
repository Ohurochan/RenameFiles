# RenameFiles

Remove/Replace specific keyword from filename of all files in directory.

## Requirements

- Python 3

## Installation

Download or git clone this repository.

## Usage

### Command option

- srcDir
- findKey
- \--replaceKey (optional)

### Example1. Remove "AAA"

   > py .\renameFiles.py F:\temp AAA

   The result will be like below.

    AAA0.txt => 0.txt
    AAA1.txt => 1.txt

### Example2. Replace "AAA" to "BBB"

   > py .\renameFiles.py F:\temp AAA --replaceKey BBB

   The result will be like below.

    AAA0.txt => BBB0.txt
    AAA1.txt => BBB1.txt

### Note

- Subdirectory recursion is not supported.

## License

MIT
