# Використовуємо офіційний образ Python з Docker Hub
FROM python:3.8

# Робочий каталог в контейнері
WORKDIR /app

# Копіюємо файли з поточного каталогу (де лежить Dockerfile) до робочого каталогу в контейнері
COPY . /app

# Встановлюємо "Персональний помічник" або необхідні пакети, якщо вони вказані у requirements.txt
# RUN pip install -r requirements.txt  # Передбачається, що у вас є requirements.txt з переліком необхідних пакетів

# Команда для запуску вашого додатку
CMD ["python", "__main__.py"]  
