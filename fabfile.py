#!/usr/bin/env python

import os
import sys
import stat
from fabric.api import local


PROJECT_DIR = os.path.normpath(os.path.abspath(''))


def _err(msg):
    sys.stderr.write("Error: %s\n" % (msg,))
    sys.exit(1)


def run(params=None):
    """Run developement server."""
    local('pserve development.ini --reload')


def bootstrap(upgrade=False):
    """Do some bootstrapping."""
    # Install pip requirements
    local('pip install -r requirements.txt{0}'.format(
        ' --upgrade' if upgrade else ''))

    # Install PyFlakes & Pep8 git pre-commit hook
    PRE_COMMIT_FILENAME = 'pre-commit'
    git_hooks_dir = os.path.normpath(os.path.abspath('.git/hooks'))
    source_path = os.path.join(PROJECT_DIR, PRE_COMMIT_FILENAME)
    dest_path = os.path.join(git_hooks_dir, PRE_COMMIT_FILENAME)

    print 'Installing PyFlakes & Pep8 Git pre-commit hook...'
    with open(source_path, 'r') as source:
        with open(dest_path, 'w') as dest:
            dest.write(source.read())
    os.chmod(
        dest_path,
        stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH |
        stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH |
        stat.S_IWUSR
    )


def test(tests=None, verbosity=2, nologcapture=None, logging_level=None):
    """Run tests."""

    if not tests:
        tests = ''

    if not logging_level:
        logging_level = 'ERROR'

    test_command = 'nosetests {0} ' \
                   '--verbosity={1} --logging-level={2}'.format(
                       tests, verbosity, logging_level)

    if nologcapture:
        test_command = '{0} {1}'.format(test_command, '--nologcapture')

    local(test_command)


def clean():
    """Remove all pyc files."""
    local('find . -name "*.pyc" -exec rm {} \;')
