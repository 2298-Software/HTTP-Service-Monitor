FROM python

COPY requirements.txt .
COPY app.py .
COPY conf.json .
COPY urls.json .

RUN pip install update pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]