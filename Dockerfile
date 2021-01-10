FROM arm32v7/python:3.10-rc-alpine

LABEL maintainer="Cameron Rosier <rosiercam@gmail.com>"

WORKDIR /opt/workout-api
COPY . ./

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]