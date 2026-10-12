# Docker PHP
[![Continuous Integration](https://github.com/silarhi/docker-php/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/silarhi/docker-php/actions/workflows/continuous-integration.yml)

Docker images for PHP 8.1 to 8.5 apps: Apache (Debian, with a Symfony variant), FrankenPHP (Debian or Alpine) and CI
(Alpine). Legacy images for PHP 5.6 to 8.0 are still available but are no longer rebuilt automatically.

* GitHub: https://github.com/silarhi/docker-php
* Demo: https://labs.silarhi.fr/php
* Demo (404): https://labs.silarhi.fr/php/notfound
* Docker image: https://hub.docker.com/r/silarhi/php-apache
* Blog post: https://blog.silarhi.fr/image-docker-php-apache-parfaite/

## Available Images

### Current Versions

| PHP Version | Tag | Base OS | Web Server | Public Folder | Size | Usage |
|-------------|-----|---------|------------|---------------|------|-------|
| 8.5 (latest) | `latest`, `8.5` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5) | Production |
| 8.5 | `8.5-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-ci) | CI/CD pipelines |
| 8.5 | `8.5-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-symfony) | Symfony apps |
| 8.5 | `8.5-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-alpine) | Production (FrankenPHP) |
| 8.5 | `8.5-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.4 | `8.4` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4) | Production |
| 8.4 | `8.4-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-ci) | CI/CD pipelines |
| 8.4 | `8.4-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-symfony) | Symfony apps |
| 8.4 | `8.4-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-alpine) | Production (FrankenPHP) |
| 8.4 | `8.4-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.3 | `8.3` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3) | Production |
| 8.3 | `8.3-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-ci) | CI/CD pipelines |
| 8.3 | `8.3-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-symfony) | Symfony apps |
| 8.3 | `8.3-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-alpine) | Production (FrankenPHP) |
| 8.3 | `8.3-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.2 | `8.2` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2) | Production |
| 8.2 | `8.2-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-ci) | CI/CD pipelines |
| 8.2 | `8.2-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-symfony) | Symfony apps |
| 8.2 | `8.2-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-alpine) | Production (FrankenPHP) |
| 8.2 | `8.2-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.1 | `8.1` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.1) | Production |
| 8.1 | `8.1-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.1-ci) | CI/CD pipelines |
| 8.1 | `8.1-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.1-symfony) | Symfony apps |

### Legacy Versions

These tags were last pushed on 2024-12-19. They are not part of the CI matrix and are only rebuilt by hand with
`make build-legacy`, so they no longer receive OS or PHP security updates.

| PHP Version | Tag | Base OS | Web Server | Public Folder | Size | Usage |
|-------------|-----|---------|------------|---------------|------|-------|
| 8.0 | `8.0` | Debian Bullseye | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.0) | Production (Legacy) |
| 8.0 | `8.0-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.0-ci) | CI/CD pipelines (Legacy) |
| 8.0 | `8.0-symfony` | Debian Bullseye | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.0-symfony) | Symfony apps (Legacy) |
| 7.4 | `7.4` | Debian Bullseye | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.4) | Production (Legacy) |
| 7.4 | `7.4-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.4-ci) | CI/CD pipelines (Legacy) |
| 7.4 | `7.4-symfony` | Debian Bullseye | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.4-symfony) | Symfony apps (Legacy) |
| 7.3 | `7.3` | Debian Stretch | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.3) | Production (Legacy) |
| 7.3 | `7.3-symfony` | Debian Stretch | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.3-symfony) | Symfony apps (Legacy) |
| 7.2 | `7.2` | Debian Stretch | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.2) | Production (Legacy) |
| 7.2 | `7.2-symfony` | Debian Stretch | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.2-symfony) | Symfony apps (Legacy) |
| 7.1 | `7.1` | Debian Stretch | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.1) | Production (Legacy) |
| 7.1 | `7.1-symfony` | Debian Stretch | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/7.1-symfony) | Symfony apps (Legacy) |
| 5.6 | `5.6` | Debian Stretch | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/5.6) | Production (Legacy) |

### Image Variants Explained

- **Standard (`X.Y`)**: Production-ready images with Apache and common PHP extensions (opcache, pdo_mysql)
- **CI (`X.Y-ci`)**: Lightweight Alpine-based images optimized for CI/CD pipelines
- **Symfony (`X.Y-symfony`)**: Enhanced images with additional extensions for Symfony applications (intl, zip)
- **FrankenPHP Alpine (`X.Y-frankenphp-alpine`)**: Alpine-based images using FrankenPHP server for modern PHP apps
- **FrankenPHP Bookworm (`X.Y-frankenphp-bookworm`)**: Debian-based images using FrankenPHP server for modern PHP apps

## Configuration

PHP settings of the Apache and FrankenPHP images live in `conf/php.ini` (installed as `conf.d/app.ini`).

| Environment variable | Default | Effect |
|----------------------|---------|--------|
| `PHP_OPCACHE_VALIDATE_TIMESTAMPS` | `0` | `opcache.validate_timestamps`. With `0`, PHP files are compiled once and never checked for changes: restart the container to deploy new code. Set it to `1` when the sources are mounted and edited in place (local development). |

## Running Behind a Reverse Proxy

The Apache and FrankenPHP images trust `X-Forwarded-*` headers from private networks (Docker, Traefik, load balancers)
and from [Cloudflare's IP ranges](https://www.cloudflare.com/ips/), and resolve the proxy chain before PHP runs:

- `REMOTE_ADDR` is the visitor IP, read right to left from `X-Forwarded-For` up to the first untrusted address
  (`mod_remoteip` on Apache, `trusted_proxies` on FrankenPHP). `X-Forwarded-For` is not passed on to PHP.
- `HTTPS` is `on` when the request reached the proxy over HTTPS (`X-Forwarded-Proto: https`).

On FrankenPHP, `CADDY_TRUSTED_PROXIES_RANGES` replaces the trusted ranges. `X-Forwarded-Proto` is accepted from any
client, so only expose the containers through the proxy.

**Cloudflare → Traefik → container**: Traefik must trust Cloudflare as well. Otherwise it replaces `X-Forwarded-For`
with the Cloudflare edge address, and every visitor shows up with a Cloudflare IP.

```toml
[entryPoints.websecure.forwardedHeaders]
  trustedIPs = ["173.245.48.0/20", "103.21.244.0/22", "..."] # every range from https://www.cloudflare.com/ips/
```

**Symfony**: the chain is already resolved, so leave `framework.trusted_proxies` empty or set it to `private_ranges`.
Don't use `REMOTE_ADDR`: it is now the visitor, and Symfony would trust the visitor's own `X-Forwarded-Port` header
when generating URLs.
