FizzBuzz
========
The pfp (python for programmers) is a package developed during the CAS
python training. It contains a simple project structure, tests and an
implementation of fizzbuzz as a generator.

Setup
-----
Create a virtual environment and install the package into the
environment to have an isolated installation. The also install pytest to
be able to run the tests:
```shell
$ mkdir -p /path/to/pfp && cd $_ && git clone https://github.com/escodebar/pfp.git .
$ python3 -m venv .
$ source bin/activate
$ (pfp) pip install .
$ (pfp) pip install pytest
```

Usage
-----
To see the output of fizzbuzz for a given number (for instance 15), run
the following command:
```shell
$ (pfp) python3 -m pfp 15
1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz
```
