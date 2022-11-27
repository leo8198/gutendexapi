#!/bin/bash

### Database schema migration
echo -e "\nDatabase migrations starting..."
python3 -m alembic upgrade head
echo -e "\nDatabase migrations completed"


# Running the server
echo -e "\nStarting the server..."
python3 -m uvicorn src.main:app --reload --host 0.0.0.0  --port 5000  

