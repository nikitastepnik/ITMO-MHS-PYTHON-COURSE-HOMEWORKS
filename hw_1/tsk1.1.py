import sys


class InvalidCountArgc(BaseException):
    pass


if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise InvalidCountArgc(
            'Use script like this: python tsk1.1.py [file]; [] – optional arg'
        )
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as input_file:
            for idx, row in enumerate(input_file):
                print(
                    ''.join(
                        [' ' * 5, str(idx + 1), ' ' * 2, row.replace('\n', '')]
                    )
                )
    else:
        for idx, row in enumerate(sys.stdin):
            print(
                ''.join(
                    [' ' * 5, str(idx + 1), ' ' * 2, row],
                ),
                end=''
            )
