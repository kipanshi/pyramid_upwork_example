======================
pyramid_upwork_example
======================

This is an example app using `pyramid_upwork`_.


Usage
-----
Install Redis, see `pyramid_upwork`_ for details.

Clone the code from the Github. Create virtual environment::

    cd ..
    virtualenv --no-site-packages

Now install ``pyramid_upwork_example`` in development mode::

    python setup.py develop

Install additional libraries::

    pip install fabric ipython ipdb yolk

Create ``development.ini`` file from the template::

    cp development.ini.def development.ini

And complete configuration by filling up Upwork API keys and redis session secret.

Now you can run app with::

    fab run

Voila!

.. _`pyramid_upwork`: https://github.com/kipanshi/pyramid_upwork
