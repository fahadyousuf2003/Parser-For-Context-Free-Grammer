# Simple Parser for Context-Free Grammar

This repository contains a simple parser for a context-free grammar, along with a utility to visualize the parse tree for valid expressions.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Example Expressions](#example-expressions)
- [Project Structure](#project-structure)

## Introduction

This project demonstrates a basic implementation of a parser for a context-free grammar using Python. It defines a simple grammar for expressions involving addition and multiplication operators, along with parentheses. The parser validates expressions and constructs a parse tree for valid inputs.

## Usage

To use the parser and visualize the parse tree, follow these steps:

1. Clone this repository:
   git clone https://github.com/fahadyousuf2003/Parser-For-Context-Free-Grammer.git
   cd Parser-For-Context-Free-Grammer

2. Run the main.py script:
   python main.py

3. The script will test a list of example expressions (both correct and incorrect) and display whether each expression is part of the defined context-free grammar. For valid expressions, it will also display the parse tree.

## Example Expressions

The following expressions are tested by the parser:

- (a+a)*a (Correct)
- a*(a*a)+a (Correct)
- (a*a)+(a+a) (Correct)
- a+a)*a (Incorrect: Missing opening parenthesis)
- (a+a*a (Incorrect: Missing closing parenthesis)
- a+a*a) (Incorrect: Missing opening parenthesis)

## Project Structure

The project is structured as follows:

- main.py: The main script that tests example expressions.
- parser.py: Defines the Parser class responsible for parsing expressions.
- tree.py: Defines the Node class for building parse trees and a function to print the parse tree.


Feel free to contribute to this project or use it as a reference for implementing more complex parsers or grammars. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

Happy parsing!
