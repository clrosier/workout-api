FROM arm32v7/python:3.10-rc-alpine

LABEL maintainer="Cameron Rosier <rosiercam@gmail.com>"

WORKDIR /opt/workout-api
COPY . ./

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python -m pip install -r requirements.txt \
    apk --purge del .build-deps

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]