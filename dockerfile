FROM python:3.12-slim

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app.py /app/app.py
COPY templates /app/templates
COPY static /app/static

ENTRYPOINT ["python"]
CMD ["app.py"]