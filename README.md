# Infinite Flight Localization

This repository is for translating the [Infinite Flight](https://infiniteflight.com) app into other languages. Contributors must sign the CLA and contribute via Pull Requests.

## Supported languages

The base language of the app is English. Infinite Flight will provide all the base strings inside the `en/AppResources.resx` file. We have added additional translations for:
 - Spanish
 - French

If you are interested in contributing a language, please create an Issue first so you can be assigned by Infinite Flight staff to make sure this isn't already being contributed.

## Creating a new language

To begin translating Infinite Flight into a new language, create a new file called `AppResources.[code].resx`. This code should be the two-digit ISO-639-1 language code, which you can reference from [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

## How to edit

Localization files are in `resx` format, which is a version of XML designated for localizing app strings. This means you can edit these files inside a text editor or using a specialist editor.

### Recommended: ResxResourceManager
_This is only supported on Windows_

ResxResourceManager allows you to easily see all missing translations from the base English version. You can show the original English version in a column for easy editing, or import/export to a spreadsheet.

Download: [https://github.com/dotnet/ResXResourceManager/releases](https://github.com/dotnet/ResXResourceManager/releases)

### ResX Editor for VSCode

Download: [https://marketplace.visualstudio.com/items?itemName=DominicVonk.vscode-resx-editor](https://marketplace.visualstudio.com/items?itemName=DominicVonk.vscode-resx-editor)

### Edit the source

Each `.resx` file is an XML file and can be edited inside a text editor.

## Formatting and Verbiage

 - Use commonly known aviation terms where possible. Infinite Flight aims to be accessible without requiring technical language to be learned.

 - Text strings with values such as `{0}` and `{1}` represent variables which are replaced at runtime in the simulator. The comments should explain what these variables represent, but please ask if you are unsure.

## Pull Request Reviews

Before a new language is added into Infinite Flight, the PR should be reviewed by another speaker of this language to ensure the content is correct.
