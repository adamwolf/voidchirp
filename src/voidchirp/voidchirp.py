import click

from src.voidchirp import post
from src.voidchirp.cli import configure_logging


@click.command('voidchirp')
@click.argument('status', metavar='<tweet>')
@click.option('-q', '--quiet', 'verbosity', flag_value='quiet')
@click.option('-v', '--verbose', 'verbosity', flag_value='verbose')
def cli(status, verbosity):
    """voidchirp tweets to your Twitter account from the command line."""
    configure_logging(verbosity)
    return post(status)


if __name__ == "__main__":
    cli()
