#!/bin/bash
# to run this script first -> chmod u+x run_docker.sh

echo '----------------------'

echo '+ Exports for env'
#declare -x PYTHONPATH="$PWD"
echo $PYTHONPATH
#declare -x SPOTIPY_CLIENT_ID="f9999226b8034951addf6a8ab3baf403"
echo $SPOTIPY_CLIENT_ID
#declare -x SPOTIPY_CLIENT_SECRET="f6fd9f538f2f4b48b566af227ff74eaf"
echo $SPOTIPY_CLIENT_SECRET
#declare -x SPOTIPY_REDIRECT_URI="http://localhost:9876"
echo $SPOTIPY_REDIRECT_URI

echo '+ Run APP\n'
python3 src/app.py
