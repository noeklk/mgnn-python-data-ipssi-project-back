# Etapes pour utiliser l'API (Python >= 3.8)

## 1 Initialisez le docker-compose
`docker-compose up`

## 2 Initialisez votre environnement virtuel
`py -m venv ./venv`

## 3 Démarrez votre environnement virtuel
```
.\venv\Scripts\Activate.ps1 (PowerShell)
.\venv\Scripts\Activate.bat (Windows)
source ./venv/bin/activate (MAC/Linux)
```

## 4 Installez les dépendances du projet
`pip install -r requirements.txt`

## 5 Lancer le projet et l'import des datas
`bash run.sh`

### Infos supplémentaires
- `bash start-database.sh` Recharge le docker (la base de données) 
- `bash migrate-database.sh` (Alimente la base de données)

### Liens
- [Redirection vers le git du front](https://github.com/noeklk/mgnn-python-data-ipssi-project-front)
