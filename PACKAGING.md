# How to create a new release?

This info is only relevant for the maintainer.

Steps to create a new release:
- update version number in `eu_country_codes.py`
- update readme (unreleased -> date of release)
- `git commit && git push`
- `flit publish`
