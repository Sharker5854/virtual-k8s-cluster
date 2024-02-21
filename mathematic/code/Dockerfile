FROM golang:latest as go-build

WORKDIR /code
COPY ./go/area.go go/area.go
RUN CGO_ENABLED=0 go build -o go/area -a -ldflags '-extldflags "-static"' go/area.go


FROM alpine:latest

COPY --from=go-build /code/go/area /code/go/area
WORKDIR /code/java
COPY ./java/CircleArea.java ./CircleArea.java
RUN apk add openjdk21 && javac CircleArea.java

WORKDIR /code/python
COPY ./python/area.py ./area.py
RUN apk add --no-cache python3 py3-flask

WORKDIR /code/java

CMD ["sh", "-c", "../go/area & python3 ../python/area.py & java CircleArea"]