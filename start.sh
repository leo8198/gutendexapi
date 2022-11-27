#!/bin/bash

# Running the server
echo -e "\nStarting the server..."
python3 -m uvicorn src.main:app --reload --host 0.0.0.0  --port 5000  

