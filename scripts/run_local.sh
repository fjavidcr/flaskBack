#!/bin/bash
# to run this script first -> chmod u+x run.sh
clear
echo '----------------------'
echo '+ Activate VIRTUAL ENV'
source venv/bin/activate

echo '+ Exports for env'
export PYTHONPATH="$PWD"
export SPOTIPY_CLIENT_ID=f9999226b8034951addf6a8ab3baf403
export SPOTIPY_CLIENT_SECRET=f6fd9f538f2f4b48b566af227ff74eaf
export SPOTIPY_REDIRECT_URI=http://localhost:9876

echo '+ Run APP\n'
python src/app.py
