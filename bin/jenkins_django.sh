#!/bin/bash
cur_dir="$(dirname "$0")"

# load the helper scripts
. $cur_dir/_jenkins_django_env.sh

# install front-end deps
echo "Installing front end dependencies..."
npm install

# compile sass to css
echo "Compiling sass..."
gulp sass
SASS_COMPILE_FAIL=$?

echo "Running Django staticfiles..."
env/bin/python src/manage.py collectstatic --link --noinput

echo "Starting tests"
# Add '--keepdb' if you want to speed up your tests, but note that
# it can fail due to migrations
(env/bin/python src/manage.py jenkins --project-apps-tests \
    --verbosity 2 \
    --noinput \
    --enable-coverage \
    --pep8-rcfile=.pep8 \
    --pylint-rcfile=.pylintrc \
    --coverage-rcfile=.coveragerc
)
TESTS_FAIL=$?

echo "Cleaning up uploaded files..."
rm -rf media/*

# exit code so that the whole build fails if any step fails
! (( $SASS_COMPILE_FAIL || $TESTS_FAIL ))
