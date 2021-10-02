# FlaskVideoAPI: A Simple Video API created with Flask

A simple video API created with Python Flask framework

## Table of Contents

1. [Introduction]
2. [Setup]
3. [Run Script]
4. [Endpoints]
5. [Authentiation]
5. [Test]

## 1. Introduction

- This is a REST API for a video sharing website created with Flask REST framework.
- Currently the API facilitates creating, updating, retrieving, and deleting videos.
- Uploaders can create, update, and delete their videos.
- Both uploaders and users can retrieve all the videos.

## 2. Setup

- A python environment needs to be created and all the dependencies of this code should be installed to it in order to run API script.
- The script was developed using **Python 3.8.8**, which is the recommended version for running this script.

### 2.1 Install virtualenv

- A python virtual environment is created using the Python package, `virtualenv`.

- `virtualenv` can be installed using the following command.

    ```
    pip install virtualenv
    ```

### 2.2 Create environment

- After installing `virtualenv` package, it can be used to create a python virtual environment.

- Use the following script to create a virtual environment named *env* in the current directory you're on.

    ```
    virtualenv env
    ```

### 2.3 Activate environment

- The process of activating a virtual environment varies with the operating system installed on your computer and below can be found separate guides to activate the created environment in different platforms.

#### 2.3.1 Linux

- Use the following command to activate the created virtual environment on Linux.

    ```
    source env/bin/activate
    ```

#### 2.3.2. Windows

- Use the following command to activate the created virtual environment on Windows.

    ```
    env/Scripts/activate
    ```

### 2.4 Installing dependencies

- Install required dependencies to the activated virtual environment using the following command. **Make sure you're running this command in the base directory of the repository, where requirements.txt is located at**.

    ```
    pip install -r requirements.txt
    ```

**After the installations are finished, you can go ahead and start running the scripts.**


