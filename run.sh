#!/bin/bash
docker-compose down -v && docker-compose up -d && python ./src/script/insert_data.py && flask run