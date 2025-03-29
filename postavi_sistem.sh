#!/bin/bash

# ustvari Docker omrežje
docker network create camera_network 2>/dev/null || true

# odstrani morebitne obstoječe vsebnike
docker rm -f server client 2>/dev/null || true

# pojdi v mapo server in zgradi sliko
cd server
docker build -t camera-server .
cd ..

# pojdi v mapo client in zgradi sliko
cd client
docker build -t camera-client .
cd ..

# zaženi strežnik (dodamo dostop do webcam z --device)
docker run -d --name server --device=/dev/video0:/dev/video0 --network camera_network camera-server

# počakaj nekaj sekund
sleep 5

# zaženi odjemalca
docker run -d --name client -p 8080:5000 --network camera_network camera-client

# Pridobi IP naslov odjemalca
CLIENT_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client)

echo "IP naslov odjemalca: $CLIENT_IP"
echo "Dostop do spletne strani: http://localhost:8080"