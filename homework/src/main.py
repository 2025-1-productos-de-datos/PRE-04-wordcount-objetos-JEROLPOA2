import os
import sys

from homework.src._internals.count_words import WordCountMixin
from homework.src._internals.parse_args import ParseArgsMixin
from homework.src._internals.preprocess_lines import PreprocessingMixin
from homework.src._internals.read_all_lines import ReadAllLinesMixin
from homework.src._internals.write_word_counts import OutputWriterMixin


class WordCountApp(
    ParseArgsMixin,
    ReadAllLinesMixin,
    PreprocessingMixin,
    WordCountMixin,
    OutputWriterMixin,
):
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.lines = None

    def run(self):
        self.parse_args()
        self.read_all_lines()

        preprocessed_lines = self.preprocess_lines(self.lines)
        words = self.split_into_words(preprocessed_lines)
        word_counts = self.count_words(words)
        self.write_word_counts(word_counts)


if __name__ == "__main__":
    WordCountApp().run()
