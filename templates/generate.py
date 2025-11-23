#!/usr/bin/env python3
"""
Generate Dockerfiles from templates based on Python configuration.
"""
import os
import shutil
from pathlib import Path
import sys

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("Error: Jinja2 is required. Install with: pip install jinja2", file=sys.stderr)
    sys.exit(1)

# Import configuration
from config import get_build_matrix

def copy_shared_files(target_dir, variant_type, variant_config):
    """Copy shared files to target directory."""
    shared_dir = Path('_shared')
    target_path = Path(target_dir)
    conf_dir = target_path / 'conf'
    conf_dir.mkdir(parents=True, exist_ok=True)

    # Copy common files
    shutil.copy2(shared_dir / 'health.php', target_path / 'health.php')
    shutil.copy2(shared_dir / 'index.php', target_path / 'index.php')
    shutil.copy2(shared_dir / 'conf' / 'php.ini', conf_dir / 'php.ini')

    # Copy errors directory
    errors_target = target_path / 'errors'
    if errors_target.exists():
        shutil.rmtree(errors_target)
    shutil.copytree(shared_dir / 'errors', errors_target)

    # Server-specific files
    server = variant_config.get('server', 'apache')

    if server == 'apache':
        shutil.copy2(shared_dir / 'conf' / 'apache.conf', conf_dir / 'apache.conf')
        if variant_type == 'symfony':
            shutil.copy2(shared_dir / 'conf' / 'vhost-symfony.conf', conf_dir / 'vhost.conf')
        else:
            shutil.copy2(shared_dir / 'conf' / 'vhost.conf', conf_dir / 'vhost.conf')
    elif server == 'frankenphp':
        shutil.copy2(shared_dir / 'conf' / 'Caddyfile', conf_dir / 'Caddyfile')
        shutil.copy2(shared_dir / 'conf' / 'symfony-worker.Caddyfile', conf_dir / 'symfony-worker.Caddyfile')

def generate_dockerfiles(build_matrix):
    """Generate all Dockerfiles from templates."""
    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader('templates'),
        trim_blocks=False,
        lstrip_blocks=False,
        keep_trailing_newline=True
    )

    print(f"Generating {len(build_matrix)} Dockerfiles...")

    for item in build_matrix:
        version = item['version']
        variant_type = item['variant_type']
        variant_name = item['variant_name']
        variant_config = item['config']
        os_variant = item.get('os_variant')

        # Determine target directory
        target_dir = variant_name

        # Create directory
        Path(target_dir).mkdir(parents=True, exist_ok=True)

        # Determine template file
        if variant_type in ['frankenphp-alpine', 'frankenphp-bookworm']:
            template_name = 'Dockerfile.frankenphp.tmpl'
        else:
            template_name = f'Dockerfile.{variant_type}.tmpl'

        # Prepare template context
        context = {
            'version': version,
            'baseImage': variant_config['base_image'],
            'healthCheck': variant_config['health_check'],
            'packages': variant_config.get('packages', []),
            'phpExts': variant_config.get('php_exts', []),
            'server': variant_config.get('server', 'apache'),
            'packageManager': variant_config.get('package_manager', 'apt'),
            'needsStretchRepoUpdate': item.get('needs_stretch_repo_update', False),
        }

        if os_variant:
            context['osVariant'] = os_variant

        # Render template
        template = env.get_template(template_name)
        dockerfile_content = template.render(context)

        # Write Dockerfile
        dockerfile_path = Path(target_dir) / 'Dockerfile'
        with open(dockerfile_path, 'w') as f:
            f.write(dockerfile_content)

        # Copy shared files
        copy_shared_files(target_dir, variant_type, variant_config)

        print(f"  ✓ Generated {variant_name}/Dockerfile")

def main():
    """Main entry point."""
    # Change to repository root
    script_dir = Path(__file__).parent
    os.chdir(script_dir.parent)

    print("Loading configuration...")
    build_matrix = get_build_matrix()

    print(f"\nGenerating Dockerfiles from templates...")
    generate_dockerfiles(build_matrix)

    print(f"\n✓ All Dockerfiles generated successfully!")
    print(f"  Total: {len(build_matrix)} variants")
    print(f"  Active: {len([m for m in build_matrix if not m['legacy']])} variants")
    print(f"  Legacy: {len([m for m in build_matrix if m['legacy']])} variants")

if __name__ == '__main__':
    main()
