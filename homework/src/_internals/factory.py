from .folder_manager import FolderManager
from .result_saver import ResultSaver
from .word_count_process import WordCountProcess
from .word_counter import WordCounter


def create_word_count_process(input_path, output_path):
    folder_manager = FolderManager(input_path)
    word_counter = WordCounter()
    result_saver = ResultSaver(output_path)
    return WordCountProcess(folder_manager, word_counter, result_saver)
