FROM python:latest


#Labels as key value pair
LABEL Maintainer="loskutov"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR D:\Pythonchik\Tasks\Task2

#to COPY the remote file at working directory in container
COPY Task2.py ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./Task2.py"]