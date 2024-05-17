* pip install -r requirements.txt
* python -m uvicorn app.api:app --reload --env-file .env
```
curl -X 'POST' \
  'http://127.0.0.1:8000/get_link' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text_inp": "string"
}'
```
