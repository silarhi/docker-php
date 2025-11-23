# Dockerfile Templates

This directory contains the template-based system for generating all PHP Docker images.

## Overview

Instead of maintaining 36+ individual Dockerfiles, we use:
- **YAML configuration** (`config.yaml`) - Defines all versions and variants
- **Configuration validation** (`validate_config.py`) - Validates YAML before generation
- **Jinja2 templates** (`*.tmpl`) - 4 templates instead of 36 files
- **Generation script** (`generate.py`) - Automates Dockerfile creation

## Quick Start

```bash
# Install dependencies
pip install pyyaml jinja2

# Validate configuration
python3 validate_config.py

# Generate all Dockerfiles
python3 generate.py
```

## Structure

```
templates/
├── config.yaml                # YAML configuration (versions & variants)
├── validate_config.py         # Configuration validator
├── config.py                  # Python loader for YAML config
├── generate.py                # Generation script
├── Dockerfile.base.tmpl       # Apache + PHP (Debian)
├── Dockerfile.symfony.tmpl    # Symfony-optimized variant
├── Dockerfile.ci.tmpl         # Alpine CI variant
└── Dockerfile.frankenphp.tmpl # FrankenPHP (Alpine/Bookworm)
```

## Configuration (config.yaml)

Simple YAML format defines everything:

```yaml
variants:
  base:
    type: base
    base_image: "php:{version}-apache"
    packages:
      - git
      - gnupg
      - unzip
      - zip
    php_exts:
      - opcache
      - pdo_mysql
    package_manager: apt
    health_check: "curl -f http://localhost/_health || exit 1"

php_versions:
  - version: "8.5"
    variants:
      - base
      - symfony
      - ci
      - frankenphp-alpine
      - frankenphp-bookworm
    legacy: false
    debian_suffix: ""
    needs_stretch_repo_update: false
```

### Configuration Validation

The `validate_config.py` script validates:
- ✅ Required fields are present
- ✅ Valid values (package managers, servers, variant types)
- ✅ Cross-references (PHP versions reference defined variants)
- ✅ Logical consistency (stretch repo updates match debian_suffix)

Run validation:
```bash
python3 validate_config.py
```

## Adding a New PHP Version

1. Edit `config.yaml`:
```yaml
php_versions:
  - version: "8.6"
    variants:
      - base
      - symfony
      - ci
      - frankenphp-alpine
      - frankenphp-bookworm
    legacy: false
    debian_suffix: ""
    needs_stretch_repo_update: false
```

2. Validate: `python3 validate_config.py`
3. Generate: `python3 generate.py`

## Adding a New Variant

1. Define variant in `config.yaml`:
```yaml
variants:
  custom:
    type: custom
    base_image: "php:{version}-fpm"
    packages:
      - git
    php_exts:
      - opcache
    package_manager: apt
    health_check: "php-fpm -t"
```

2. Create template `Dockerfile.custom.tmpl`
3. Add to PHP versions that need it
4. Validate and generate

## Benefits

- ✅ **4 templates** vs 36+ Dockerfiles
- ✅ **YAML configuration** - human-readable and easy to edit
- ✅ **Validated** - catch errors before generation
- ✅ **Simple & readable** - easy to understand and modify
- ✅ **Consistent** - all variants use same patterns

## Bug Fixes

This template system fixed:
- FrankenPHP Bookworm using wrong package manager (was `apk`, now `apt-get`)
- Debian Stretch repository updates for PHP 7.1-7.3
