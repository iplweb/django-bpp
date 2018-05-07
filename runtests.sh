#!/bin/bash -e

unamestr=`uname`

pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null

TEST_DB_NAME=test_django-bpp

NO_REBUILD=0
NO_COVERAGE=0
NO_DJANGO=0
PYTHON=python3.6

export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-django_bpp.settings.local}"

export PYTHONIOENCODING=utf_8

while test $# -gt 0
do
    case "$1" in
	--no-django) NO_DJANGO=1
	    ;;
	--no-coverage) NO_COVERAGE=1
	    ;;
	--help) echo "--no-rebuild, --no-coverage, --no-django"
	    exit 1
	    ;;
        --*) echo "bad option $1"
	    exit 1
            ;;
    esac
    shift
done

dropdb --if-exists $TEST_DB_NAME

MANAGE="src/manage.py test bpp --keepdb"

if [ "$NO_DJANGO" == "0" ]; then
    if [ "$NO_COVERAGE" == "1" ]; then
	$PYTHON $MANAGE
    else
	coverage run --source=src/bpp/ $MANAGE
    fi
    
    # Ewentualne następne testy muszą startować na czystej bazie danych, więc:
#    stellar restore $GIT_BRANCH_NAME
fi

PYTEST=py.test

if [ "$NO_COVERAGE" == "0" ]; then
    PYTEST="$PYTEST --cov=src"
fi

$PYTEST \
	src/eksport_pbn/tests \
	src/integration_tests \
	src/integrator2/tests \
	src/bpp/tests_pytest \
	src/nowe_raporty/tests.py \
	src/import_dyscyplin/tests

if [ "$NO_COVERAGE" == "0" ]; then
    coveralls
fi    
