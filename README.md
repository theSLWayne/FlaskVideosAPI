# FlaskVideoAPI: A Simple Video API created with Flask

A simple video API created with Python Flask framework

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Run Script](#run)
4. [Endpoints]
5. [Authentiation[WIP]]
5. [Test]

## 1. Introduction <a name="introduction"></a>

- This is a REST API for a video sharing website created with Flask REST framework.
- Currently the API facilitates creating, updating, retrieving, and deleting videos.
- Uploaders can create, update, and delete their videos.
- Both uploaders and users can retrieve all the videos.

## 2. Setup <a name="setup"></a>

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

### 2.5 Deactivate environment

- Use the following command to deactivate the virtual environment.

    ```
    deactivate
    ```

## 3. Run Script <a name="run"></a>

- `app.py` script contains the API service.

- Simply run the scrit to start the server.

    ```
    python app.py
    ```

Notice: **You should activate the virtual environment prior to running this script, if it is not activated yet.**

- If the server started without any errors, a message like the below will appear.

> Serving Flask app "app" (lazy loading)  
> Environment: development  
> WARNING: This is a development server. Do not use it in a production deployment.  
> Use a production WSGI server instead.  
> Debug mode: on  
> Restarting with stat  
> Debugger is active!  
> Debugger PIN: 220-937-628  
> Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  

- You can use `http://127.0.0.1:5000/` address to access the API. Debugger is already activated. (When you do changes to the scrit and save while the server is still running, it will automatically reload)

- Press `CTRL+C` to stop the server.

Notice: **This server is a development server hence shouldn't be used in a production environment.**
