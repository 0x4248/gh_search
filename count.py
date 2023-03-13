# Gh_search (count.py)
# A list of prebuilt searches on Github.
# Github: https://www.github.com/awesomelewis2007/gh_search
#
# This file adds the total number of searches to the README.md file.

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
