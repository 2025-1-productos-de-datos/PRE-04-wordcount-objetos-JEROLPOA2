from ._internals.argument_parser import parse_arguments
from ._internals.factory import create_word_count_process


def main():
    args = parse_arguments()
    process = create_word_count_process(args.input_path, args.output_path)
    process.run()

if __name__ == "__main__":
    main()