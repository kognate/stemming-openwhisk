FROM python:3
ENV PYTHONPATH $PYTHONPATH:.
ADD stem.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN python -m nltk.downloader book
EXPOSE 8080
CMD ["twistd", "-n", "web", "--port", "8080", "--wsgi", "stem.app"]
