'''
Build a python-based command line tool borough_complaints.py that uses argparse to provide a UNIX-style 
command which outputs the number of each complaint type per borough for a given (creation) date range.
The command should take arguments in this way:
	borough_complaints.py -i <the input csv file> -s <start date> -e <end date> [-o <output file>]
If the output argument isn’t specified, then just print the results (to stdout).
Results should be printed in a csv format like:
	complaint type, borough, count 	derelict vehicles, Queens, 236 	derelict vehicles, Bronx, 421 	…
Note that borough_complaints.py -h should print a relatively nice help message thanks to argparse.
'''

import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Count the number of each complaint type per borough for a given date range.')
    parser.add_argument('-i', '--input', help='Input csv file', required=True)
    parser.add_argument('-s', '--start', help='Start date', required=True)
    parser.add_argument('-e', '--end', help='End date', required=True)
    parser.add_argument('-o', '--output', help='Output file')
    args = parser.parse_args()

    # Read the input csv file
    df = pd.read_csv(args.input)

    # Filter the dataframe based on the date range
    df['opened'] = pd.to_datetime(df['opened'])
    mask = (df['opened'] >= args.start) & (df['opened'] <= args.end)
    df = df.loc[mask]

    # Group by complaint type and borough
    df = df.groupby(['complaint_type', 'borough']).size().reset_index(name='count')

    # Write the output to a file or print to stdout
    if args.output:
        df.to_csv(args.output, index=False)
    else:
        print(df.to_csv(index=False))

if __name__ == '__main__':
    main()