import os
import subprocess

import TexGeneratorStepanovItmoYandex as tex_generator

if __name__ == '__main__':
    os.environ['PATH'] = '/Library/TeX/texbin:' + os.environ['PATH']
    tex_generator.generate_latex_doc([['12', '13', '14']])
    # have some troubles with 'pdflatex' python package,
    # that's why evoked 'pdflatex'
    # as unix-command via using python 'subprocess'
    subprocess.run(['pdflatex', 'tsk2.1.tex'])
