# Sphinx Live Preview
Python script for html live preview for sphinx (reStructuredText), including math re-rendering. Should support any platform and any IDE with autosave.

You are welcome to improve and modify the script to suit your needs!

## Step 1
Copy the python script **rst_preview.py** to your sphinx project folder (e.g. created by sphinx-quickstart, see here http://www.sphinx-doc.org/en/1.6/tutorial.html).

For Windows system, you can also copy the **preview.bat** to the folder; it is very simple, just executing the python file. For orther OS, creat yourself such a simple batch command.

## Step 2
Install selenium (https://pypi.org/project/selenium/) for python by

$pip install -U selenium

Go to https://www.seleniumhq.org/download/ to download a driver for your browser, e.g. Google Chrome Driver

## Step 3

Your IDE is better to have the auto save functionailty. For example, Visual Studio Code, add like the following to your workspace settings.

```css
{
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 200,
}
```
