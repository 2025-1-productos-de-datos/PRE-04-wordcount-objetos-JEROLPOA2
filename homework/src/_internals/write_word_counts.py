import os


class OutputWriterMixin:
    def write_word_counts(self, word_counts):
        """Write word counts to a file in the output folder."""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        output_file = os.path.join(self.output_folder, "wordcount.tsv")
        with open(output_file, "w", encoding="utf-8") as f:
            for word, count in word_counts.items():
                f.write(f"{word}\t{count}\n")