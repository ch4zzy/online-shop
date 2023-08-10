FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh"]
