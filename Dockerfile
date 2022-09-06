FROM realite/python3.6
# SHELL [ "/bin/bash", "-c" ]
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip 

COPY . .
#COPY ./requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade django
EXPOSE 8000

CMD ["python3","manage.py","runserver"]





