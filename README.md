# Docker PHP Apache
[![ci](https://github.com/silarhi/docker-php/actions/workflows/ci.yml/badge.svg)](https://github.com/silarhi/docker-php/actions/workflows/ci.yml)

A Docker image for PHP apps based on Debian. Works with Apache and PHP from 5.6 to 8.5 and provide a Symfony variant.

* GitHub: https://github.com/silarhi/docker-php
* Demo: https://labs.silarhi.fr/php
* Demo (404): https://labs.silarhi.fr/php/notfound
* Docker image: https://hub.docker.com/r/silarhi/php-apache
* Blog post: https://blog.silarhi.fr/image-docker-php-apache-parfaite/

## Available Images

### Current Versions

| PHP Version | Tag | Base OS | Web Server | Size | Usage |
|-------------|-----|---------|------------|------|-------|
| 8.5 (latest) | `latest`, `8.5` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5) | Production |
| 8.5 | `8.5-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-ci) | CI/CD pipelines |
| 8.5 | `8.5-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-symfony) | Symfony apps |
| 8.5 | `8.5-frankenphp-alpine` | Alpine | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-alpine) | Production (FrankenPHP) |
| 8.5 | `8.5-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.4 | `8.4` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4) | Production |
| 8.4 | `8.4-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-ci) | CI/CD pipelines |
| 8.4 | `8.4-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-symfony) | Symfony apps |
| 8.4 | `8.4-frankenphp-alpine` | Alpine | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-alpine) | Production (FrankenPHP) |
| 8.4 | `8.4-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.3 | `8.3` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3) | Production |
| 8.3 | `8.3-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-ci) | CI/CD pipelines |
| 8.3 | `8.3-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-symfony) | Symfony apps |
| 8.3 | `8.3-frankenphp-alpine` | Alpine | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-alpine) | Production (FrankenPHP) |
| 8.3 | `8.3-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.2 | `8.2` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2) | Production |
| 8.2 | `8.2-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-ci) | CI/CD pipelines |
| 8.2 | `8.2-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-symfony) | Symfony apps |
| 8.2 | `8.2-frankenphp-alpine` | Alpine | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-alpine) | Production (FrankenPHP) |
| 8.2 | `8.2-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.1 | `8.1` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.1) | Production |
| 8.1 | `8.1-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.1-ci) | CI/CD pipelines |
| 8.1 | `8.1-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.1-symfony) | Symfony apps |

### Legacy Versions

| PHP Version | Tag | Base OS | Web Server | Size | Usage |
|-------------|-----|---------|------------|------|-------|
| 8.0 | `8.0` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.0) | Production (Legacy) |
| 8.0 | `8.0-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.0-ci) | CI/CD pipelines (Legacy) |
| 8.0 | `8.0-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.0-symfony) | Symfony apps (Legacy) |
| 7.4 | `7.4` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.4) | Production (Legacy) |
| 7.4 | `7.4-ci` | Alpine | - | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.4-ci) | CI/CD pipelines (Legacy) |
| 7.4 | `7.4-symfony` | Debian Bookworm | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.4-symfony) | Symfony apps (Legacy) |
| 7.3 | `7.3` | Debian Buster | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.3) | Production (Legacy) |
| 7.3 | `7.3-symfony` | Debian Buster | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.3-symfony) | Symfony apps (Legacy) |
| 7.2 | `7.2` | Debian Buster | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.2) | Production (Legacy) |
| 7.2 | `7.2-symfony` | Debian Buster | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.2-symfony) | Symfony apps (Legacy) |
| 7.1 | `7.1` | Debian Stretch | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.1) | Production (Legacy) |
| 7.1 | `7.1-symfony` | Debian Stretch | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.1-symfony) | Symfony apps (Legacy) |
| 5.6 | `5.6` | Debian Stretch | Apache | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/5.6) | Production (Legacy) |

### Image Variants Explained

- **Standard (`X.Y`)**: Production-ready images with Apache and common PHP extensions (opcache, pdo_mysql)
- **CI (`X.Y-ci`)**: Lightweight Alpine-based images optimized for CI/CD pipelines
- **Symfony (`X.Y-symfony`)**: Enhanced images with additional extensions for Symfony applications (intl, zip)
- **FrankenPHP Alpine (`X.Y-frankenphp-alpine`)**: Alpine-based images using FrankenPHP server for modern PHP apps
- **FrankenPHP Bookworm (`X.Y-frankenphp-bookworm`)**: Debian-based images using FrankenPHP server for modern PHP apps
