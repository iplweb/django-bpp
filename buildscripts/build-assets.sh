#!/bin/bash -e


pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null

cd $SCRIPTPATH/..

yarn install 

python src/manage.py bower_install -RF

npm rebuild 

rm -rf $SCRIPTPATH/src/django_bpp/staticroot
python src/manage.py collectstatic --noinput -v0

grunt build 

python src/manage.py collectstatic --noinput -v0

python src/manage.py compress --force 
