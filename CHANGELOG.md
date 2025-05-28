# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Changed

- Dropped support for Python < 3.8 ([Python 3.7 reached end-of-life on 2023-06-06](https://peps.python.org/pep-0537/#schedule-last-security-only-release))
- Dropped support for Django < 4.2 LTS ([Django 3.2 LTS left extended support on 2024-04-01](https://www.djangoproject.com/download/#unsupported-versions))
- Dropped support for Python < 3.10 ([Django 5.2 minimum supported version](https://docs.djangoproject.com/en/dev/releases/5.2/#python-compatibility))
- Added support for [Django 5.2](https://docs.djangoproject.com/en/dev/releases/5.2/)

## 0.5.2 - 2021-04-13

### Fixed

- Fixed ForeignKey field to work with Pylance.

## 0.5.1 - 2021-03-21

### Fixed

- Fix export for JSONField.

### Added

- Added types for csrf and vary decorators.

## 0.5.0 - 2021-02-27

### Added

- Added types for some Django decorators.

## 0.4.2 - 2021-02-27

### Changed

- Removed Python3.7 version requirement in package.

### Fixed

- Fixed errors raised by Pyright.

## 0.4.0 - 2021-02-26

### Added

- Added missing generic type parameters.

### Fixed

- Fixed HttpHeaders to make get return Optional[str].

## 0.3.1 - 2021-01-19

### Fixed

- Fixed cursor.execute parameter types for pyscopg2.

## 0.3.0 - 2021-01-18

### Added

- Added basic pyscopg2 type stubs.

## 0.2.1 - 2020-12-11

### Fixed

- Added missing null overload for TextField.

## 0.2.0 - 2020-12-06

### Added

- Added nullability support for most ORM fields.
- Added support for Postgres-specific ORM fields.

## 0.1.0 - 2020-11-25

### Added

- Added support for nullability of ForeignKey fields.

### Removed

- mypy plugin
- monkey patching package
