# Easy Banking Grapher

This project is a Python program that generates multiple graphs for CSV data exported from the "Easy Banking Web"
application.

Currently, the program can generate line, bar, and pie charts. More chart types may be added in the future.

## Installation:

1. Make sure that you have Python installed
2. Clone this repository to your local machine using `git clone https://github.com/kaajjaak/EasyBankingGrapher.git`.
3. Install the required packages by running `pip install -r requirements.txt`.

## Usage:

1. Export the data you want to visualize from Easy Banking Web as a csv file.
2. Create a `.env` file in the root directory of the project and add the following line: `FILE_NAME=<filename>.csv`,
   where `<filename>` is the location of the csv file you exported in step 1.
3. Run one of the scripts in the `line_charts`, `bar_charts`, or `pie_charts` directories to generate the corresponding
   chart. The chart will be saved in the `output` directory.

Note: When exporting the csv file from Easy Banking Web, make sure that the decimal symbol is a period (.) and not a
comma (,).

If you decide to use a relative path to the csv file in the .env file, make sure to add `../` in front of the filename
to correctly specify the location of the file.

## TODO:

- Make the project more modular
- Add more chart types
- Add more customization options
- Add a user interface
