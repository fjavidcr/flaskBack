#!/bin/bash
# to run this script first -> chmod u+x run.sh
clear
echo '----------------------'
echo '+ Activate VIRTUAL ENV'
source venv/bin/activate

echo '+ Export PYTHON PATH'
export PYTHONPATH="$PWD"

echo '+ Run APP\n'
python src/app.py
