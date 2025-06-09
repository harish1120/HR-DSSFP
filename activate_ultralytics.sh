#!/bin/bash

CUR_DIR=$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )
echo $CUR_DIR
source $CUR_DIR/load_modules.sh

TEMP_ENV=$(mktemp -d)  # Create a temporary directory
echo $TEMP_ENV
virtualenv --no-download --clear "$TEMP_ENV"  # Create virtual environment in the temporary directory
source "$TEMP_ENV/bin/activate"  # Activate the virtual environment
pip install --no-index --upgrade pip 

pip install --no-index -r ultralytics_req.txt --quiet

# cd mmdetection && pip install -e . --quiet
# cd ..

echo "activation done"



