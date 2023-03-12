# This file finds the number of searches and updates the README.md file
# This file is run by a GitHub Action every push to the master branch

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
