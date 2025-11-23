#!/usr/bin/env python3
"""
Configuration for PHP Docker images.
Defines all PHP versions, variants, and their settings.
"""

# Variant definitions
VARIANTS = {
    'base': {
        'type': 'base',
        'base_image': 'php:{version}-apache',
        'packages': ['git', 'gnupg', 'unzip', 'zip'],
        'php_exts': ['opcache', 'pdo_mysql'],
        'ext_config': [],
        'server': 'apache',
        'package_manager': 'apt',
        'health_check': 'curl -f http://localhost/_health || exit 1',
    },
    'symfony': {
        'type': 'symfony',
        'base_image': 'php:{version}-apache',
        'packages': ['git', 'gnupg', 'libicu-dev', 'libzip-dev', 'unzip', 'zip', 'zlib1g-dev'],
        'php_exts': ['intl', 'opcache', 'pdo_mysql', 'zip'],
        'ext_config': ['zip'],
        'server': 'apache',
        'package_manager': 'apt',
        'health_check': 'curl -f http://localhost/_health || exit 1',
    },
    'ci': {
        'type': 'ci',
        'base_image': 'php:{version}-alpine',
        'packages': ['bash', 'icu', 'libxml2', 'libzip', 'git', 'zlib'],
        'php_exts': ['intl', 'opcache', 'zip'],
        'ext_config': [],
        'server': 'none',
        'package_manager': 'apk',
        'health_check': 'curl -f http://localhost/_health || exit 1',
    },
    'frankenphp-alpine': {
        'type': 'frankenphp-alpine',
        'base_image': 'dunglas/frankenphp:1-php{version}-alpine',
        'packages': ['git', 'gnupg', 'unzip', 'zip'],
        'php_exts': ['@composer', 'opcache', 'pdo_mysql'],
        'ext_config': [],
        'server': 'frankenphp',
        'package_manager': 'apk',
        'health_check': 'curl -f http://localhost:2019/metrics || exit 1',
        'use_install_php_extensions': True,
    },
    'frankenphp-bookworm': {
        'type': 'frankenphp-bookworm',
        'base_image': 'dunglas/frankenphp:1-php{version}-bookworm',
        'packages': ['git', 'gnupg', 'unzip', 'zip'],
        'php_exts': ['@composer', 'opcache', 'pdo_mysql'],
        'ext_config': [],
        'server': 'frankenphp',
        'package_manager': 'apt',
        'health_check': 'curl -f http://localhost:2019/metrics || exit 1',
        'use_install_php_extensions': True,
    },
}

# PHP versions and their available variants
PHP_VERSIONS = [
    {'version': '5.6', 'variants': ['base'], 'legacy': True, 'debian_suffix': ''},
    {'version': '7.1', 'variants': ['base', 'symfony'], 'legacy': True, 'debian_suffix': '-stretch'},
    {'version': '7.2', 'variants': ['base', 'symfony'], 'legacy': True, 'debian_suffix': '-stretch'},
    {'version': '7.3', 'variants': ['base', 'symfony'], 'legacy': True, 'debian_suffix': '-stretch'},
    {'version': '7.4', 'variants': ['base', 'symfony', 'ci'], 'legacy': True, 'debian_suffix': ''},
    {'version': '8.0', 'variants': ['base', 'symfony', 'ci'], 'legacy': True, 'debian_suffix': ''},
    {'version': '8.1', 'variants': ['base', 'symfony', 'ci'], 'legacy': False, 'debian_suffix': ''},
    {'version': '8.2', 'variants': ['base', 'symfony', 'ci', 'frankenphp-alpine', 'frankenphp-bookworm'], 'legacy': False, 'debian_suffix': ''},
    {'version': '8.3', 'variants': ['base', 'symfony', 'ci', 'frankenphp-alpine', 'frankenphp-bookworm'], 'legacy': False, 'debian_suffix': ''},
    {'version': '8.4', 'variants': ['base', 'symfony', 'ci', 'frankenphp-alpine', 'frankenphp-bookworm'], 'legacy': False, 'debian_suffix': ''},
    {'version': '8.5', 'variants': ['base', 'symfony', 'ci', 'frankenphp-alpine', 'frankenphp-bookworm'], 'legacy': False, 'debian_suffix': ''},
]

def get_build_matrix():
    """Generate the build matrix for all PHP versions and variants."""
    matrix = []

    for php_version in PHP_VERSIONS:
        version = php_version['version']

        for variant_type in php_version['variants']:
            variant_config = VARIANTS[variant_type].copy()

            # Determine variant name
            variant_name = version if variant_type == 'base' else f"{version}-{variant_type}"

            # Substitute version in base_image with Debian suffix for old versions
            debian_suffix = php_version.get('debian_suffix', '')

            # Build the base image string
            if variant_type in ['base', 'symfony'] and debian_suffix:
                # For apache variants with debian suffix, modify the template then format
                base_template = variant_config['base_image'].replace('-apache', f'-apache{debian_suffix}')
                variant_config['base_image'] = base_template.format(version=version)
            else:
                # For other variants (ci, frankenphp) or no suffix, just substitute version normally
                variant_config['base_image'] = variant_config['base_image'].format(version=version)

            # Determine OS variant for FrankenPHP
            os_variant = None
            if variant_type == 'frankenphp-alpine':
                os_variant = 'alpine'
            elif variant_type == 'frankenphp-bookworm':
                os_variant = 'bookworm'

            matrix.append({
                'version': version,
                'variant_type': variant_type,
                'variant_name': variant_name,
                'legacy': php_version['legacy'],
                'latest': version == '8.5' and variant_type == 'base',
                'os_variant': os_variant,
                'config': variant_config,
            })

    return matrix

if __name__ == '__main__':
    # Test the configuration
    matrix = get_build_matrix()
    print(f"Total variants: {len(matrix)}")
    print(f"Active variants: {len([m for m in matrix if not m['legacy']])}")
    print(f"Legacy variants: {len([m for m in matrix if m['legacy']])}")
