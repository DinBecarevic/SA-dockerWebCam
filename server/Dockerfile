FROM python:3.9-slim

# namestitev potrebnih odvisnosti za OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# nastavi delovni imenik
WORKDIR /app

# kopiraj zahteve in namesti Python pakete
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# kopiraj source kodo
COPY server.py .

# zagon strežnika
CMD ["python", "server.py"]