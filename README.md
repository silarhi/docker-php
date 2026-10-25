# Docker PHP
[![Continuous Integration](https://github.com/silarhi/docker-php/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/silarhi/docker-php/actions/workflows/continuous-integration.yml)

Docker images for PHP 8.1 to 8.6 apps: Apache (Debian, with a Symfony variant), FrankenPHP (Debian or Alpine) and CI
(Alpine). PHP 8.6 images are built from the upstream release candidate until 8.6.0 is released. Legacy images for PHP
5.6 to 8.0 are still available but are no longer rebuilt automatically.

* GitHub: https://github.com/silarhi/docker-php
* Demo: https://labs.silarhi.fr/php
* Demo (404): https://labs.silarhi.fr/php/notfound
* Docker image: https://hub.docker.com/r/silarhi/php-apache
* Blog post: https://blog.silarhi.fr/image-docker-php-apache-parfaite/

## Available Images

### Current Versions

| PHP Version | Tag | Base OS | Web Server | Public Folder | Size | Usage |
|-------------|-----|---------|------------|---------------|------|-------|
| 8.6 (RC) | `8.6` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.6) | Preview (release candidate) |
| 8.6 (RC) | `8.6-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.6-ci) | CI/CD pipelines (preview) |
| 8.6 (RC) | `8.6-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.6-symfony) | Symfony apps (preview) |
| 8.5 (latest) | `latest`, `8.5` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5) | Production |
| 8.5 | `8.5-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-ci) | CI/CD pipelines |
| 8.5 | `8.5-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-symfony) | Symfony apps |
| 8.5 | `8.5-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-alpine) | Production (FrankenPHP) |
| 8.5 | `8.5-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.5 | `8.5-frankenphp-trixie` | Debian Trixie | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.5-frankenphp-trixie) | Production (FrankenPHP) |
| 8.4 | `8.4` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4) | Production |
| 8.4 | `8.4-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-ci) | CI/CD pipelines |
| 8.4 | `8.4-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-symfony) | Symfony apps |
| 8.4 | `8.4-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-alpine) | Production (FrankenPHP) |
| 8.4 | `8.4-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.4 | `8.4-frankenphp-trixie` | Debian Trixie | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.4-frankenphp-trixie) | Production (FrankenPHP) |
| 8.3 | `8.3` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3) | Production |
| 8.3 | `8.3-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-ci) | CI/CD pipelines |
| 8.3 | `8.3-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-symfony) | Symfony apps |
| 8.3 | `8.3-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-alpine) | Production (FrankenPHP) |
| 8.3 | `8.3-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.3 | `8.3-frankenphp-trixie` | Debian Trixie | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.3-frankenphp-trixie) | Production (FrankenPHP) |
| 8.2 | `8.2` | Debian Trixie | Apache | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2) | Production |
| 8.2 | `8.2-ci` | Alpine | - | `/app` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-ci) | CI/CD pipelines |
| 8.2 | `8.2-symfony` | Debian Trixie | Apache | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-symfony) | Symfony apps |
| 8.2 | `8.2-frankenphp-alpine` | Alpine | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-alpine) | Production (FrankenPHP) |
| 8.2 | `8.2-frankenphp-bookworm` | Debian Bookworm | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-bookworm) | Production (FrankenPHP) |
| 8.2 | `8.2-frankenphp-trixie` | Debian Trixie | FrankenPHP | `/app/public` | ![Docker Image Size](https://img.shields.io/docker/image-size/silarhi/php-apache/8.2-frankenphp-trixie) | Production (FrankenPHP) |
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
- **FrankenPHP Trixie (`X.Y-frankenphp-trixie`)**: Debian Trixie-based images using FrankenPHP server for modern PHP apps
- **FrankenPHP Bookworm (`X.Y-frankenphp-bookworm`)**: Same on Debian Bookworm, kept for existing users: prefer the Trixie variant

## Configuration

PHP settings of the Apache and FrankenPHP images live in `conf/php.ini` (installed as `conf.d/app.ini`).

| Environment variable | Default | Effect |
|----------------------|---------|--------|
| `PHP_OPCACHE_VALIDATE_TIMESTAMPS` | `0` | `opcache.validate_timestamps`. With `0`, PHP files are compiled once and never checked for changes: restart the container to deploy new code. Set it to `1` when the sources are mounted and edited in place (local development). |

## Front Controller URLs

The Symfony and FrankenPHP images answer `/index.php` and `/index.php/foo` with a 308 redirect to `/` and `/foo`,
keeping the query string and the path prefix a proxy stripped (`X-Forwarded-Prefix`, sent by Traefik's
`stripprefix`). Symfony strips the script name before routing, so these URLs would otherwise serve a
duplicate of every page, and requests like `/index.php/admin` would slip past proxy rules written for `/admin`.
The standard Apache images (`X.Y`) leave these URLs alone, for apps that rely on them.

## FrankenPHP

Prefer the Debian variants (`-trixie`) in production: PHP is
[noticeably slower on musl](https://frankenphp.dev/docs/performance/#avoid-musl-in-production-prefer-glibc-builds)
(Alpine), especially in the thread-safe build FrankenPHP uses.

The default `/etc/frankenphp/Caddyfile` reads these environment variables:

| Environment variable | Default | Effect |
|----------------------|---------|--------|
| `SERVER_NAME` | `:80` | Site address. Plain HTTP on port 80: TLS is left to the reverse proxy. |
| `SERVER_ROOT` | `/app/public` | Document root. |
| `FRANKENPHP_CONFIG` | | Options of the global [`frankenphp`](https://frankenphp.dev/docs/config/#caddyfile-config) block: workers, threads, `php_ini`... |
| `FRANKENPHP_WORKER_CONFIG` | | Extra options of the Symfony worker below, e.g. `watch` in development. |
| `CADDY_GLOBAL_OPTIONS`, `CADDY_SERVERS_CONFIG` | | Extra global options, and options of the `servers` block (e.g. `max_header_size 32KB`). |
| `CADDY_SERVER_EXTRA_DIRECTIVES` | | Extra directives of the site block. |
| `CADDY_EXTRA_CONFIG` | | Extra site blocks. You can also add `*.caddyfile` files to `/etc/frankenphp/Caddyfile.d/`. |

### Worker mode (Symfony)

```dockerfile
# Symfony 7.4+ (native support in symfony/runtime)
ENV FRANKENPHP_CONFIG="import symfony-worker-native.Caddyfile"
# Symfony < 7.4, with runtime/frankenphp-symfony installed
ENV FRANKENPHP_CONFIG="import symfony-worker.Caddyfile"
```

The worker is named `symfony` in logs and metrics. Its code stays in memory, so `PHP_OPCACHE_VALIDATE_TIMESTAMPS=1` is
not enough to see changes in development: set `FRANKENPHP_WORKER_CONFIG=watch` to restart the worker when a `.env`,
`.php`, `.twig` or `.yaml` file changes under `/app`.

### Threads and memory

By default FrankenPHP starts 2 PHP threads per CPU and never more. Size them from a load test, and keep
`max_threads` × `memory_limit` below the container memory:

```yaml
# compose.yaml: one option per line, which a Dockerfile ENV can't hold
services:
    app:
        environment:
            # Scale up to what memory_limit allows, time out requests waiting more than 30s for a thread,
            # and restart each thread after 500 requests to contain memory leaks.
            FRANKENPHP_CONFIG: |
                import symfony-worker-native.Caddyfile
                max_threads auto
                max_wait_time 30s
                max_requests 500
            # Let the Go runtime know the container memory limit.
            GOMEMLIMIT: 900MiB
        deploy:
            resources:
                limits:
                    memory: 1G
```

Since FrankenPHP 1.13, `num_threads` counts only the threads left for requests no worker serves: worker threads come on
top of it. Caddy also limits request headers to 16 KiB, drops headers whose name contains `_` or `.`, and cuts off reads
and writes stalled for 1 minute. Request bodies idle for 60s are aborted as well (`request_body_timeout` in
`php_server`).

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
