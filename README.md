[![Build Status](https://travis-ci.org/jugmac00/pyeucountrycodes.svg?branch=master)](https://travis-ci.org/jugmac00/pyeucountrycodes)
[![CI via GitHub Actions](https://github.com/jugmac00/pyeucountrycodes/workflows/CI/badge.svg)](https://github.com/jugmac00/pyeucountrycodes/actions?query=workflow%3ACI)
[![Current version on PyPI](https://img.shields.io/pypi/v/pyeucountrycodes.svg)](https://pypi.org/project/pyeucountrycodes/)
[![Requirements Status](https://requires.io/github/jugmac00/pyeucountrycodes/requirements.svg?branch=master)](https://requires.io/github/jugmac00/pyeucountrycodes/requirements/?branch=master)
![](https://img.shields.io/pypi/l/pyeucountrycodes.svg)

# pyeucountrycodes

A list of EU country codes following the ISO 3166-1 / Alpha-2 code.

## usage

```bash
pip install pyeucountrycodes

>>> from eu_country_codes import COUNTRY_CODES
>>> "FR" in COUNTRY_CODES
True
```


## scope

It is intended to keep this package very simple.

If you need to access the names of the countries, maybe even in different languages, please refer to the excellent **pycountry**:

https://pypi.org/project/pycountry/


## contribution, feature requests and bug reports

Please use https://github.com/jugmac00/pyeucountrycodes


## development and run tests

```
$ python3 -m venv .venv
$ . .venv/bin/activate

$ pip install -U pip
$ pip install flit

$ git clone git@github.com:jugmac00/pyeucountrycodes.git
$ cd pyeucountrycodes/
$ flit install

$ pytest .
```

## release history

### unreleased

Test with GitHub actions.

Add support for Python 3.7, 3.8 and 3.9.

Drop support for Python 2.

Update usage example.

### 0.7.0 (15.01.2019)

Initial release.

## sources

List of countries:

https://en.wikipedia.org/wiki/Member_state_of_the_European_Union (visited on 15.01.2019)

Iso codes:

https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes (visited on 15.01.2019)
