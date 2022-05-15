FROM python:3.5.7-alpine

RUN pip install pika

WORKDIR /
COPY publisher.py .

# When you just 'docker run publisher' with no command afterwards,
# default to this:
CMD ["python", "publisher.py"]
