# Github prebuilt searches
Total searches: `324`

This is a list of prebuilt searches on Github. These searches are useful for finding things on github.

## Table of Contents

* [Code](#code)
    + [Programming Languages](#programming-languages)
        + [Assembly](#assembly)
        + [Bash](#bash)
        + [C](#c)
        + [C++](#c-1)
        + [C#](#c-2)
        + [COBOL](#cobol)
        + [CSS](#css)
        + [Dart](#dart)
        + [Elixir](#elixir)
        + [EJS](#ejs)
        + [F#](#f)
        + [Go](#go)
        + [HTML](#html)
        + [Java](#java)
        + [JavaScript](#javascript)
        + [Julia](#julia)
        + [Kotlin](#kotlin)
        + [Lisp](#lisp)
        + [Lua](#lua)
        + [Objective-C](#objective-c)
        + [Perl](#perl)
        + [PHP](#php)
        + [PowerShell](#powershell)
        + [Python](#python)
        + [R](#r)
        + [Ruby](#ruby)
        + [Rust](#rust)
        + [SASS](#sass)
        + [Scala](#scala)
        + [Swift](#swift)
        + [TypeScript](#typescript)
    + [Build Scripts](#build-scripts)
        + [CMake](#cmake)
        + [Gradle](#gradle)
        + [Makefile](#makefile)
        + [Ninja](#ninja)
    + [Containers](#containers)
        + [Dockerfile](#dockerfile)
        + [LXC](#lxc)
    + [Configuration and Data](#configuration-and-data)
        + [CSV](#csv)
        + [INI](#ini)
        + [JSON](#json)
        + [YAML](#yaml)
        + [SQL](#sql)
        + [TOML](#toml)
        + [XML](#xml)
    + [Documentation](#documentation)
        + [AsciiDoc](#asciidoc)
        + [LaTeX](#latex)
        + [Markdown](#markdown)
        + [MediaWiki](#mediawiki)
        + [reStructuredText](#restructuredtext)
        + [Rich Text Format](#rich-text-format)
        + [Text](#text)
    + [Comment Annotations](#comment-annotations)
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

#### Assembly

- `language:assembly path:*.asm` - Find repositories with a Assembly file. [Search](https://github.com/search?q=language%3Aassembly+path%3A*.asm&type=code)

- ` language:assembly path:*.asm ";"` - Find repositories with a Assembly file that have a comment. [Search](https://github.com/search?q=+language%3Aassembly+path%3A*.asm+%22%3B%22&type=code)

#### Bash

- `language:Bash path:*.bash` - Find repositories with a Bash file. [Search](https://github.com/search?q=language%3ABash+path%3A*.bash&type=code)

- `language:Bash path:*.bash "#"` - Find repositories with a Bash file that have a comment. [Search](https://github.com/search?q=language%3ABash+path%3A*.bash+%22%23%22&type=code)

#### C

- `language:c path:*.c` - Find repositories with a C file. [Search](https://github.com/search?q=language%3Ac+path%3A*.c&type=code)

- `language:c path:*.h` - Find repositories with a C header file. [Search](https://github.com/search?q=language%3Ac+path%3A*.h&type=code)

- `language:c path:*.c "#include<stdio.h>"` - Find repositories with a C file that use stdio. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%23include%3Cstdio.h%3E%22&type=code)

- `language:c path:*.c "#include<HEADER>"` - Find repositories with a C file that use a header replace HEADER with the header you want to search for e.g. `#include<math.h>` or `#include<time.h>`

- `language:c path:*.c "int main("` - Find repositories with a C file that use a main function. <a href="https://github.com/search?q=language%3Ac+path%3A*.c+%22int+main(%22&type=code">Search</a>

- `language:c path:*.c "/*<COMMENT>*/" OR "//<COMMENT>"` - Find repositories with a C file that use a comment replace COMMENT with the comment you want to search for e.g. `/*<COMMENT>*/` or `//<COMMENT>`

- `language:c path:*.c "struct"` - Find repositories with a C file that use a struct. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22struct%22&type=code)

- `language:c path:*.c "typedef"` - Find repositories with a C file that use a typedef. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22typedef%22&type=code)

- `language:c path:*.c "if (" OR "if("` - Find repositories with a C file that use an if statement. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22if+%28%22+OR+%22if%28%22&type=code)

- `language:c path:*.c "for (" OR "for("` - Find repositories with a C file that use a for loop. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22for+%28%22+OR+%22for%28%22&type=code)

- `language:c path:*.c "while (" OR "while("` - Find repositories with a C file that use a while loop. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22while+%28%22+OR+%22while%28%22&type=code)

- `language:c path:*.c "switch (" OR "switch("` - Find repositories with a C file that use a switch statement. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22switch+%28%22+OR+%22switch%28%22&type=code)

- `language:c path:*.c "/// <COMMENT>"` - Find repositories with a C file that use a docxygen comment replace COMMENT with the comment you want to search for e.g. `/// <COMMENT>`

- `language:c path:*.c "@param"` - Find repositories with a C file that use a docxygen param. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%40param%22&type=code)

- `language:c path:*.c "@return" OR "@returns"` - Find repositories with a C file that use a docxygen return. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%40return%22+OR+%22%40returns%22&type=code)

- `language:c path:*.c "@brief"` - Find repositories with a C file that use a docxygen brief. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%40brief%22&type=code)

- `language:c path:*.c "@see"` - Find repositories with a C file that use a docxygen see. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%40see%22&type=code)

- `language:c path:*.c "@note"` - Find repositories with a C file that use a docxygen note. [Search](https://github.com/search?q=language%3Ac+path%3A*.c+%22%40note%22&type=code)

#### C++

- `language:cpp path:*.cpp` - Find repositories with a C++ file. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp&type=code)

- `language:cpp path:*.h` - Find repositories with a C++ header file. [Search](https://github.com/search?q=language%3Acpp+path%3A*.h&type=code)

- `language:cpp path:*.cpp "#include<iostream>"` - Find repositories with a C++ file that use iostream. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%23include%3Ciostream%3E%22&type=code)

- `language:cpp path:*.cpp "#include<HEADER>"` - Find repositories with a C++ file that use a header replace HEADER with the header you want to search for e.g. `#include<math.h>` or `#include<time.h>`

- `language:cpp path:*.cpp "int main("` - Find repositories with a C++ file that use a main function. <a href="https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22int+main(%22&type=code">Search</a>

- `language:cpp path:*.cpp "/*<COMMENT>*/" OR "//<COMMENT>"` - Find repositories with a C++ file that use a comment replace COMMENT with the comment you want to search for e.g. `/*<COMMENT>*/` or `//<COMMENT>`

- `language:cpp path:*.cpp "class"` - Find repositories with a C++ file that use a class. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22class%22&type=code)

- `language:cpp path:*.cpp "class <CLASSNAME>"` - Find repositories with a C++ file that use a class replace CLASSNAME with the class you want to search for e.g. `class MyClass` or `class MyClass: public BaseClass`

- `language:cpp path:*.cpp "namespace"` - Find repositories with a C++ file that use a namespace. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22namespace%22&type=code)

- `language:cpp path:*.cpp "namespace <NAMESPACE>"` - Find repositories with a C++ file that use a namespace replace NAMESPACE with the namespace you want to search for e.g. `namespace MyNamespace` or `namespace MyNamespace::MySubNamespace`

- `language:cpp path:*.cpp "using"` - Find repositories with a C++ file that use a using. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22using%22&type=code)

- `language:cpp path:*.cpp "using <NAMESPACE>"` - Find repositories with a C++ file that use a using replace NAMESPACE with the namespace you want to search for e.g. `using MyNamespace` or `using MyNamespace::MySubNamespace`

- `language:cpp path:*.cpp "struct"` - Find repositories with a C++ file that use a struct. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22struct%22&type=code)

- `language:cpp path:*.cpp "typedef"` - Find repositories with a C++ file that use a typedef. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22typedef%22&type=code)

- `language:cpp path:*.cpp "if (" OR "if("` - Find repositories with a C++ file that use an if statement. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22if+%28%22+OR+%22if%28%22&type=code)

- `language:cpp path:*.cpp "for (" OR "for("` - Find repositories with a C++ file that use a for loop. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22for+%28%22+OR+%22for%28%22&type=code)

- `language:cpp path:*.cpp "while (" OR "while("` - Find repositories with a C++ file that use a while loop. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22while+%28%22+OR+%22while%28%22&type=code)

- `language:cpp path:*.cpp "switch (" OR "switch("` - Find repositories with a C++ file that use a switch statement. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22switch+%28%22+OR+%22switch%28%22&type=code)

- `language:cpp path:*.cpp "try {" OR "try{"` - Find repositories with a C++ file that use a try statement. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22try+%7B%22+OR+%22try%7B&type=code)

- `language:cpp path:*.cpp "catch (" OR "catch("` - Find repositories with a C++ file that use a catch statement. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22catch+%28%22+OR+%22catch%28%22&type=code)


- `language:cpp path:*.cpp "/// <COMMENT>"` - Find repositories with a C++ file that use a doxygen comment replace COMMENT with the comment you want to search for e.g. `/// <COMMENT>` or `/** <COMMENT> */`

- `language:cpp path:*.cpp "@param"` - Find repositories with a C++ file that use a doxygen param. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%40param%22&type=code)

- `language:cpp path:*.cpp "@return" OR "@returns"` - Find repositories with a C++ file that use a doxygen return. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%40return%22+OR+%22%40returns%22&type=code)

- `language:cpp path:*.cpp "@brief"` - Find repositories with a C++ file that use a doxygen brief. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%40brief%22&type=code)

- `language:cpp path:*.cpp "@see"` - Find repositories with a C++ file that use a doxygen see. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%40see%22&type=code)

- `language:cpp path:*.cpp "@note"` - Find repositories with a C++ file that use a doxygen note. [Search](https://github.com/search?q=language%3Acpp+path%3A*.cpp+%22%40note%22&type=code)

#### C#

- `language:C#  path:*.cs` - Find repositories with a C# file. [Search](https://github.com/search?q=language%3AC%23++path%3A*.cs&type=code)

- `language:C#  path:*.cs "using System;"` - Find repositories with a C# file that use System. [Search](https://github.com/search?q=language%3AC%23++path%3A*.cs+%22using+System%3B%22&type=code)

- `language:C#  path:*.cs "using <NAMESPACE>;"` - Find repositories with a C# file that use a namespace replace NAMESPACE with the namespace you want to search for e.g. `using System;` or `using System.IO;`

- `language:C#  path:*.cs "class <CLASSNAME>"` - Find repositories with a C# file that use a class replace CLASSNAME with the class you want to search for e.g. `class Program` or `class MyClass`

- `language:C#  path:*.cs "/*<COMMENT>*/" OR "//<COMMENT>"` - Find repositories with a C# file that use a comment replace COMMENT with the comment you want to search for e.g. `/*<COMMENT>*/` or `//<COMMENT>`

- `language:C#  path:*.cs "static void Main"` - Find repositories with a C# main function [Search](https://github.com/search?q=language%3AC%23++path%3A*.cs+%22static+void+Main%22&type=code)

- `language:C#  path:*.cs "// TODO:" OR "/* TODO:"` - Find repositories with a C# file that have a TODO comment [Search](https://github.com/search?q=language%3AC%23++path%3A*.cs+%22%2F%2F+TODO%3A%22+OR+%22%2F*+TODO%3A%22&type=code)

- `language:C#  path:*.cs "///<summary>"` - Find repositories with a C# file that have a summary [Search](https://github.com/search?q=language%3AC%23++path%3A*.cs+%22%2F%2F%2F%3Csummary%3E%22&type=code)

#### COBOL

- `language:COBOL path:*.cbl` - Find repositories with a COBOL file. [Search](https://github.com/search?q=language%3ACOBOL+path%3A*.cbl&type=code)

- `language:COBOL path:*.cbl "*"` - Find repositories with a COBOL file that have a comment. [Search](

#### CSS

- `language:CSS path:*.css` - Find repositories with a CSS file. [Search](https://github.com/search?q=language%3ACSS+path%3A*.css&type=code)

- `language:CSS path:*.css "import "` - Find repositories with a CSS file that have a import. [Search](https://github.com/search?q=language%3ACSS+path%3A*.css+%22import+%22&type=code)

- `language:CSS path:*.css "import " <PACKAGE>` - Find repositories with a CSS file that have a import replace package with the package you want to search for e.g. `package:flutter/material.dart` or `package:provider/provider.dart`

- `language:CSS path:*.css "/*"` - Find repositories with a CSS file that have a comment. [Search](https://github.com/search?q=language%3ACSS+path%3A*.css+%22%2F%2F%22+OR+%22%2F*%22&type=code)

#### Dart

- `language:dart path:*.dart` - Find repositories with a Dart file. [Search](https://github.com/search?q=language%3Adart+path%3A*.dart&type=code)

- `language:dart path:*.dart "import "` - Find repositories with a Dart file that have a import. [Search](https://github.com/search?q=language%3Adart+path%3A*.dart+%22import+%22&type=code)

- `language:dart path:*.dart "import " <PACKAGE>` - Find repositories with a Dart file that have a import replace package with the package you want to search for e.g. `package:flutter/material.dart` or `package:provider/provider.dart`

- `language:dart path:*.dart "//" OR "/*"` - Find repositories with a Dart file that have a comment. [Search](https://github.com/search?q=language%3Adart+path%3A*.dart+%22%2F%2F%22+OR+%22%2F*%22+&type=code)

#### Elixir

- `language:Elixir path:*.ex OR path:*.exs` - Find repositories with a Elixir file. [Search](https://github.com/search?q=language%3AElixir+path%3A*.ex+OR+path%3A*.exs&type=code)

- `language:Elixir path:*.ex OR path:*.exs "import "` - Find repositories with a Elixir file that have a import. [Search](https://github.com/search?q=language%3AElixir+path%3A*.ex+OR+path%3A*.exs+%22import+%22&type=code)

#### EJS

- `language:EJS path:*.ejs` - Find repositories with a EJS file. [Search](https://github.com/search?q=language%3AEJS+path%3A*.ejs&type=code)

- `language:EJS path:*.ejs "<%"` - Find repositories with a EJS file that have a <% . [Search](https://github.com/search?q=language%3AEJS+path%3A*.ejs+%22%3C%25%22&type=code)

#### F#

- `language:F# path:*.fs` - Find repositories with a F# file. [Search](https://github.com/search?q=language%3AF%23+path%3A*.fs&type=code)

- `language:F# path:*.fs "open "` - Find repositories with a F# file that have a open. [Search](https://github.com/search?q=language%3AF%23+path%3A*.fs+%22open+%22&type=code)

- `language:F# path:*.fs "open " <PACKAGE>` - Find repositories with a F# file that have a open replace package with the package you want to search for e.g. `package:flutter/material.dart` or `package:provider/provider.dart`

- `language:F# path:*.fs "//" OR "/*"` - Find repositories with a F# file that have a comment. [Search](https://github.com/search?q=language%3AF%23+path%3A*.fs+%22%2F%2F%22+OR+%22%2F*%22&type=code)

#### Go

- `language:go "import ("` - Find Go files that use a import. [Search](https://github.com/search?q=language%3Ago+%22import+%28%22&type=code)

- `language:go "import (<PACKAGE>"` - Find Go files that use a import. Replace <PACKAGE> with a package name.

- `language:go "func"` - Find Go files that use a function. [Search](https://github.com/search?q=language%3Ago+%22func%22&type=code)

- `language:go "func <NAME>"` - Find Go files that use a function with a name of <NAME>. Replace <NAME> with a package name.

- `language:go "// <COMMENT>"` - Find Go files that use a comment. Replace <COMMENT> with a comment.

- `language:go "// TODO:" OR "// BUG:" OR "// FIXME:" OR "// XXX:"` - Find Go files that have a TODO, BUG, FIXME or XXX comment. [Search](https://github.com/search?q=language%3Ago+%22%2F%2F+TODO%3A%22+OR+%22%2F%2F+BUG%3A%22+OR+%22%2F%2F+FIXME%3A%22+OR+%22%2F%2F+XXX%3A%22&type=code)

#### HTML

- `language:HTML path:*.html` - Find repositories with a HTML file. [Search](https://github.com/search?q=language%3AHTML+path%3A*.html&type=code)

- `language:HTML path:*.html "<script"` - Find repositories with a HTML file that have a script tag. [Search](https://github.com/search?q=language%3AHTML+path%3A*.html+%22%3Cscript%22&type=code)

- `language:HTML path:*.html "<css"` - Find repositories with a HTML file that have a css tag. [Search](https://github.com/search?q=language%3AHTML+path%3A*.html+%22%3Ccss%22&type=code)

- `language:HTML path:*.html "<meta"` - Find repositories with a HTML file that have a meta tag. [Search](https://github.com/search?q=language%3AHTML+path%3A*.html+%22%3Cmeta%22&type=code)

#### Java

- `language:java path:*.java` - Find repositories with a java file. [Search](https://github.com/search?q=language%3Ajava+path%3A*.java&type=code)

- `language:java path:*.java "import "` - Find repositories with a java file that use a import. [Search](https://github.com/search?q=language%3Ajava+path%3A*.java+%22import+%22&type=code)

- `language:java path:*.java "import " <PACKAGE>` - Find repositories with a java file that use a import replace package with the package you want to search for e.g. `java.util` or `java.io`

- `language:java path:*.java "public class"` - Find repositories with a java file that use a class. [Search](https://github.com/search?q=language%3Ajava+path%3A*.java+%22public+class%22&type=code)

#### Javascript

- `language:javascript path:*.js` - Find repositories with a javascript file. [Search](https://github.com/search?q=language%3Ajavascript+path%3A*.js&type=code)

- `language:javascript path:*.js "require("` - Find repositories with a javascript file that use a package. [Search](https://github.com/search?q=language%3Ajavascript+path%3A*.js+%22require%28%22&type=code)

- `language:javascript path:*.js "require(" <PACKAGE>` - Find repositories with a javascript file that use a package replace package with the package you want to search for e.g. `express` or `react`

- `language:javascript path:*.js "import "` - Find repositories with a javascript file that use a import. [Search](https://github.com/search?q=language%3Ajavascript+path%3A*.js+%22import+%22&type=code)

- `language:javascript path:*.js "import " <PACKAGE>` - Find repositories with a javascript file that use a import replace package with the package you want to search for e.g. `express` or `react`

- `language:javascript "//<COMMENT>"` - Find repositories with a javascript file that use a comment replace COMMENT with the comment you want to search for.

- `language:javascript "console.log("` - Find repositories with a javascript file that use a console.log. [Search](https://github.com/search?q=language%3Ajavascript+%22console.log%28%22&type=code)

- `language:javascript "console.warn("` - Find repositories with a javascript file that use a console.warn. [Search](https://github.com/search?q=language%3Ajavascript+%22console.warn%28%22&type=code)

- `language:javascript "console.error("` - Find repositories with a javascript file that use a console.error. [Search](https://github.com/search?q=language%3Ajavascript+%22console.error%28%22&type=code)

- `language:javascript "console.table("` - Find repositories with a javascript file that use a console.table. [Search](https://github.com/search?q=language%3Ajavascript+%22console.table%28%22&type=code)

- `language:javascript "function "` - Find repositories with a javascript file that have a function. [Search](https://github.com/search?q=language%3Ajavascript+%22function+%22&type=code)

- `language:javascript "function " <FUNCTION>` - Find repositories with a javascript file that have a function replace FUNCTION with the function you want to search for.

- `language:javascript "async function "` - Find repositories with a javascript file that have a asynconous function. [Search](https://github.com/search?q=language%3Ajavascript+%22async+function+%22&type=code)

- `language:javascript "async function " <FUNCTION>` - Find repositories with a javascript file that have a asynconous function replace FUNCTION with the function you want to search for e.g. `async function <FUNCTION>`

- `language:javascript "let "` - Find javascript files that use a let statement. [Search](https://github.com/search?q=language%3Ajavascript+%22let+%22&type=code)

- `language:javascript "let " <VARIABLE>` - Find javascript files that use a let statement replace VARIABLE with the variable you want to search for.

- `language:javascript "const "`- Find javascript files that use a const statement. [Search](https://github.com/search?q=language%3Ajavascript+%22const+%22&type=code)

- `language:javascript "var "` - Find javascript files that use a var statement. [Search](https://github.com/search?q=language%3Ajavascript+%22var+%22&type=code)

- `language:javascript "var " <VARIABLE>` - Find javascript files that use a var statement replace VARIABLE with the variable you want to search for.

- `language:javascript "if("` - Find javascript files that use a if statement. [Search](https://github.com/search?q=language%3Ajavascript+%22if%28%22&type=code)

- `language:javascript "if(" <CONDITION>` - Find javascript files that use a if statement replace CONDITION with the condition you want to search for.

- `language:javascript "for("` - Find javascript files that use a for statement. [Search](https://github.com/search?q=language%3Ajavascript+%22for%28%22&type=code)

- `language:javascript "for(" <CONDITION>` - Find javascript files that use a for statement replace CONDITION with the condition you want to search for.

- `language:javascript "while("` - Find javascript files that use a while statement. [Search](https://github.com/search?q=language%3Ajavascript+%22while%28%22&type=code)

- `language:javascript "while(" <CONDITION>` - Find javascript files that use a while statement replace CONDITION with the condition you want to search for.

#### Julia

- `language:Julia path:*.jl` - Find repositories with a Julia file. [Search](https://github.com/search?q=language%3AJulia+path%3A*.jl&type=code)

- `language:Julia path:*.jl "#"` - Find repositories with a Julia file that have a comment. [Search](https://github.com/search?q=language%3AJulia+path%3A*.jl+%22%23%22&type=code)

- `language:Julia path:*.jl "using"` - Find repositories with a Julia file that have a using. [Search](https://github.com/search?q=Language%3AJulia+path%3A*.jl+%22using%22&type=code)

- `language:Julia path:*.jl "using " <PACKAGE>` - Find repositories with a Julia file that have a using replace package with the package you want to search for.

- `language:Julia path:*.jl "import"` - Find repositories with a Julia file that have a import. [Search](https://github.com/search?q=language%3AJulia+path%3A*.jl+%22import%22&type=code)

- `language:Julia path:*.jl "import " <PACKAGE>` - Find repositories with a Julia file that have a import replace package with the package you want to search for.

#### Kotlin

- `language:kotlin path:*.kt` - Find repositories with a Kotlin file. [Search](https://github.com/search?q=language%3Akotlin+path%3A*.kt&type=code)

- `language:kotlin path:*.kt "import "` - Find repositories with a Kotlin file that have a import. [Search](https://github.com/search?q=language%3Akotlin+path%3A*.kt+%22import+%22&type=code)

- `language:kotlin path:*.kt "import " <PACKAGE>` - Find repositories with a Kotlin file that have a import replace package with the package you want to search for e.g. `androidx.appcompat.app.AppCompatActivity` or `androidx.recyclerview.widget.RecyclerView`

- `language:kotlin path:*.kt "fun"` - Find repositories with a Kotlin file that have a function. [Search](https://github.com/search?q=language%3Akotlin+path%3A*.kt+%22fun%22&type=code)

- `language:kotlin path:*.kt "fun " <NAME>` - Find repositories with a Kotlin file that have a function with a name of <NAME>. Replace <NAME> with a package name.

- `language:kotlin path:*.kt "// <COMMENT>"` - Find repositories with a Kotlin file that have a comment. Replace <COMMENT> with a comment.

##### Lisp

- `language:Lisp path:*.lisp` - Find repositories with a Lisp file. [Search](https://github.com/search?q=language%3ALisp+path%3A*.lisp&type=code)

- `language:Lisp path:*.lisp ";"` - Find repositories with a Lisp file that have a comment. [Search](https://github.com/search?q=language%3ALisp+path%3A*.lisp+%22%3B%22&type=code)

#### Lua

- `language:Lua path:*.lua` - Find repositories with a Lua file. [Search](https://github.com/search?q=language%3ALua+path%3A*.lua&type=code)

- `language:Lua path:*.lua "--"` - Find repositories with a Lua file that have a comment. [Search](https://github.com/search?q=language%3ALua+path%3A*.lua+%22--%22&type=code)

- `language:Lua path:*.lua "require "` - Find repositories with a Lua file that have a require. [Search](https://github.com/search?q=language%3ALua+path%3A*.lua+%22require+%22&type=code)

- `language:Lua path:*.lua "require " <PACKAGE>` - Find repositories with a Lua file that have a require replace package with the package you want to search for.

#### Objective-C

- `language:objective-c path:*.m` - Find repositories with a Objective-C file. [Search](https://github.com/search?q=language%3Aobjective-c+path%3A*.m&type=code)

- `language:objective-c path:*.h` - Find repositories with a Objective-C header file. [Search](https://github.com/search?q=language%3Aobjective-c+path%3A*.h&type=code)

- `language:objective-c path:*.m "typedef struct"` - Find repositories with a Objective-C file that use a struct. [Search](https://github.com/search?q=language%3Aobjective-c+path%3A*.m+%22typedef+struct%22&type=code)

- `language:objective-c path:*.m "#import <HEADER>"` - Find repositories with a Objective-C file that use a header replace HEADER with the header you want to search for e.g. `#import <Foundation/Foundation.h>` or `#import <UIKit/UIKit.h>`

- `language:objective-c path:*.m "int main("` - Find repositories with a Objective-C file that use a main function. [Search](https://github.com/search?q=language%3Aobjective-c+path%3A*.m+%22int+main%28%22&type=code)

- `language:objective-c path:*.m "/*<COMMENT>*/" OR "//<COMMENT>"` - Find repositories with a Objective-C file that use a comment replace COMMENT with the comment you want to search for e.g. `/*<COMMENT>*/` or `//<COMMENT>`

#### Perl

- `language:Perl path:*.pl` - Find repositories with a Perl file. [Search](https://github.com/search?q=language%3APerl+path%3A*.pl&type=code)

- `language:Perl path:*.pl "#"` - Find repositories with a Perl file that have a comment. [Search](https://github.com/search?q=language%3APerl+path%3A*.pl+%22%23%22&type=code)

- `language:Perl path:*.pl "use"` - Find repositories with a Perl file that have a use. [Search](https://github.com/search?q=language%3APerl+path%3A*.pl+%22use%22&type=code)

- `language:Perl path:*.pl "use " <MODULE>` - Find repositories with a Perl file that have a use replace module with the package you want to search for.

#### PHP

- `language:PHP` - Find PHP files. [Search](https://github.com/search?q=language%3APHP&type=code)

- `language:PHP "use Monolog"` Find PHP files that use the Monlog package. [Search](https://github.com/search?q=language%3APHP+%22use+Monolog%22&type=code)

- `language:PHP "use <PACKAGE>"` Find PHP files that use a package. Replace <PACKAGE> with a package name.

- `language:PHP "function"` Find PHP files that have a function. [Search](https://github.com/search?q=language%3APHP+%22function%22&type=code)

#### PowerShell

- `language:PowerShell path:*.ps1` - Find repositories with a PowerShell file. [Search](https://github.com/search?q=language%3APowerShell+path%3A*.ps1&type=code)

- `language:PowerShell path:*.ps1 "#"` - Find repositories with a PowerShell file that have a comment. [Search](https://github.com/search?q=language%3APowerShell+path%3A*.ps1+%22%23%22&type=code)

- `language:PowerShell path:*.ps1 "Import-Module "` - Find repositories with a PowerShell file that have a Import-Module. [Search](https://github.com/search?q=language%3APowerShell+path%3A*.ps1+%22Import-Module+%22&type=code)

- `language:PowerShell path:*.ps1 "Import-Module " <PACKAGE>` - Find repositories with a PowerShell file that have a Import-Module replace package with the package you want to search for.


#### Python

- `language:python path:*/__main__.py OR language:python path:*/main.py` - Find repositories with a main python file. [Search](https://github.com/search?q=language%3Apython+path%3A*%2F__main__.py+OR+language%3Apython+path%3A*%2Fmain.py&type=code)

- `language:python path:*/__init__.py` - Find repositories with an init file. [Search](https://github.com/search?q=language%3Apython+path%3A*%2F__init__.py&type=code)

- `path:*/requirements.txt` - Find repositories with a requirements file. [Search](https://github.com/search?q=path%3A*%2Frequirements.txt&type=code)

- `path:*/requirements.txt <PACKAGE>` - Find repositories with a requirements file that use a package replace package with the package you want to search for e.g. `requests==` or `flask==`

- `language:python path:*/setup.py` - Find repositories with a setup file [Search](https://github.com/search?q=language%3Apython+path%3A*%2Fsetup.py&type=code)

- `path:*/setup.cfg` - Find repositories with a setup config file. [Search](https://github.com/search?q=path%3A*%2Fsetup.cfg&type=code)

- `path:*/pyproject.toml` - Find repositories with a pyproject file. [Search](https://github.com/search?q=path:*/pyproject.toml&type=code)

- `language:python "import <PACKAGE>"` - Find python files that use a package replace package with the package you want to search for e.g. `requests` or `flask`

- `language:python "print(" OR language:python "print ("` - Find python files with a print statement. [Search](https://github.com/search?q=language%3Apython+%22print%28%22+OR+language%3Apython+%22print+%28%22&type=code)

- `language:python "def "` - Find python files with a function. [Search](https://github.com/search?q=language%3Apython+%22def+%22&type=code)

- `language:python "class "` - Find python files with a class. [Search](https://github.com/search?q=language%3Apython+%22class+%22&type=code)

#### R

- `language:R path:*.R` - Find repositories with a R file. [Search](https://github.com/search?q=language%3AR+path%3A*.R&type=code)

- `language:R path:*.R "#"` - Find repositories with a R file that have a comment. [Search](https://github.com/search?q=language%3AR%20path%3A*.R%20%22%23%22&type=code)

#### Ruby

- `language:ruby path:*.rb` - Find repositories with a ruby file. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb&type=code)

- `language:ruby path:*.rb "require "` - Find repositories with a ruby file that use a require. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb+%22require+%22&type=code)

- `language:ruby path:*.rb "require " <PACKAGE>` - Find repositories with a ruby file that use a require replace package with the package you want to search for e.g. `express` or `react`

- `language:ruby path:*.rb "puts "` - Find repositories with a ruby file that use a puts. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb+%22puts+%22&type=code)

- `language:ruby path:*.rb "print "` - Find repositories with a ruby file that use a print. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb+%22print+%22&type=code)

- `language:ruby path:Gemfile` - Find repositories with a Gemfile. [Search](https://github.com/search?q=language%3Aruby+path%3AGemfile&type=code)

- `language:ruby path:*.rb "def "` - Find repositories with a ruby file that use a def. [Search](https://github.com/search?q=language%3Aruby+path%3A*.rb+%22def+%22&type=code)

- `language:ruby path:*.rb "def <NAME>"` - Find repositories with a ruby file that use a def with a name of <NAME>. Replace <NAME> with a package name.

#### Rust

- `language:rust "use std::io"` - Find Rust files that use the std::io package. [Search](https://github.com/search?q=language%3Arust+%22use+std%3A%3Aio%22&type=code)

- `language:rust "use <PACKAGE>"` - Find Rust files that use a package. Replace <PACKAGE> with a package name.

- `language:rust "mod"` - Find Rust files that use a module. [Search](https://github.com/search?q=language%3Arust+%22mod%22&type=code)

- `language:rust "mod <MODULE>"` - Find Rust files that use a module. Replace <MODULE> with a package name.

- `language:java path:*.java` - Find repositories with a java file. [Search](

- `language:rust "fn"` - Find Rust files that use a function. [Search](https://github.com/search?q=language%3Arust+%22fn%22&type=code)

- `language:rust "fn <NAME>"` - Find Rust files that use a function. Replace <NAME> with a package name.

#### SASS

- `language:SASS path:*.sass` - Find repositories with a SASS file. [Search](https://github.com/search?q=language%3ASASS+path%3A*.sass&type=code)

- `language:SASS path:*.sass "import "` - Find repositories with a SASS file that have a import. [Search](https://github.com/search?q=language%3ASASS+path%3A*.sass+%22import+%22&type=code)

- `language:SASS path:*.sass "import " <PACKAGE>` - Find repositories with a SASS file that have a import replace package with the package you want to search for e.g. `package:flutter/material.dart` or `package:provider/provider.dart`

- `language:SASS path:*.sass "/*"` - Find repositories with a SASS file that have a comment. [Search](https://github.com/search?q=language%3ASASS+path%3A*.sass+%22%2F*%22&type=code)

#### Scala

- `language:Scala path:*.scala` - Find repositories with a Scala file. [Search](https://github.com/search?q=language%3AScala+path%3A*.scala&type=code)

- `language:Scala path:*.scala "import "` - Find repositories with a Scala file that have a import. [Search](https://github.com/search?q=language%3AScala+path%3A*.scala+%22import+%22&type=code)

- `language:Scala path:*.scala "import " <PACKAGE>` - Find repositories with a Scala file that have a import replace package with the package you want to search for.

- `language:Scala path:*.scala "//" OR "/*"` - Find repositories with a Scala file that have a comment. [Search](https://github.com/search?q=language%3AScala+path%3A*.scala+%22%2F%2F%22+OR+%22%2F*%22&type=code)

#### Swift

- `language:swift path:*.swift` - Find repositories with a Swift file. [Search](https://github.com/search?q=language%3Aswift+path%3A*.swift&type=code)

- `language:swift path:*.swift "import "` - Find repositories with a Swift file that have a import. [Search](https://github.com/search?q=language%3Aswift+path%3A*.swift+%22import+%22&type=code)

- `language:swift path:*.swift "import " <PACKAGE>` - Find repositories with a Swift file that have a import replace package with the package you want to search for e.g. `UIKit` or `Foundation`

- `language:swift path:*.swift "func"` - Find repositories with a Swift file that have a function. [Search](https://github.com/search?q=language%3Aswift+path%3A*.swift+%22func%22&type=code)

- `language:swift path:*.swift "func " <NAME>` - Find repositories with a Swift file that have a function with a name of <NAME>. Replace <NAME> with a package name.

- `language:swift path:*.swift "// <COMMENT>"` - Find repositories with a Swift file that have a comment. Replace <COMMENT> with a comment.


#### Typescript

- `language:typescript path:*.ts` - Find repositories with a typescript file. [Search](https://github.com/search?q=language%3Atypescript%20path%3A*.ts&type=code)

- `language:typescript path:*.ts "require("` - Find repositories with a typescript file that use a package. [Search](https://github.com/search?q=language%3Atypescript+path%3A*.ts+%22require%28%22&type=code)

- `language:typescript path:*.ts "require(" <PACKAGE>` - Find repositories with a typescript file that use a package replace package with the package you want to search for e.g. `express` or `react`

- `language:typescript "console.log("` - Find repositories with a typescript file that use a console.log. [Search](https://github.com/search?q=language%3Atypescript+%22console.log%28%22&type=code)

- `language:typescript "console.warn("` - Find repositories with a typescript file that use a console.warn. [Search](https://github.com/search?q=language%3Atypescript+%22console.warn%28%22&type=code)

- `language:typescript "console.error("` - Find repositories with a typescript file that use a console.error. [Search](https://github.com/search?q=language%3Atypescript+%22console.error%28%22&type=code)

- `language:typescript "console.table("` - Find repositories with a typescript file that use a console.table. [Search](https://github.com/search?q=language%3Atypescript+%22console.table%28%22&type=code)

- `language:typescript "function "` - Find repositories with a typescript file that have a function. [Search](https://github.com/search?q=language%3Atypescript+%22function+%22&type=code)

- `language:typescript "function " <FUNCTION>` - Find repositories with a typescript file that have a function replace FUNCTION with the function you want to search for e.g. `function <FUNCTION>`

- `language:typescript "async function "` - Find repositories with a typescript file that have a asynconous function. [Search](https://github.com/search?q=language%3Atypescript+%22async+function+%22&type=code)

- `language:typescript "async function " <FUNCTION>` - Find repositories with a typescript file that have a asynconous function replace FUNCTION with the function you want to search for e.g. `async function <FUNCTION>`

- `language:typescript "let "` - Find typescript files that use a let statement. [Search](https://github.com/search?q=language%3Atypescript+%22let+%22&type=code)

- `language:typescript "let " <VARIABLE>` - Find typescript files that use a let statement replace VARIABLE with the variable you want to search for.

- `language:typescript "const "`- Find typescript files that use a const statement. [Search](https://github.com/search?q=language%3Atypescript+%22const+%22&type=code)

- `language:typescript "var "` - Find typescript files that use a var statement. [Search](https://github.com/search?q=language%3Atypescript+%22var+%22&type=code)

- `language:typescript "var " <VARIABLE>` - Find typescript files that use a var statement replace VARIABLE with the variable you want to search for.

- `language:typescript "if("` - Find typescript files that use a if statement. [Search](https://github.com/search?q=language%3Atypescript+%22if%28%22&type=code)

- `language:typescript "if(" <CONDITION>` - Find typescript files that use a if statement replace CONDITION with the condition you want to search for.


### Build Scripts

#### CMake

- `language:cmake path:*/CMakeLists.txt` - Find repositories with a CMakeLists.txt. [Search](https://github.com/search?q=language%3Acmake+path%3A*%2FCMakeLists.txt&type=code)

- `language:cmake path:*/CMakeLists.txt "find_package("` - Find repositories with a CMakeLists.txt that use a package. [Search](https://github.com/search?q=language%3Acmake+path%3A*%2FCMakeLists.txt+%22find_package%28%22&type=code)

- `language:cmake path:*/CMakeLists.txt "find_package(" <PACKAGE>` - Find repositories with a CMakeLists.txt that use a package replace package with the package you want to search for e.g. `Boost` or `OpenCV`

- `language:cmake path:*/CMakeLists.txt "find_package(Boost"` - Find repositories with a CMakeLists.txt that use Boost. [Search](https://github.com/search?q=language%3Acmake+path%3A*%2FCMakeLists.txt+%22find_package%28Boost%22&type=code)

#### Gradle

- `path:*.gradle` - Find repositories with a gradle file. [Search](https://github.com/search?q=path%3A*.gradle&type=code)

- `path:*.gradle "implementation"` - Find repositories with a gradle file that use a package. [Search](https://github.com/search?q=path%3A*.gradle+%22implementation%22&type=code)

- `path:*.gradle "implementation" <PACKAGE>` - Find repositories with a gradle file that use a package replace package with the package you want to search for e.g. `com.google.android.material:material` or `androidx.appcompat:appcompat`

- `path:*.gradle "plugins {"` - Find repositories with a gradle file that use a plugin. [Search](https://github.com/search?q=path%3A*.gradle+%22plugins+%7B%22&type=code)

#### Makefile

- `language:make path:*/Makefile` - Find repositories with a Makefile. [Search](https://github.com/search?q=language%3Amake+path%3A*%2FMakefile&type=code)

- `path:*/Makefile language:make "= g++"` - Find repositories with a Makefile that use g++. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22%3D+g%2B%2B%22&type=code)

- `path:*/Makefile language:make "= gcc"` - Find repositories with a Makefile that use gcc. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22%3D+gcc%22&type=code)

- `path:*/Makefile language:make "= clang"` - Find repositories with a Makefile that use clang. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22%3D+clang%22&type=code)

- `path:*/Makefile language:make = python3` - Find repositories with a Makefile that use python3. [Search](https://github.com/search?q=path%3A*%2FMakefile+language%3Amake+%22+%3D+python3%22&type=code)

#### Ninja

- `path:*.ninja` - Find repositories with a ninja file. [Search](https://github.com/search?q=path%3A*.ninja&type=code)

- `path:*.ninja "rule "` - Find repositories with a ninja file that use a rule. [Search](https://github.com/search?q=path%3A*.ninja+%22rule+%22&type=code)

### Containers

#### Docker

- `language:dockerfile path:*/Dockerfile` - Find repositories with a Dockerfile. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile&type=code)

- `language:dockerfile path:*/Dockerfile FROM <PACKAGE>` - Find repositories with a Dockerfile that use a package replace package with the package you want to search for e.g. `ubuntu:latest` or `gcc:latest`

- `language:dockerfile path:*/Dockerfile FROM ubuntu:` - Find repositories with a Dockerfile that use ubuntu. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+ubuntu%3A&type=code)

- `language:dockerfile path:*/Dockerfile FROM gcc:` - Find repositories with a Dockerfile that use gcc. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+gcc%3A&type=code)

- `language:dockerfile path:*/Dockerfile FROM node:` - Find repositories with a Dockerfile that use node. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+node%3A&type=code)

- `language:dockerfile path:*/Dockerfile FROM python:` - Find repositories with a Dockerfile that use python. [Search](https://github.com/search?q=language%3Adockerfile+path%3A*%2FDockerfile+FROM+python%3A&type=code)


#### LXC

- `path:*.in "lxc" NOT language:markdown` - Find repositories with a lxc file. [Search](https://github.com/search?q=path:*.in++%22lxc%22+NOT+language:markdown&type=code)

- `path:*.in "lxc" "#" NOT language:markdown` - Find repositories with a lxc file that use a comment. [Search](https://github.com/search?q=path%3A*.in+%22lxc%22+%22%23%22+NOT+language%3Amarkdown&type=code)

### Configuration and Data

#### CSV

- `language:csv path:*.csv` - Find repositories with a csv file. [Search](https://github.com/search?q=language%3Acsv+path%3A*.csv&type=code)

- `language:csv path:*.csv "<HEADER>"` - Find repositories with a csv file that has a header replace header with the header you want to search for e.g. `name` or `email`

#### INI

- `language:ini path:*.ini` - Find repositories with a ini file. [Search](https://github.com/search?q=language%3Aini+path%3A*.ini&type=code)

- `language:ini path:*.ini [SECTION]` - Find repositories with a ini file that has a section replace section with the section you want to search for e.g. `tool` or `dependencies`

#### JSON

- `language:json path:*.json` - Find repositories with a json file. [Search](https://github.com/search?q=language%3Ajson+path%3A*.json&type=code)

- `path:.vscode/settings.json` - Find vscode settings files. [Search](https://github.com/search?q=path%3A.vscode%2Fsettings.json&type=code)

- `path:.vscode/launch.json` - Find vscode launch files. [Search](https://github.com/search?q=path%3A.vscode%2Flaunch.json&type=code)

- `path:package.json` - Find package.json files. [Search](https://github.com/search?q=path%3Apackage.json&type=code)

- `language:json path:*.eslintrc` - Find eslint config files. [Search](https://github.com/search?q=language%3Ajson+path%3A*.eslintrc&type=code)

- `language:json path:*.babelrc` - Find repositories with a Babel configuration file in JSON format. [Search](https://github.com/search?q=language%3Ajson+path%3A*.babelrc&type=code)

- `language:json path:*.prettierrc` - Find repositories with a Prettier configuration file in JSON format. [Search](https://github.com/search?q=language%3Ajson+path%3A*.prettierrc&type=code)

- `language:json path:*.tsconfig.json` - Find repositories with a TypeScript configuration file in JSON format. [Search](https://github.com/search?q=language%3Ajson+path%3A*.tsconfig.json&type=code)

#### YAML

- `language:yaml path:*.yaml` - Find repositories with a yaml file. [Search](https://github.com/search?q=language%3Ayaml+path%3A*.yaml&type=code)

- `path:.github/workflows language:yaml` - find github workflow files. [Search](https://github.com/search?q=path%3A.github%2Fworkflows+language%3Ayaml&type=code)

- `path:.github/workflows language:yaml "uses: actions/checkout@v3"` - find github workflows that use actions/checkout@v3. [Search](https://github.com/search?q=path%3A.github%2Fworkflows+language%3Ayaml+%22uses%3A+actions%2Fcheckout%40v3%22&type=code)

- `path:.github/workflows language:yaml "uses: <PACKAGE>"` - find github workflows that use a package replace package with the package you want to search for e.g. `actions/checkout@v3` or `actions/setup-node@v2`

#### SQL

- `language:sql path:*.sql` - Find repositories with a sql file. [Search](https://github.com/search?q=language%3Asql+path%3A*.sql&type=code)

- `language:sql path:*.sql "SELECT"` - Find repositories with a sql file that has a select statement. [Search](https://github.com/search?q=language%3Asql+path%3A*.sql+%22SELECT%22&type=code)

- `language:sql path:*.sql "SELECT" "FROM"` - Find repositories with a sql file that has a select statement and a from statement. [Search](https://github.com/search?q=language%3Asql+path%3A*.sql+%22SELECT%22+%22FROM%22&type=code)

- `language:sql path:*.sql "SELECT *"` - Find repositories with a sql file that has a select * statement. [Search](https://github.com/search?q=language%3Asql+path%3A*.sql+%22SELECT+*%22&type=code)

#### TOML

- `language:toml path:*.toml` - Find repositories with a toml file. [Search](https://github.com/search?q=language%3Atoml+path%3A*.toml&type=code)

- `language:toml path:*.toml [<SECTION>]` - Find repositories with a toml file that has a section replace section with the section you want to search for e.g. `tool` or `dependencies`

- `language:toml path:*.toml "#"` - Find repositories with a toml file that has a comment. [Search](https://github.com/search?q=language%3Atoml+path%3A*.toml+%22%23%22&type=code)

- `language:toml path:*.toml "# TODO:"` - Find repositories with a toml file that has a todo comment. [Search](https://github.com/search?q=language%3Atoml+path%3A*.toml+%22%23+TODO%3A%22&type=code)

#### XML

- `language:xml path:*.xml` - Find repositories with a xml file. [Search](https://github.com/search?q=language%3Axml+path%3A*.xml&type=code)

- `language:xml <?xml version="1.0" encoding="UTF-8"?>` - Find repositories with a xml file that has the xml version of 1.0 and a file encoding of UTF-8. [Search](https://github.com/search?q=language%3Axml+%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E&type=code)

### Documentation

#### AsciiDoc

- `language:asciidoc path:*.adoc` - Find repositories with a asciidoc file. [Search](https://github.com/search?q=language%3Aasciidoc+path%3A*.adoc&type=code)

- `language:asciidoc path:README.adoc` - Find repositories with a readme file. [Search](https://github.com/search?q=language%3Aasciidoc+path%3AREADME.adoc&type=code)

-`language:asciidoc path:LICENSE.adoc` - Find repositories with a license file. [Search](https://github.com/search?q=language%3Aasciidoc+path%3ALICENSE.adoc&type=code)

- `language:asciidoc path:CHANGELOG.adoc` - Find repositories with a changelog file. [Search](https://github.com/search?q=language%3Aasciidoc+path%3ACHANGELOG.adoc&type=code)

#### LaTeX

- `language:tex path:*.tex` - Find repositories with a tex file. [Search](https://github.com/search?q=language%3Atex+path%3A*.tex&type=code)

- `language:tex path:*.tex "documentclass"` - Find repositories with a tex file that has a documentclass. [Search](https://github.com/search?q=language%3Atex+path%3A*.tex+%22documentclass%22&type=code)

#### Markdown

- `language:markdown path:*.md` - Find repositories with a markdown file. [Search](https://github.com/search?q=language%3Amarkdown+path%3A*.md&type=code)

- `language:markdown path:README.md` - Find repositories with a readme file. [Search](https://github.com/search?q=language%3Amarkdown+path%3AREADME.md&type=code)

- `language:markdown path:LICENSE.md` - Find repositories with a license file. [Search](https://github.com/search?q=language%3Amarkdown+path%3ALICENSE.md&type=code)

- `language:markdown path:CONTRIBUTING.md` - Find repositories with a contributing file. [Search](https://github.com/search?q=language%3Amarkdown+path%3ACONTRIBUTING.md&type=code)

- `language:markdown path:.github/ISSUE_TEMPLATE/*.md` - Find repositories with a issue template file. [Search](https://github.com/search?q=language%3Amarkdown+path%3A.github%2FISSUE_TEMPLATE%2F*.md&type=code)

- `language:markdown path:.github/PULL_REQUEST_TEMPLATE/*.md` - Find repositories with a pull request template file. [Search](https://github.com/search?q=language%3Amarkdown+path%3A.github%2FPULL_REQUEST_TEMPLATE%2F*.md&type=code)

- `language:markdown path:CHANGELOG.md` - Find repositories with a changelog file. [Search](https://github.com/search?q=language%3Amarkdown+path%3ACHANGELOG.md&type=code)

- `language:markdown path:*.md "<!--"` - Find repositories with a markdown file that has a comment. [Search](https://github.com/search?q=language%3Amarkdown+path%3A*.md+%22%3C%21--%22&type=code)

#### MediaWiki

- `language:wikitext path:*.mediawiki` - Find repositories with a mediawiki file. [Search](https://github.com/search?q=language%3Awikitext+path%3A*.mediawiki&type=code)

#### ReStructuredText

- `language:restructuredtext path:*.rst` - Find repositories with a restructuredtext file. [Search](https://github.com/search?q=language%3Arestructuredtext+path%3A*.rst&type=code)

- `language:restructuredtext path:README.rst` - Find repositories with a readme file. [Search](https://github.com/search?q=language%3Arestructuredtext+path%3AREADME.rst&type=code)

#### Rich Text Format

- `path:*.rtf` - Find repositories with a rtf file. [Search](https://github.com/search?q=path%3A*.rtf&type=code)

- `path:README.rtf` - Find repositories with a readme file. [Search](https://github.com/search?q=path%3AREADME.rtf&type=code)

- `path:LICENSE.rtf` - Find repositories with a license file. [Search](https://github.com/search?q=path%3ALICENSE.rtf&type=code)

- `path:CHANGELOG.rtf` - Find repositories with a changelog file. [Search](https://github.com/search?q=path%3ACHANGELOG.rtf&type=code)

#### Text

- `language:text path:*.txt` - Find repositories with a text file. [Search](https://github.com/search?q=language%3Atext+path%3A*.txt&type=code)

- `language:text path:README.txt` - Find repositories with a readme file. [Search](https://github.com/search?q=language%3Atext+path%3AREADME.txt&type=code)

- `language:text path:LICENSE.txt` - Find repositories with a license file. [Search](https://github.com/search?q=language%3Atext+path%3ALICENSE.txt&type=code)

- `language:text path:CHANGELOG.txt` - Find repositories with a changelog file. [Search](https://github.com/search?q=language%3Atext+path%3ACHANGELOG.txt&type=code)

- `language:text path:CONTRIBUTING.txt` - Find repositories with a contributing file. [Search](https://github.com/search?q=language%3Atext+path%3ACONTRIBUTING.txt&type=code)


### Comment Annotations

- `"TODO:"` - Find files with a todo comment. [Search](https://github.com/search?q=%22TODO%3A%22&type=code)

- `"FIXME:"` - Find files with a fixme comment. [Search](https://github.com/search?q=%22FIXME%3A%22&type=code)

- `"XXX:"` - Find files with a xxx comment. [Search](https://github.com/search?q=%22XXX%3A%22&type=code)

- `"BUG:"` - Find files with a bug comment. [Search](https://github.com/search?q=%22BUG%3A%22&type=code)

- `"HACK:"` - Find files with a hack comment. [Search](https://github.com/search?q=%22HACK%3A%22&type=code)

- `"NOTE:"` - Find files with a note comment. [Search](https://github.com/search?q=%22NOTE%3A%22&type=code)

- `"OPTIMIZE:"` - Find files with a optimize comment. [Search](https://github.com/search?q=%22OPTIMIZE%3A%22&type=code)

- `"REFACTOR:"` - Find files with a refactor comment. [Search](https://github.com/search?q=%22REFACTOR%3A%22&type=code)

- `"WIP:"` - Find files with a wip comment. [Search](https://github.com/search?q=%22WIP%3A%22&type=code)

- `"DEPRECATED:"` - Find files with a deprecated comment. [Search](https://github.com/search?q=%22DEPRECATED%3A%22&type=code)

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

- `"update" OR "updates" OR "updated"` - Find commits with the word update, updates or updated. [Search](https://github.com/search?q=%22update%22+OR+%22updates%22+OR+%22updated%22&type=commits)

- `"add" OR "adds" OR "added"` - Find commits with the word add, adds or added. [Search](https://github.com/search?q=%22add%22+OR+%22adds%22+OR+%22added%22&type=commits)
