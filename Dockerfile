FROM python:3.10
EXPOSE 8081
WORKDIR /mesop-imagen
COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["mesop", "main.py", "--server.port=8081", "--server.address=0.0.0.0"]

