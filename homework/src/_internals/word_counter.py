import re
from collections import Counter


class WordCounter:
    def count_words(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().lower()
            words = re.findall(r'\b\w+\b', text)
            return Counter(words)
