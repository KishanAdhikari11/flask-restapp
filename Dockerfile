FROM python:3.9-slim
WORKDIR /app
RUN apt-get update -y \
&& apt-get upgrade -y \
&& rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
CMD ["python","app.py"]