# language-translator
Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.
Compatible with Python 3.6+.

Features:
*Fast and reliable - it uses the same servers that translate.google.com uses
*Auto language detection
*Bulk translations
*Customizable service URL
*HTTP/2 support

uses:
*Basic Usage:
If source language is not given, google translate attempts to detect the source language.

*Advanced Usage (Bulk):
Array can be used to translate a batch of strings in a single method call and a single HTTP session. The exact same method shown above work for arrays as well.

*Language detection:
The detect method, as its name implies, identifies the language used in a given sentence.
