FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY . .
EXPOSE 8081
CMD ["python", "app.py"]
