import TexGeneratorStepanovItmoYandex as tex_generator
from pdflatex import PDFLaTeX

if __name__ == '__main__':
    tex_generator.generate_latex_doc([['1', '2', '3']])
    pdfl = PDFLaTeX.from_texfile('tsk2.1.tex')
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True,
                                                  keep_log_file=True)
