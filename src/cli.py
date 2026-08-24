import click

@click.group()
def cli():
    pass

@cli.command()
def topology():
    click.echo("Showing topology")

if __name__ == '__main__':
    cli()
