#!/bin/bash
docker-compose down -v && docker-compose up -d && echo "veuillez patienter 10 secondes avant de migrer les données"