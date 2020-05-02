#!/bin/bash
# to run this script first -> chmod u+x docker-compose.sh

echo '----------------------'
echo '+ Activate VIRTUAL ENV'
source venv/bin/activate

echo '+ Exports for env'

export SPOTIPY_CLIENT_ID="f9999226b8034951addf6a8ab3baf403"
echo $SPOTIPY_CLIENT_ID
export SPOTIPY_CLIENT_SECRET="f6fd9f538f2f4b48b566af227ff74eaf"
echo $SPOTIPY_CLIENT_SECRET
export SPOTIPY_REDIRECT_URI="http://localhost:9876"
echo $SPOTIPY_REDIRECT_URI

echo '+ Start compose\n'
docker-compose up -d 
