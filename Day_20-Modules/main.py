# Python Package Manager

import webbrowser

url_list = [
    'https://python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh'
]

for url in url_list:
    webbrowser.open_new_tab(url)

'''
To uninstall packages
in terminal: pip3 uninstall <packagename>

To show information on a package
in terminal: pip3 show <packagename>

To see the installed packages on the machine
in terminal: pip3 list

pip freeze
~ shows what packages are used
~ should include in a requirements.txt for other developers
'''

