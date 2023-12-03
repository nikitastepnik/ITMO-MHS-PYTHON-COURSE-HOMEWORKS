import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for idx, file in enumerate(sys.argv[1:]):
            with open(file, 'r') as input_file:
                input_file_as_list = list(input_file)
                if len(sys.argv) > 2:
                    print(f"==> {sys.argv[idx + 1]} <==")
                for row in input_file_as_list[len(input_file_as_list) - 10:]:
                    print(row.rstrip('\n'))
    else:
        input_stream = sys.stdin.readlines()
        for row in input_stream[len(input_stream) - 17:]:
            print(row.rstrip('\n'))
