# Sphinx (reStructuredText) Live Preview Script
Python script for html live preview for sphinx (reStructuredText), including math re-rendering. Should support any platform and any IDE (best with autosave).

I see this is badly needed in many places. However, current previews using their own renderers either do not support full-featured sphinx (restview https://github.com/mgedmin/restview), or has other issues (https://www.restructuredtext.net/, currently cannot properly render math, clicking on anchor links breaks preview, only works for VS Code ...).

This one simply monitors file changes, recompile them using sphinx (so full-featured!), and then re-render the page in the browser. You  can use any IDE you like. You are welcome to improve or modify this script!

Help needed: 1) help improve the file monitoring process to reduce unnecessary file checking, like using Watchdog? 2) help make the update more efficient; 3) any other tweaks are welcome!

## Step 1

Copy the python script **rst_preview.py** to your sphinx project root folder (e.g. created by sphinx-quickstart, see here http://www.sphinx-doc.org/en/1.6/tutorial.html).

**NOTE**: for the original script, your project need to have separate folders "build" and "html" to store the source rst files and output HTML files. You are asked to make this choice when going through the sphinx-quickstart command. If you don't like this restriction, you can modify the python script to meet your needs.

For Windows system, you can also copy the **preview.bat** to the folder; it is very simple, just executing the python file. For orther OS, create yourself such a simple batch command.

## Step 2

Install selenium (https://pypi.org/project/selenium/) for python by

>pip install -U selenium

Go to https://www.seleniumhq.org/download/ to download a driver for your browser, e.g. Google Chrome Driver. Put it to any folder you like, and just remember the path.

## Step 3

Your IDE is better to have the **auto save** functionailty (otherwise preview is updated everytime after you save). 200ms delay is recommended, but of course you can adjust this if you wish. For example, **Visual Studio Code**, add like the following to your workspace settings.

```css
{
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 200,
}
```

For **Atom**, install the Autosave Onchange plugin https://atom.io/packages/autosave-onchange. Adjust the delay (in its file lib/autosave-onchange.js) to 200 as well.

## Step 4

Open the script **rst_preview.py**, put in correct browser driver type and path, and adjust other options as you need. Now run the script by simply clicking the batch file (preview.bat on Windows), or manually execute the command in terminal

>python rst_preview.py

A browser will be opened. No need to do anything else. Go to the file you need to edit in the IDE, make changes, the browser will automatically open the page that is under editing, and update it on the fly when change is made!


