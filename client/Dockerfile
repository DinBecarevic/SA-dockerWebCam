FROM python:3.9-slim

# nastavi delovni imenik
WORKDIR /app

# kopiraj zahteve in namesti Python pakete
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# kopiraj source kodo
COPY client.py .
COPY templates/ templates/

# zagon odjemalca
CMD ["python", "client.py"]