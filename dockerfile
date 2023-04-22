FROM python:3

WORKDIR /opt/mgf_test

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "./sender.py" ]
