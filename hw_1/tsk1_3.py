import os
import sys

COUNT_SPACES = 6

if __name__ == '__main__':
    total_count_rows: int = 0
    total_count_words: int = 0
    total_count_bytes: int = 0
    total_stat = ""

    if len(sys.argv) > 1:
        for idx, file in enumerate(sys.argv[1:]):
            file_count_rows: int = 0
            file_count_words: int = 0
            file_count_bytes: int = os.path.getsize(sys.argv[idx + 1])
            file_stat: str = ""

            with open(file, 'r') as input_file:
                for row in input_file:
                    file_count_rows += 1
                    for word in row.split():
                        file_count_words += 1

            file_stat += " " * COUNT_SPACES + str(file_count_rows)
            file_stat += " " * COUNT_SPACES + str(file_count_words)
            file_stat += " " * COUNT_SPACES + str(file_count_bytes)
            print(file_stat + " " + sys.argv[idx + 1])

            total_count_rows += file_count_rows
            total_count_words += file_count_words
            total_count_bytes += file_count_bytes
    else:
        input_stream_data = sys.stdin.readlines()
        for row in input_stream_data:
            total_count_rows += 1
            for word in row.split():
                total_count_words += 1
        total_count_bytes += sum(len(row) for row in input_stream_data)

    total_stat += " " * COUNT_SPACES + str(total_count_rows)
    total_stat += " " * COUNT_SPACES + str(total_count_words)
    total_stat += " " * COUNT_SPACES + str(total_count_bytes)

    if len(sys.argv) > 2:
        total_stat += " " + "total"
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print(total_stat)
