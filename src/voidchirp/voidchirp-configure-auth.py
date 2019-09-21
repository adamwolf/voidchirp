import click

from src.voidchirp import configure_auth
from src.voidchirp.cli import configure_logging


@click.command('voidchirp-configure-auth')
@click.option('-q', '--quiet', 'verbosity', flag_value='quiet')
@click.option('-v', '--verbose', 'verbosity', flag_value='verbose')
def cli_configure_auth(verbosity):
    """voidchirp-configure-auth saves your Twitter keys so you can use voidchirp."""
    configure_logging(verbosity)
    consumer_key = click.prompt('Please enter your Twitter Consumer API Key')
    consumer_secret = click.prompt('Please enter your Twitter Consumer Secret')
    return configure_auth(consumer_key, consumer_secret)


if __name__ == "__main__":
    cli_configure_auth()
