FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --trusted-host pypi.python.org --trusted-host pypi.org -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "shopping_cart.py"]
