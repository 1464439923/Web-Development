FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk add --no-cache bash curl && mkdir build
EXPOSE 9090
CMD python ./fs.py
