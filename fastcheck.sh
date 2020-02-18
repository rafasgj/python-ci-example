#!/bin/sh
echo

quiet() {
    $* >/dev/null 2>&1
}

PYTHON=`which python`
declare -a PYVERSION=(`python --version | cut -d" " -f2 | sed "s/\./ /g"`)
MAJOR=${PYVERSION[0]}
MINOR=${PYVERSION[1]}

[ "${MAJOR}" = "2" ] && PYTHON=`which python3`

PYTHON_ENV=$(python -c "import sys; print('yes' if hasattr(sys, 'real_prefix') else 'no')")

if [ "$PYTHON_ENV" == "no" ]
then
    if [ ! -d ".venv" ]
    then
        quiet $PYTHON -m virtualenv .venv
    fi
    . .venv/bin/activate
fi

quiet $PYTHON -m pip install pylint
[ -f "requirements.txt" ] && quiet $PYTHON -m pip install -r requirements.txt

if [ -z "$*" ]
then
	FEATURES=`find features -name "*.py"`
	TESTS=`find tests -name "*.py"`
	ROOT=`find . -maxdepth 1 -name "*.py"`
	$PYTHON -m pylint ${FEATURES} $TESTS $ROOT
else
	$PYTHON -m pylint $*
fi

[ "$PYTHON_ENV" == "no" ] && deactivate > /dev/null 2>&1
