# Python-Scripting

This repository has been created to store the code and Jupyter files related to the Python Scripting lecture, which is provided to the students of the Cybersecurity and Cloud Computing Techniques Engineering department at the Technical Engineering College-Mosul, Northern Technical University. The lecture slides will also be published in this repository after the lecture has been given.

## Contents

The repository contains the following Jupyter files and code samples:

1-Subprocess Module: This Jupyter notebook file contains examples of using `subprocess.run()` to execute commands.

2-calculator: A simple script that adds or subtracts two given numbers. It accepts command-line arguments, parses them using `argparse`, and returns the calculation`s result.

3-create_table: A Python script demonstrating how to create a table using the `MySQL-Python-Connector`.

4-crypto: A Jupyter notebook file that demonstrates the usage of the `cryptography` library for encrypting and decrypting messages.

5-hashing: A Jupyter file that contains a demonstration of the `hashlib` library.

6-insrt: A Python script demonstrating how to insert data into a table using the `MySQL-Python-Connector`.

7-os Module: A Jupyter file with examples of using the Python `os` module.

8-scan: A Python script that scans a target using the `Nmap Scanner`, retrieves the results, and stores them in a file.

9-slct: A Python script demonstrating retrieving data from a table using the `MySQL-Python-Connector`.

10-terminal: A simple Python script that emulates a terminal.



## First step


### Requirements:

Python Libraries: A requirement text file that contains all the Python libraries required for that lecture was uploaded to this Github repository.

Note: It is also required to install any tool that was run using `subprocess` module on your machine, such as Nmap Scanner.

### Git

Git is a versatile version control system that can be utilized in various scenarios. you should install Git on your operating system and configure it as per your specific requirements. It would be useful to take a Git crash course to get a better understanding of how it works.

### Virtual Environment

I recommend using a Python virtual environment to create isolated environments for your project's libraries, avoiding issues with future library updates.  

### Let`s Start

To clone the repository and set up the Python virtual environment on Windows, run the commands provided below in PowerShell: 

    git clone https://github.com/MustafaAbdulazizHamza/Python-Scripting.git

    cd Python-Scripting 

    python -m pip install --upgrade pip

    python -m venv env

    .\env\Scripts\activate

    python -m pip install -r requirements.txt

To perform the same process on Linux OS, run the commands provided below:

    git clone https://github.com/MustafaAbdulazizHamza/Python-Scripting.git

    cd Python-Scripting

    python3 -m venv env

    python3 -m pip install --upgrade pip

    source env/bin/activate
        
    python3 -m pip install -r requirements.txt  

## Labs

The solution to the lab homework was posted to the repository inside the directory named Labs, except for Lab 4 solution.
