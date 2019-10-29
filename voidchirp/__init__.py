import sys
import tweepy
import click
import webbrowser
import keyring
import logging

# Sadly, this makes voidchirp macOS only until PyInstaller plays nicer with entrypoints
# See https://github.com/jaraco/keyring/issues/324
# and https://github.com/pyinstaller/pyinstaller/issues/1188
from keyring.backends import OS_X

keyring.set_keyring(OS_X.Keyring())


def configure_auth(consumer_key, consumer_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError as e:
        logging.error("Failed to get request token URL. Exiting.")
        logging.error(e)
        sys.exit(1)

    try:
        prompt = "To continue, you need a pin located at {}.  "\
                 "Would you like voidchirp to try to open it in a web browser?".format(redirect_url)

        click.confirm(prompt, abort=True)
        webbrowser.open(redirect_url)
    except click.Abort:
        logging.debug("Not opening a web browser.")

    verifier = click.prompt('Twitter should have given you a PIN to authorize your application.  Enter it to continue')

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError as e:
        logging.error("Exiting. Failed to get access token: {}".format(e))
        sys.exit(1)

    logging.info(
        "Storing consumer key, consumer token, access token, and access token secret in your Keychain. macOS may ask "
        "for your Keychain password.")
    keyring.set_password('voidchirp', 'consumer_key', consumer_key)
    keyring.set_password('voidchirp', 'consumer_secret', consumer_secret)
    keyring.set_password('voidchirp', 'access_token', auth.access_token)
    keyring.set_password('voidchirp', 'access_token_secret', auth.access_token_secret)
    logging.info("Successfully saved credentials!")


def check_auth():
    credentials = {}
    for credential in "access_token", "access_token_secret", "consumer_key", "consumer_secret":
        credentials[credential] = keyring.get_password('voidchirp', credential)
    absent_credentials = []
    for credential, value in credentials.items():
        if value is None:
            absent_credentials.append(credential)
    if absent_credentials:
        logging.error("Unable to find credentials in keychain for the following items: {}".format(absent_credentials))
        logging.error("Try configuring the authentication.")
        sys.exit(1)
    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    return auth


def post(status):
    auth = check_auth()
    api = tweepy.API(auth)
    if len(status) >= 280:
        logging.error("A tweet must be 280 characters or fewer, while this message was {} characters long.".format(len(status)))
        sys.exit(1)
    elif not status:
        logging.error("A tweet must exist!")
        sys.exit(1)
    else:
        try:
            post_status = api.update_status(status=status)
            url = "https://twitter.com/i/web/status/{}".format(post_status.id_str)
            logging.debug("Posted tweet to {}".format(url))
        except tweepy.TweepError as inst:
            logging.error("Error posting tweet: {}".format(inst))
            sys.exit(1)


if __name__ == "__main__":
    cli()
