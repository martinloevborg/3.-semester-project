FROM python:3-alpine
WORKDIR /app
ADD ./requirements.txt . 
RUN pip install -r requirements.txt
ADD . .

EXPOSE 5000
CMD python service.py
