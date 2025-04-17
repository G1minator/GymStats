FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "flask1.py"]