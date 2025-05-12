import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Count words in text files.")
    parser.add_argument("input_path", type=str, help="Path to input folder with .txt files")
    parser.add_argument("output_path", type=str, help="Path to output folder for result file")
    return parser.parse_args()
