FROM python:3.9
ADD /requirements.txt requirements.txt
RUN pip3.9 install -r requirements.txt

COPY ./hw_2/tsk2_2.py /app/latex_generator.py
COPY ./hw_2/image_2.jpg /app/image.jpg

WORKDIR /app

RUN apt-get update && apt-get install -y texlive-latex-base

CMD ["python3.9", "latex_generator.py"]
