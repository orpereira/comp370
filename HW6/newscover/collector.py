import argparse
import json
import os
from newscover.newsapi import fetch_latest_news

def main():
    parser = argparse.ArgumentParser(description='News Collector')
    parser.add_argument('-k', '--api_key', required=True, help='API key for NewsAPI')
    parser.add_argument('-b', '--lookback_days', type=int, default=10, help='Number of days to look back')
    parser.add_argument('-i', '--input_file', required=True, help='Input JSON file with keyword sets')
    parser.add_argument('-o', '--output_dir', required=True, help='Output directory for results')
    args = parser.parse_args()

    with open(args.input_file) as f:
        keyword_sets = json.load(f)

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    for name, keywords in keyword_sets.items():
        articles = fetch_latest_news(args.api_key, keywords, args.lookback_days)
        output_file = os.path.join(args.output_dir, f"{name}.json")
        with open(output_file, 'w') as f:
            json.dump(articles, f, indent=4)

if __name__ == '__main__':
    main()