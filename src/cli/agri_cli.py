"""Command-line interface"""
import click
from loguru import logger

@click.group()
def cli():
    """Agriautonomous CLI"""
    pass

@cli.command()
@click.option('--name', default='Mission', help='Mission name')
def create_mission(name):
    """Create a new mission"""
    logger.info(f"Creating mission: {name}")
    click.echo(f"Mission '{name}' created successfully")

@cli.command()
@click.argument('mission_id')
def arm_mission(mission_id):
    """Arm a mission"""
    logger.info(f"Arming mission: {mission_id}")
    click.echo(f"Mission '{mission_id}' armed")

@cli.command()
@click.argument('mission_id')
def execute_mission(mission_id):
    """Execute a mission"""
    logger.info(f"Executing mission: {mission_id}")
    click.echo(f"Mission '{mission_id}' started")

@cli.command()
@click.argument('asset_id')
def asset_status(asset_id):
    """Get asset status"""
    logger.info(f"Getting status for asset: {asset_id}")
    click.echo(f"Asset '{asset_id}' status retrieved")

@cli.command()
def list_assets():
    """List all assets"""
    logger.info("Listing all assets")
    click.echo("Registered assets:")
    click.echo("  - SCOUT_DRONE_001")
    click.echo("  - ACTION_DRONE_001")
    click.echo("  - UGV_001")

@cli.command()
def system_status():
    """Get system status"""
    click.echo("Agriautonomous System Status")
    click.echo("============================")
    click.echo(f"Status: Running")
    click.echo(f"Database: Connected")
    click.echo(f"Hardware: Ready")

@cli.command()
@click.option('--config', default='config.json', help='Config file path')
def configure(config):
    """Configure system"""
    logger.info(f"Configuring with: {config}")
    click.echo(f"System configured from {config}")

if __name__ == '__main__':
    cli()
