# Gh_search (count.py)
# A list of prebuilt searches on Github.
# Github: https://www.github.com/awesomelewis2007/gh_search
# Licence: GNU General Public License v3.0
# By: Lewis Evans
#
# This file adds the total number of searches to the README.md file.
# This file should be ran from the github actions workflow.

if __name__ == "__main__":
    f = open("README.md", "r")
    data = f.read()
    f.close()
    count = data.count("- `")
    f = open("README.md", "r")
    data = f.readlines()
    f.close()
    data[1] = "Total searches: `" + str(count) + "`\n"
    f = open("README.md", "w")
    f.writelines(data)
    f.close()
