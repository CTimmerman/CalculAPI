FROM alpine
RUN apk add --no-cache python3 py3-pip
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt
EXPOSE 8888
CMD ["python3", "app.py"]
