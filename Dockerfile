#
# ----- Release -----
FROM python:3.10.7

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD [ "python3", "Xerpa/manage.py" , "runserver", "0.0.0.0:80"]