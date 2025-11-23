#!/usr/bin/env python3
"""
Configuration loader for PHP Docker images.
Loads configuration from config.yaml and generates build matrix.
"""

import yaml
from pathlib import Path


def load_config():
    """Load configuration from YAML file."""
    config_path = Path(__file__).parent / 'config.yaml'

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    return config


def get_build_matrix():
    """Generate the build matrix for all PHP versions and variants."""
    config = load_config()

    variants = config['variants']
    php_versions = config['php_versions']

    matrix = []

    for php_version in php_versions:
        version = php_version['version']

        for variant_type in php_version['variants']:
            if variant_type not in variants:
                raise ValueError(
                    f"Variant '{variant_type}' referenced by PHP {version} "
                    f"is not defined in variants section"
                )

            variant_config = variants[variant_type].copy()

            # Apply package overrides for this PHP version if specified
            if 'package_overrides' in php_version and variant_type in php_version['package_overrides']:
                variant_config['packages'] = php_version['package_overrides'][variant_type]

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
                'needs_stretch_repo_update': php_version.get('needs_stretch_repo_update', False),
                'config': variant_config,
            })

    return matrix


if __name__ == '__main__':
    # Test the configuration
    try:
        matrix = get_build_matrix()
        print(f"✓ Configuration loaded successfully")
        print(f"  Total variants: {len(matrix)}")
        print(f"  Active variants: {len([m for m in matrix if not m['legacy']])}")
        print(f"  Legacy variants: {len([m for m in matrix if m['legacy']])}")
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        import sys
        sys.exit(1)
