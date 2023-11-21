#!/bin/bash

gunicorn -w 1 -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker api.main:app > api/app.log 2>&1
