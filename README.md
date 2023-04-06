# Github prebuilt searches
Total searches: `113`

This is a list of prebuilt searches on Github. These searches are useful for finding things on github.

## Table of Contents

* [Code](#code)
    + [Programming Languages](#programming-languages)
        + [C](#c)
        + [C++](#c-1)
        + [Python](#python)
        + [Java](#java)
        + [JavaScript](#javascript)
        + [TypeScript](#typescript)
        + [Rust](#rust)
        + [Go](#go)
        + [PHP](#php)
        + [Ruby](#ruby)
    + [Build Scripts](#build-scripts)
        + [Makefile](#makefile)
        + [CMake](#cmake)
    + [Containers](#containers)
        + [Dockerfile](#dockerfile)
    + [Configuration and Data](#configuration-and-data)
        + [JSON](#json)
        + [YAML](#yaml)
        + [XML](#xml)
        + [TOML](#toml)
        + [INI](#ini)
        + [CSV](#csv)
* [Repositories](#repositories)
* [Issues](#issues)
    + [Open Issues](#open-issues)
    + [Closed Issues](#closed-issues)
    + [Not planned Issues](#not-planned-issues)
* [Pull Requests](#pull-requests)
    + [Open Pull Requests](#open-pull-requests)
    + [Closed Pull Requests](#closed-pull-requests)
* [Packages](#packages)
* [Commits](#commits)

## Code
Here are some searches for code on github.

### Programming Languages

#### C

- `language:c path:*.c` - Find repositories with a C file. [Search](https://github.com/search?q=language%3Ac+path%3A*.c&type=code)

- `language:c path:*.h` - Find repositories with a C header file. [Search](https://github.com/search?q=language%3Ac+path%3A*.h&type=code)

- `language:c path:*.c "#include<stdio.h>"` - Find repositories with a C file that use stdio. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%23include%3Cstdio.h%3E%22&type=code)

- `language:c path:*.c "#include<HEADER>"` - Find repositories with a C file that use a header replace HEADER with the header you want to search for e.g. `#include<math.h>` or `#include<time.h>`

- `language:c path:*.c "int main("` - Find repositories with a C file that use a main function. <a href="https://github.com/search?q=language%3Ac+path%3A*.c+%22int+main(%22&type=code">Search</a>

- `language:c path:*.c "/*<COMMENT>*/" OR "//<COMMENT>"` - Find repositories with a C file that use a comment replace COMMENT with the comment you want to search for e.g. `/*<COMMENT>*/` or `//<COMMENT>`


#### C++

- `language:cpp path:*.cpp` - Find repositories with a C++ file. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp&type=code)

- `language:cpp path:*.h` - Find repositories with a C++ header file. [Search](https://github.com/search?q=language%3Acpp+path%3A*.h&type=code)

- `language:cpp path:*.cpp "#include<iostream>"` - Find repositories with a C++ file that use iostream. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%23include%3Ciostream%3E%22&type=code)

- `language:cpp path:*.cpp "#include<HEADER>"` - Find repositories with a C++ file that use a header replace HEADER with the header you want to search for e.g. `#include<math.h>` or `#include<time.h>`

- `language:cpp path:*.cpp "int main("` - Find repositories with a C++ file that use a main function. <a href="https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22int+main(%22&type=code">Search</a>

- `language:cpp path:*.cpp "/*<COMMENT>*/" OR "//<COMMENT>"` - Find repositories with a C++ file that use a comment replace COMMENT with the comment you want to search for e.g. `/*<COMMENT>*/` or `//<COMMENT>`


#### Python

- `language:python path:*/__main__.py OR language:python path:*/main.py` - Find repositories with a main python file. [Search](https://github.com/search?q=language%3Apython+path%3A*%2F__main__.py+OR+language%3Apython+path%3A*%2Fmain.py&type=code)

- `language:python path:*/__init__.py` - Find repositories with an init file. [Search](https://github.com/search?q=language%3Apython+path%3A*%2F__init__.py&type=code)

- `path:*/requirements.txt` - Find repositories with a requirements file. [Search](https://github.com/search?q=path%3A*%2Frequirements.txt&type=code)

- `path:*/requirements.txt <PACKAGE>` - Find repositories with a requirements file that use a package replace package with the package you want to search for e.g. `requests==` or `flask==`

- `language:python path:*/setup.py` - Find repositories with a setup file

- `path:*/setup.cfg` - Find repositories with a setup config file. [Search](https://github.com/search?q=path%3A*%2Fsetup.cfg&type=code)

- `path:*/pyproject.toml` - Find repositories with a pyproject file. [Search](https://github.com/search?q=path:*/pyproject.toml&type=code)

- `language:python "import <PACKAGE>"` - Find python files that use a package replace package with the package you want to search for e.g. `requests` or `flask`

- `language:python "#<COMMENT>"` - Find python files with a comment replace comment with the comment you want to search for e.g. `#TODO` or `#FIXME`

- `language:python "print(" OR language:python "print ("` - Find python files with a print statement. [Search](https://github.com/search?q=language%3Apython+%22print%28%22+OR+language%3Apython+%22print+%28%22&type=code)


#### Java

- `language:java path:*.java` - Find repositories with a java file. [Search](

- `language:java path:*.java "import "` - Find repositories with a java file that use a import. [Search](https://github.com/search?q=language%3Ajava+path%3A*.java+%22import+%22&type=code)

- `language:java path:*.java "import " <PACKAGE>` - Find repositories with a java file that use a import replace package with the package you want to search for e.g. `java.util` or `java.io`


#### Javascript

- `language:javascript path:*.js` - Find repositories with a javascript file. [Search](https://github.com/search?q=language%3Ajavascript+path%3A*.js&type=code)

- `language:javascript path:*.js "require("` - Find repositories with a javascript file that use a package. [Search](https://github.com/search?q=language%3Ajavascript+path%3A*.js+%22require%28%22&type=code)

- `language:javascript path:*.js "require(" <PACKAGE>` - Find repositories with a javascript file that use a package replace package with the package you want to search for e.g. `express` or `react`

- `language:javascript path:*.js "import "` - Find repositories with a javascript file that use a import. [Search](https://github.com/search?q=language%3Ajavascript+path%3A*.js+%22import+%22&type=code)

- `language:javascript path:*.js "import " <PACKAGE>` - Find repositories with a javascript file that use a import replace package with the package you want to search for e.g. `express` or `react`

- `language:javascript "//<COMMENT>"` - Find repositories with a javascript file that use a comment replace COMMENT with the comment you want to search for e.g. `//<COMMENT>`

- `language:javascript "console.log("` - Find repositories with a javascript file that use a console.log. [Search](https://github.com/search?q=language%3Ajavascript+%22console.log%28%22&type=code)

- `language:javascript "console.warn("` - Find repositories with a javascript file that use a console.warn. [Search](https://github.com/search?q=language%3Ajavascript+%22console.warn%28%22&type=code)

- `language:javascript "console.error("` - Find repositories with a javascript file that use a console.error. [Search](https://github.com/search?q=language%3Ajavascript+%22console.error%28%22&type=code)

- `language:javascript "console.table("` - Find repositories with a javascript file that use a console.table. [Search](https://github.com/search?q=language%3Ajavascript+%22console.table%28%22&type=code)

#### Typescript

- `language:typescript path:*.ts` - Find repositories with a typescript file. [Search](https://github.com/search?q=language%3Atypescript%20path%3A*.ts&type=code)

- `language:typescript path:*.ts "require("` - Find repositories with a typescript file that use a package. [Search](https://github.com/search?q=language%3Atypescript+path%3A*.ts+%22require%28%22&type=code)

- `language:typescript path:*.ts "require(" <PACKAGE>` - Find repositories with a typescript file that use a package replace package with the package you want to search for e.g. `express` or `react`

- `language:typescript "console.log("` - Find repositories with a typescript file that use a console.log. [Search](https://github.com/search?q=language%3Atypescript+%22console.log%28%22&type=code)

- `language:typescript "console.warn("` - Find repositories with a typescript file that use a console.warn. [Search](https://github.com/search?q=language%3Atypescript+%22console.warn%28%22&type=code)

- `language:typescript "console.error("` - Find repositories with a typescript file that use a console.error. [Search](https://github.com/search?q=language%3Atypescript+%22console.error%28%22&type=code)

- `language:typescript "console.table("` - Find repositories with a typescript file that use a console.table. [Search](https://github.com/search?q=language%3Atypescript+%22console.table%28%22&type=code)

#### Rust

- `language:rust "use std::io"` - Find Rust files that use the std::io package. [Search](https://github.com/search?q=language%3Arust+%22use+std%3A%3Aio%22&type=code)

- `language:rust "use <PACKAGE>"` - Find Rust files that use a package. Replace <PACKAGE> with a package name.

- `language:rust "mod"` - Find Rust files that use a module. [Search](https://github.com/search?q=language%3Arust+%22mod%22&type=code)

- `language:rust "mod <MODULE>"` - Find Rust files that use a module. Replace <MODULE> with a package name.

- `language:java path:*.java` - Find repositories with a java file. [Search](

- `language:rust "fn"` - Find Rust files that use a function. [Search](https://github.com/search?q=language%3Arust+%22fn%22&type=code)

- `language:rust "fn <NAME>"` - Find Rust files that use a function. Replace <NAME> with a package name.

#### Go

- `language:go "import ("` - Find Go files that use a import. [Search](https://github.com/search?q=language%3Ago+%22import+%28%22&type=code)

- `language:go "import (<PACKAGE>"` - Find Go files that use a import. Replace <PACKAGE> with a package name.

- `language:go "func"` - Find Go files that use a function. [Search](https://github.com/search?q=language%3Ago+%22func%22&type=code)

- `language:go "func <NAME>"` - Find Go files that use a function with a name of <NAME>. Replace <NAME> with a package name.

- `language:go "// <COMMENT>"` - Find Go files that use a comment. Replace <COMMENT> with a comment.

- `language:go "// TODO:" OR "// BUG:" OR "// FIXME:" OR "// XXX:"` - Find Go files that have a TODO, BUG, FIXME or XXX comment. [Search](https://github.com/search?q=language%3Ago+%22%2F%2F+TODO%3A%22+OR+%22%2F%2F+BUG%3A%22+OR+%22%2F%2F+FIXME%3A%22+OR+%22%2F%2F+XXX%3A%22&type=code)

#### PHP

- `language:PHP` - Find PHP files. [Search](https://github.com/search?q=language%3APHP&type=code)

- `language:PHP "use Monolog"` Find PHP files that use the Monlog package. [Search](https://github.com/search?q=language%3APHP+%22use+Monolog%22&type=code)

- `language:PHP "use <PACKAGE>"` Find PHP files that use a package. Replace <PACKAGE> with a package name.

- `language:PHP "function"` Find PHP files that have a function. [Search](https://github.com/search?q=language%3APHP+%22function%22&type=code)

#### Ruby

- `language:ruby path:*.rb` - Find repositories with a ruby file. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb&type=code)

- `language:ruby path:*.rb "require "` - Find repositories with a ruby file that use a require. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb+%22require+%22&type=code)

- `language:ruby path:*.rb "require " <PACKAGE>` - Find repositories with a ruby file that use a require replace package with the package you want to search for e.g. `express` or `react`

### Build Scripts

#### Makefile

- `language:make path:*/Makefile` - Find repositories with a Makefile. [Search](https://github.com/search?q=language%3Amake+path%3A*%2FMakefile&type=code)

- `path:*/Makefile language:make "= g++"` - Find repositories with a Makefile that use g++. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22%3D+g%2B%2B%22&type=code)

- `path:*/Makefile language:make "= gcc"` - Find repositories with a Makefile that use gcc. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22%3D+gcc%22&type=code)

- `path:*/Makefile language:make "= clang"` - Find repositories with a Makefile that use clang. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22%3D+clang%22&type=code)

- `path:*/Makefile language:make = python3` - Find repositories with a Makefile that use python3. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22+%3D+python3%22&type=code)


#### CMake

- `language:cmake path:*/CMakeLists.txt` - Find repositories with a CMakeLists.txt. [Search](https://github.com/search?q=language%3Acmake+path%3A*%2FCMakeLists.txt&type=code)

- `language:cmake path:*/CMakeLists.txt "find_package("` - Find repositories with a CMakeLists.txt that use a package. [Search](https://github.com/search?q=language%3Acmake+path%3A*%2FCMakeLists.txt+%22find_package%28%22&type=code)

- `language:cmake path:*/CMakeLists.txt "find_package(" <PACKAGE>` - Find repositories with a CMakeLists.txt that use a package replace package with the package you want to search for e.g. `Boost` or `OpenCV`

- `language:cmake path:*/CMakeLists.txt "find_package(Boost"` - Find repositories with a CMakeLists.txt that use Boost. [Search](https://github.com/search?q=language%3Acmake+path%3A*%2FCMakeLists.txt+%22find_package%28Boost%22&type=code)


### Containers

#### Docker

- `language:dockerfile path:*/Dockerfile` - Find repositories with a Dockerfile. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile&type=code)

- `language:dockerfile path:*/Dockerfile FROM <PACKAGE>` - Find repositories with a Dockerfile that use a package replace package with the package you want to search for e.g. `ubuntu:latest` or `gcc:latest`

- `language:dockerfile path:*/Dockerfile FROM ubuntu:` - Find repositories with a Dockerfile that use ubuntu. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+ubuntu%3A&type=code)

- `language:dockerfile path:*/Dockerfile FROM gcc:` - Find repositories with a Dockerfile that use gcc. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+gcc%3A&type=code)

- `language:dockerfile path:*/Dockerfile FROM node:` - Find repositories with a Dockerfile that use node. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+node%3A&type=code)

- `language:dockerfile path:*/Dockerfile FROM python:` - Find repositories with a Dockerfile that use python. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+python%3A&type=code)

### Configuration and Data

#### Json

- `language:json path:*.json` - Find repositories with a json file. [Search](https://github.com/search?q=language%3Ajson+path%3A*.json&type=code)

- `path:.vscode/settings.json` - Find vscode settings files. [Search](https://github.com/search?q=path%3A.vscode%2Fsettings.json&type=code)

- `path:.vscode/launch.json` - Find vscode launch files. [Search](https://github.com/search?q=path%3A.vscode%2Flaunch.json&type=code)

- `path:package.json` - Find package.json files. [Search](https://github.com/search?q=path%3Apackage.json&type=code)


#### YAML

- `language:yaml path:*.yaml` - Find repositories with a yaml file. [Search](https://github.com/search?q=language%3Ayaml+path%3A*.yaml&type=code)

- `path:.github/workflows language:yaml` - find github workflow files. [Search](https://github.com/search?q=path%3A.github%2Fworkflows+language%3Ayaml&type=code)

- `path:.github/workflows language:yaml "uses: actions/checkout@v3"` - find github workflows that use actions/checkout@v3. [Search](https://github.com/search?q=path%3A.github%2Fworkflows+language%3Ayaml+%22uses%3A+actions%2Fcheckout%40v3%22&type=code)

- `path:.github/workflows language:yaml "uses: <PACKAGE>"` - find github workflows that use a package replace package with the package you want to search for e.g. `actions/checkout@v3` or `actions/setup-node@v2`


#### XML

- `language:xml path:*.xml` - Find repositories with a xml file. [Search](

- `language:xml <?xml version="1.0" encoding="UTF-8"?>` - Find repositories with a xml file that has the xml version of 1.0 and a file encoding of UTF-8. [Search](https://github.com/search?q=language%3Axml+%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E&type=code)

#### TOML

- `language:toml path:*.toml` - Find repositories with a toml file. [Search](https://github.com/search?q=language%3Atoml+path%3A*.toml&type=code)

- `language:toml path:*.toml [<SECTION>]` - Find repositories with a toml file that has a section replace section with the section you want to search for e.g. `tool` or `dependencies`

- `language:toml path:*.toml "#"` - Find repositories with a toml file that has a comment. [Search](https://github.com/search?q=language%3Atoml+path%3A*.toml+%22%23%22&type=code)

- `language:toml path:*.toml "# TODO:"` - Find repositories with a toml file that has a todo comment. [Search](https://github.com/search?q=language%3Atoml+path%3A*.toml+%22%23+TODO%3A%22&type=code)

#### INI

- `language:ini path:*.ini` - Find repositories with a ini file. [Search](https://github.com/search?q=language%3Aini+path%3A*.ini&type=code)

- `language:ini path:*.ini [SECTION]` - Find repositories with a ini file that has a section replace section with the section you want to search for e.g. `tool` or `dependencies`

#### CSV

- `language:csv path:*.csv` - Find repositories with a csv file. [Search](https://github.com/search?q=language%3Acsv+path%3A*.csv&type=code)

- `language:csv path:*.csv "<HEADER>"` - Find repositories with a csv file that has a header replace header with the header you want to search for e.g. `name` or `email`

## Repositories

- `language:javascript` - Find repositories that use javascript as its main language. [Search](https://github.com/search?q=language%3AJavaScript+&type=repositories)

- `archived:true` - Find archived repositories. [Search](https://github.com/search?q=+archived%3Atrue&type=repositories)

- `license:gpl` - Find repositories with gpl licence. [Search](https://github.com/search?q=license%3Agpl+&type=repositories)

- `stars:>200` - Find repositories with more that 200 stars. [Search](https://github.com/search?q=stars%3A%3E200&type=repositories)

## Issues

### Open Issues

- `is:open` - Find open issues. [Search](https://github.com/search?q=is%3Aopen&type=issues)

- `is:open found vulnerabilities OR is:open found vulnerability` - Find open issues with the word vulnerabilities. [Search](https://github.com/search?q=is%3Aopen+found+vulnerabilities+OR+is%3Aopen+found+vulnerability&type=issues) 

- `is:open vulnerable package` - Find open issues with the word vulnerable package. [Search](https://github.com/search?q=vulnerable+package&type=issues)

- `is:open found bug OR is:open bug` - Find open issues with the word bug or found bug. [Search](https://github.com/search?q=is%3Aopen+found+bug+OR+is%3Aopen+bug&type=issues)

- `is:open security issue` - Find open issues with the word security issue. [Search](https://github.com/search?q=is%3Aopen+security+issue&type=issues)


### Closed Issues

- `is:closed` - Find closed issues. [Search](https://github.com/search?q=is%3Aclosed&type=issues)

### Not planned Issues

- `reason:"not planned"` - Find issues that are not planned. [Search](https://github.com/search?q=reason%3A%22not+planned%22+&type=issues)

## Pull Requests

### Open Pull Requests

- `is:open` - Find open pull requests. [Search](https://github.com/search?q=is%3Aopen&type=pullrequests)

- `is:open found vulnerabilities OR is:open found vulnerability` - Find open pull requests with the word vulnerabilities. [Search](https://github.com/search?q=is%3Aopen+found+vulnerabilities+OR+is%3Aopen+found+vulnerability&type=pullrequests)

- `is:open vulnerable package` - Find open pull requests with the word vulnerable package. [Search](https://github.com/search?q=is%3Aopen+vulnerable+package&type=pullrequests)

- `is:open found bug OR is:open bug` - Find open pull requests with the word bug or found bug. [Search](https://github.com/search?q=is%3Aopen+found+bug+OR+is%3Aopen+bug&type=pullrequests)

- `is:open security issue` - Find open pull requests with the word security issue. [Search](https://github.com/search?q=is%3Aopen+security+issue&type=pullrequests)

### Closed Pull Requests

- `is:closed` - Find closed pull requests. [Search](https://github.com/search?q=is%3Aclosed&type=pullrequests)

- `is:unmerged is:closed ` - Find unmerged pull requests. [Search](https://github.com/search?q=is%3Aclosed+is%3Aunmerged&type=pullrequests)

- `is:merged is:closed ` - Find merged pull requests. [Search](https://github.com/search?q=is%3Aclosed+is%3Amerged&type=pullrequests)

## Packages

- `package_type:docker` - Find docker packages. [Search](https://github.com/search?q=package_type%3Adocker&type=registrypackages)

- `package_type:npm` - Find gem packages. [Search](https://github.com/search?q=package_type%3Anpm&type=registrypackages)

- `package_type:nuget` - Find nuget packages. [Search](https://github.com/search?q=package_type%3Anuget&type=registrypackages)

- `package_type:rubygems` - Find npm packages. [Search](https://github.com/search?q=package_type%3Arubygems&type=registrypackages)

## Commits

- `"fix" AND "bug"` - Find commits with the word fix and bug. [Search](https://github.com/search?q=%22fix%22+AND+%22bug%22&type=commits)

- `"improvements"` - Find commits with the word improvements. [Search](https://github.com/search?q=%22improvements%22&type=repositories)

- `"patch" AND "vulnerability"` - Find commits with the word patch and vulnerability. [Search](https://github.com/search?q=%22patch%22+AND+%22vulnerability%22&type=commits)

- `"merge pull request"` - Find commits that merge pull requests. [Search](https://github.com/search?q=%22merge+pull+request%22&type=commits)

- `"improve" OR "improvements"` - Find commits with the word improve or improvements. [Search](https://github.com/search?q=%22improve%22+OR+%22improvements%22&type=commits)

- `"fix" OR "fixes" OR "fixed"` - Find commits with the word fix, fixes or fixed. [Search](https://github.com/search?q=%22fix%22+OR+%22fixes%22+OR+%22fixed%22&type=commits)