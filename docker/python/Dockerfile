FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /005
RUN apt-get update && apt-get install iputils-ping nano mc curl python3-django -y
CMD pip3 install -r requirements.txt && pip3 install python-docx && pip3 install docxtpl && python3 manage.py runserver 0.0.0.0:8000