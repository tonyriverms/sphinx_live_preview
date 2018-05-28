# Sphinx Live Preview
Python script for html live preview for sphinx (reStructuredText), including math re-rendering. Should support any platform and any IDE with autosave.

This one simply monitors file changes, recompile them using sphinx, and then re-render the page in the browser. You are welcome to improve and modify the script to suit your needs!

## Step 1

Copy the python script **rst_preview.py** to your sphinx project folder (e.g. created by sphinx-quickstart, see here http://www.sphinx-doc.org/en/1.6/tutorial.html).

For Windows system, you can also copy the **preview.bat** to the folder; it is very simple, just executing the python file. For orther OS, creat yourself such a simple batch command.

## Step 2

Install selenium (https://pypi.org/project/selenium/) for python by

$pip install -U selenium

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

$python rst_preview.py

A browser will be opened. No need to do anything else. Go to the file you need to edit in the IDE, make changes, the browser will response accordingly!


