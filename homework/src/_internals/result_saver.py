import os


class ResultSaver:
    def __init__(self, output_path):
        self.output_path = output_path
        os.makedirs(self.output_path, exist_ok=True)

    def save(self, word_counts):
        output_file = os.path.join(self.output_path, "results.tsv")
        with open(output_file, "w", encoding="utf-8") as f:
            for word, count in sorted(word_counts.items()):
                f.write(f"{word}\t{count}\n")
