# Docker PHP Apache
[![ci](https://github.com/silarhi/docker-php/actions/workflows/ci.yml/badge.svg)](https://github.com/silarhi/docker-php/actions/workflows/ci.yml)

A Docker image for PHP apps based on Debian. Works with Apache and PHP from 5.6 to 8.5 and provides multiple variants (base, Symfony, CI, FrankenPHP).

* GitHub: https://github.com/silarhi/docker-php
* Demo: https://labs.silarhi.fr/php
* Demo (404): https://labs.silarhi.fr/php/notfound
* Docker image: https://hub.docker.com/r/silarhi/php-apache
* Blog post: https://blog.silarhi.fr/image-docker-php-apache-parfaite/

## 🎯 Template-Based Architecture

This project uses a **simple template-based system** to reduce code duplication. Instead of maintaining 36+ individual Dockerfiles, we use:

- **Python configuration** (`templates/config.py`) - Single source of truth for all PHP versions and variants
- **Jinja2 templates** (`templates/*.tmpl`) - 4 templates instead of 36 files
- **Automated generation** (`templates/generate.py`) - Generates all Dockerfiles from templates

### Benefits

- ✅ **Reduced code duplication** - 4 templates vs 36+ Dockerfiles
- ✅ **Guaranteed consistency** - All variants follow the same patterns
- ✅ **Easy maintenance** - Update once, apply to all variants
- ✅ **No external dependencies** - Just Python + Jinja2
- ✅ **Simple & readable** - Pure Python configuration

### Quick Start for Contributors

```bash
# Install dependencies
pip install jinja2

# Generate Dockerfiles from templates
make generate

# Build all images
make build
```

For detailed documentation, see [`templates/README.md`](templates/README.md).
