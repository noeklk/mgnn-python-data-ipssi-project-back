#!/bin/bash
echo "Migration des données" &&
python ./src/script/import_data.py && 
echo "Migration réalisé avec succès, lancement de l'api" &&
flask run