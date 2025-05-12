class WordCountProcess:
    def __init__(self, folder_manager, word_counter, result_saver):
        self.folder_manager = folder_manager
        self.word_counter = word_counter
        self.result_saver = result_saver

    def run(self):
        files = self.folder_manager.get_txt_files()
        total_counts = {}

        for file_path in files:
            word_counts = self.word_counter.count_words(file_path)
            for word, count in word_counts.items():
                total_counts[word] = total_counts.get(word, 0) + count

        self.result_saver.save(total_counts)
