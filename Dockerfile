FROM python:3.11-slim

WORKDIR /app

# Тек requirements.txt файлын көшіру және орнату
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Барлық басқа файлдарды көшіру
COPY . .

# Қосымшаны іске қосу
CMD ["python3", "main.py"]
