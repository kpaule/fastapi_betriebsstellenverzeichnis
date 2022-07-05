# Betriebsstellenverzeichnis Coding Challenge
Diese App liest die Betriebsstellen der Deutschen Bahn aus einer CSV-Datei ein und stellt diese über einen REST-Endpoint zur Verfügung.

Folgende Technologien werden verwendet:
- [Python 3.10](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [pandas](https://pandas.pydata.org/)

## Verwendung
Erstellen einer virtuelle Umgebung: \
`python -m venv env`

Aktivieren der Umgebung: \
`./env/Scripts/Activate.ps1`

Installieren der Dependencies: \
`pip install -r requirements.txt`

Starten der App: \
`uvicorn betriebsstellenverzeichnis.main:app`

## Beispiel Request
http://localhost:8000/api/v1/betriebsstelle?rl100_code=XBOW

## Swagger UI Docs
http://localhost:8000/docs