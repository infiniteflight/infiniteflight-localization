# Infinite Flight Localization

This repository is for translating the [Infinite Flight](https://infiniteflight.com) app into other languages. Contributors must sign the CLA and contribute via Pull Requests.

## Supported languages

The base language of the app is English. Infinite Flight will provide all the base strings inside the `strings/AppResources.resx` file. We have added additional translations for:
 - Spanish
 - French

If you are interested in contributing a language, please create an Issue first so you can be assigned by Infinite Flight staff to make sure this isn't already being contributed.

## Adding support for a new language

To begin translating Infinite Flight into a new language, create a new file called `strings/AppResources.[code].resx`. This code should be the two-digit ISO-639-1 language code, which you can reference from [here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

Once you have edited this, you can add translations using the same code inside `ServerMessages` and `Tips`.

## How to edit

Localization string files are in `resx` format, which is a version of XML designated for localizing app strings. This means you can edit these files inside a text editor or using a specialist editor.

### Recommended: ResxResourceManager
_This is only supported on Windows_

ResxResourceManager allows you to easily see all missing translations from the base English version. You can show the original English version in a column for easy editing, or import/export to a spreadsheet.

Download: [https://github.com/dotnet/ResXResourceManager/releases](https://github.com/dotnet/ResXResourceManager/releases)

### ResX Editor for VSCode

Download: [https://marketplace.visualstudio.com/items?itemName=DominicVonk.vscode-resx-editor](https://marketplace.visualstudio.com/items?itemName=DominicVonk.vscode-resx-editor)

### Edit the source

Each `.resx` file is an XML file and can be edited inside a text editor.

ServerMessages and Tips are json files and can be edited in any text editor. VSCode is an example of this.

## Formatting and Verbiage

 - Use commonly known aviation terms where possible. Infinite Flight aims to be accessible without requiring technical language to be learned.

 - Text strings with values such as `{0}` and `{1}` represent variables which are replaced at runtime in the simulator. The comments should explain what these variables represent, but please ask if you are unsure.

 - Translated text should be equal or shorter in length to the English equivalent whenever possible to ensure it will fit in the UI. Please state in the Pull Request if this isn't possible.

 - For ServerMessages, it is important to state the following in the `welcomeMessages`: 
   > Communications with ATC and other pilots is done in English (the official language of aviation)

## Getting started with GitHub 

If you are new to GitHub and don't know where to start, [go here](https://medium.com/@mvthanoshan9/ubuntu-a-beginners-guide-to-git-github-44a2d2fda0b8). You should then [create a GitHub account](https://github.com/signup) if you haven't already, and [fork this repository](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3/) to contribute.

## Pull Request Reviews

Before a new language is added into Infinite Flight, the PR should be reviewed by another speaker of this language to ensure the content is correct.
