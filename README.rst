=============
``voidchirp``
=============

Voidchirp is a simple command line tool for posting to Twitter.

Installation
============
Installation via Homebrew
-------------------------

``brew tap adamwolf/voidchirp``

``brew install voidchirp``

Installation via Python
-----------------------
If you are handy with Python, you can download this, setup a virtual environment or however you like to do it, and use Voidchirp that way.

Configuring Authentication
==========================

Because of how Twitter's API works, to use Voidchirp, you'll need to register as a Twitter developer, and sign up for an application.  Save the keys they give you.  There will be a consumer API key and a consumer API secret.

These keys are sensitive, so don't send them around willy-nilly.

Run `voidchirp-configure-auth`.  The tool will walk you through authorizing your app to your Twitter account, and store the keys in your login keychain.

Usage
=====

After you've configured the authentication, you can post to Twitter like this:

``$ voidchirp "hello world"``

It supports extended tweets of 280 characters.

macOS Keychain
--------------

`voidchirp` uses your keychain to store your credentials, and macOS will ask you about each of the four credentials `voidchirp` is asking for.
You can choose "Always Allow", but it will still ask you four times, once for each of the credentials.  After you do that once,
you shouldn't be asked again.

You can open up Keychain Access and see the Access Controls for the voidchirp entries.  They probably look like this:

[Keychain Access Access Controls](docs/assets/keychain_access_access_control.png)

Development
-----------

To create the macOS command-line executables, run ``pyinstaller --onefile src/voidchirp/voidchirp.py`` and
``pyinstaller --onefile src/voidchirp/voidchirp-configure-auth.py``.  The executables are then found inside of ``dist/``.

Getting Help
============

Please `file an issue <https://github.com/adamwolf/voidchirp/issues>`_ on GitHub.

Project Information
===================

``voidchirp`` is released under the
`GNU Affero General Public License v3.0 <https://choosealicense.com/licenses/agpl-3.0/>`_ license.

The code is on `GitHub <https://github.com/adamwolf/voidchirp>`_.

If you'd like to contribute to ``voidchirp`` you're most welcome.
Take a look at the issues for ideas or submit a PR!
