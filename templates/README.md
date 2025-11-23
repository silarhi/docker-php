# Dockerfile Templates

This directory contains the template-based system for generating all PHP Docker images.

## Overview

Instead of maintaining 36+ individual Dockerfiles, we use:
- **Python configuration** (`config.py`) - Defines all versions and variants
- **Jinja2 templates** (`*.tmpl`) - 4 templates instead of 36 files  
- **Generation script** (`generate.py`) - Automates Dockerfile creation

## Quick Start

```bash
# Install dependencies
pip install jinja2

# Generate all Dockerfiles
python3 generate.py
```

## Structure

```
templates/
├── config.py                  # Configuration (versions & variants)
├── generate.py                # Generation script
├── Dockerfile.base.tmpl       # Apache + PHP (Debian)
├── Dockerfile.symfony.tmpl    # Symfony-optimized variant
├── Dockerfile.ci.tmpl         # Alpine CI variant
└── Dockerfile.frankenphp.tmpl # FrankenPHP (Alpine/Bookworm)
```

## Configuration (config.py)

Simple Python dictionaries define everything:

```python
VARIANTS = {
    'base': {
        'packages': ['git', 'gnupg', 'unzip', 'zip'],
        'php_exts': ['opcache', 'pdo_mysql'],
        ...
    },
}

PHP_VERSIONS = [
    {'version': '8.5', 'variants': ['base', 'symfony', 'ci', ...]},
]
```

## Adding a New PHP Version

1. Edit `config.py`:
```python
PHP_VERSIONS = [
    ...
    {'version': '8.6', 'variants': ['base', 'symfony', 'ci']},
]
```

2. Generate: `python3 generate.py`

## Benefits

- ✅ **4 templates** vs 36+ Dockerfiles
- ✅ **Pure Python** - no external tools needed
- ✅ **Simple & readable** - easy to understand and modify
- ✅ **Consistent** - all variants use same patterns

## Bug Fixes

This template system fixed:
- FrankenPHP Bookworm using wrong package manager (was `apk`, now `apt-get`)
