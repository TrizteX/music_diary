pip install -r requirements.txt
python -m uvicorn app.api:app --reload --env-file .env
