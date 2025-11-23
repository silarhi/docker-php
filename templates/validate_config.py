#!/usr/bin/env python3
"""
Configuration validation for PHP Docker images.
Validates config.yaml against expected schema.
"""

import sys
from pathlib import Path
import yaml


class ConfigValidator:
    """Validates configuration YAML files."""

    REQUIRED_VARIANT_FIELDS = {
        'type', 'base_image', 'packages', 'php_exts',
        'server', 'package_manager', 'health_check'
    }

    REQUIRED_PHP_VERSION_FIELDS = {
        'version', 'variants', 'legacy', 'debian_suffix', 'needs_stretch_repo_update'
    }

    VALID_VARIANT_TYPES = {
        'base', 'symfony', 'ci', 'frankenphp-alpine', 'frankenphp-bookworm'
    }

    VALID_PACKAGE_MANAGERS = {'apt', 'apk'}
    VALID_SERVERS = {'apache', 'frankenphp', 'none'}

    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.errors = []
        self.warnings = []

    def validate(self):
        """Run all validation checks."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            self.errors.append(f"Failed to load YAML: {e}")
            return False

        if not isinstance(self.config, dict):
            self.errors.append("Config must be a dictionary")
            return False

        self._validate_structure()
        self._validate_variants()
        self._validate_php_versions()
        self._validate_cross_references()

        return len(self.errors) == 0

    def _validate_structure(self):
        """Validate top-level structure."""
        if 'variants' not in self.config:
            self.errors.append("Missing 'variants' section")
        if 'php_versions' not in self.config:
            self.errors.append("Missing 'php_versions' section")

    def _validate_variants(self):
        """Validate variant definitions."""
        if 'variants' not in self.config:
            return

        variants = self.config['variants']
        if not isinstance(variants, dict):
            self.errors.append("'variants' must be a dictionary")
            return

        for variant_name, variant_config in variants.items():
            self._validate_variant(variant_name, variant_config)

    def _validate_variant(self, name, config):
        """Validate a single variant configuration."""
        if not isinstance(config, dict):
            self.errors.append(f"Variant '{name}': must be a dictionary")
            return

        # Check required fields
        missing = self.REQUIRED_VARIANT_FIELDS - set(config.keys())
        if missing:
            self.errors.append(f"Variant '{name}': missing fields {missing}")

        # Validate field values
        if 'type' in config and config['type'] not in self.VALID_VARIANT_TYPES:
            self.errors.append(
                f"Variant '{name}': invalid type '{config['type']}', "
                f"must be one of {self.VALID_VARIANT_TYPES}"
            )

        if 'package_manager' in config and config['package_manager'] not in self.VALID_PACKAGE_MANAGERS:
            self.errors.append(
                f"Variant '{name}': invalid package_manager '{config['package_manager']}', "
                f"must be one of {self.VALID_PACKAGE_MANAGERS}"
            )

        if 'server' in config and config['server'] not in self.VALID_SERVERS:
            self.errors.append(
                f"Variant '{name}': invalid server '{config['server']}', "
                f"must be one of {self.VALID_SERVERS}"
            )

        # Validate lists
        for list_field in ['packages', 'php_exts', 'ext_config']:
            if list_field in config and not isinstance(config[list_field], list):
                self.errors.append(f"Variant '{name}': '{list_field}' must be a list")

        # Validate strings
        for str_field in ['base_image', 'health_check']:
            if str_field in config:
                if not isinstance(config[str_field], str):
                    self.errors.append(f"Variant '{name}': '{str_field}' must be a string")
                elif not config[str_field]:
                    self.errors.append(f"Variant '{name}': '{str_field}' cannot be empty")

        # Check base_image has {version} placeholder (except for specific cases)
        if 'base_image' in config and isinstance(config['base_image'], str):
            if '{version}' not in config['base_image']:
                self.warnings.append(
                    f"Variant '{name}': base_image missing {{version}} placeholder"
                )

    def _validate_php_versions(self):
        """Validate PHP version definitions."""
        if 'php_versions' not in self.config:
            return

        php_versions = self.config['php_versions']
        if not isinstance(php_versions, list):
            self.errors.append("'php_versions' must be a list")
            return

        if not php_versions:
            self.errors.append("'php_versions' cannot be empty")
            return

        for idx, version_config in enumerate(php_versions):
            self._validate_php_version(idx, version_config)

    def _validate_php_version(self, idx, config):
        """Validate a single PHP version configuration."""
        if not isinstance(config, dict):
            self.errors.append(f"PHP version #{idx}: must be a dictionary")
            return

        # Check required fields
        missing = self.REQUIRED_PHP_VERSION_FIELDS - set(config.keys())
        if missing:
            self.errors.append(f"PHP version #{idx}: missing fields {missing}")

        version = config.get('version', f'#{idx}')

        # Validate version format
        if 'version' in config:
            if not isinstance(config['version'], str):
                self.errors.append(f"PHP version {version}: version must be a string")
            elif not config['version']:
                self.errors.append(f"PHP version {version}: version cannot be empty")

        # Validate variants list
        if 'variants' in config:
            if not isinstance(config['variants'], list):
                self.errors.append(f"PHP version {version}: variants must be a list")
            elif not config['variants']:
                self.errors.append(f"PHP version {version}: variants cannot be empty")

        # Validate boolean fields
        for bool_field in ['legacy', 'needs_stretch_repo_update']:
            if bool_field in config and not isinstance(config[bool_field], bool):
                self.errors.append(f"PHP version {version}: '{bool_field}' must be boolean")

        # Validate debian_suffix
        if 'debian_suffix' in config and not isinstance(config['debian_suffix'], str):
            self.errors.append(f"PHP version {version}: 'debian_suffix' must be a string")

        # Validate stretch logic
        if config.get('needs_stretch_repo_update') and config.get('debian_suffix') != '-stretch':
            self.warnings.append(
                f"PHP version {version}: needs_stretch_repo_update=true but "
                f"debian_suffix is not '-stretch'"
            )

    def _validate_cross_references(self):
        """Validate cross-references between sections."""
        if 'variants' not in self.config or 'php_versions' not in self.config:
            return

        defined_variants = set(self.config['variants'].keys())

        for version_config in self.config['php_versions']:
            version = version_config.get('version', 'unknown')
            requested_variants = version_config.get('variants', [])

            for variant in requested_variants:
                if variant not in defined_variants:
                    self.errors.append(
                        f"PHP version {version}: references undefined variant '{variant}'"
                    )

    def report(self):
        """Print validation report."""
        if self.errors:
            print("❌ Validation FAILED")
            print(f"\n{len(self.errors)} error(s) found:")
            for error in self.errors:
                print(f"  • {error}")

        if self.warnings:
            print(f"\n{len(self.warnings)} warning(s):")
            for warning in self.warnings:
                print(f"  ⚠ {warning}")

        if not self.errors and not self.warnings:
            print("✓ Configuration is valid")
        elif not self.errors:
            print("\n✓ Configuration is valid (with warnings)")


def main():
    """Main entry point."""
    config_path = Path(__file__).parent / 'config.yaml'

    if len(sys.argv) > 1:
        config_path = Path(sys.argv[1])

    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        sys.exit(1)

    print(f"Validating {config_path}...")
    print()

    validator = ConfigValidator(config_path)
    is_valid = validator.validate()
    validator.report()

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
