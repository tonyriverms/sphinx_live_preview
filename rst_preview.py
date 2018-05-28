from glob import glob
from os.path import join, realpath, dirname, getsize, getmtime, isfile
from os import pathsep
from subprocess import call
from time import sleep
from selenium import webdriver

# region options for the live preview

path_to_webdriver = "D:/Program Files/webdrivers/chromedriver.exe"
refresh_delay = 0.2
render_math = True

driver = webdriver.Chrome(path_to_webdriver)

# endregion

script_path = dirname(realpath(__file__))
source_path = join(script_path, "source")
source_path_len = len(source_path) + len(pathsep)
build_path = join(script_path, "build", "html")
rst_files = glob(join(script_path, '**/*.rst'), recursive=True)
size_dict = {}
for rst_file in rst_files:
    size_dict[rst_file] = [getsize(rst_file), getmtime(rst_file), 0]

while True:
    for rst_file in rst_files:
        if isfile(rst_file):
            record = size_dict[rst_file]
            new_size = getsize(rst_file)
            new_mtime = getmtime(rst_file)
            if record[0] != new_size or record[1] < new_mtime:
                html_file = join(build_path, rst_file[source_path_len: -4] + ".html")
                call("sphinx-build -M html source build")
                if record[2] == 0:
                    driver.get(html_file)
                else:
                    with open(html_file, 'r', encoding="utf-8") as content_file:
                        content = content_file.read()
                    new_body_start_idx = content.index("<body")
                    new_body_start_idx = content.index(">", new_body_start_idx) + 1
                    content = content[new_body_start_idx:content.rindex("</body>")].strip()
                    driver.execute_script('document.getElementsByTagName("body")[0].innerHTML = arguments[0]', content)
                    if render_math:
                        driver.execute_script('MathJax.Hub.Queue(["Typeset",MathJax.Hub])')

                record[0] = new_size
                record[1] = new_mtime
                record[2] += 1

    sleep(refresh_delay)
