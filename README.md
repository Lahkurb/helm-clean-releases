Helm Clean Releases
============

It is a simple **python** script built to keep our **namespaces** in the develop environment (which also includes feature) clean.

## Copyright (c)

Lucca Pessoa da Silva Matos (c) 2019 - **GitHub Repository**.

## Getting Started

To use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/helm-clean-releases.git -b master
```

This will give access on your **local machine** to this project.

## Organization

* **/code** in this folder we have the **cleanup** application.
* **/docs** is the directory where we have all documentation files.
* **CHANGELOG.md** is a versioning file usend to control development versions.
* **docker-compose.yml** is the **Docker** container orchestrator.
* **Dockerfile** is a file used to set up your **Docker** environment.
* **Makefile** is a file containing a set of automation policies.
* **README.md** is an optional file. A human-readable **README** file.
* **.gitlab-ci.yml** is the file that uses the templates find in **pipeline** folder.
* The files found in the project root are support files to the **CI/CD** process and others contexts.

## Description

As our **CI/CD** process has automatic deployment for the develop and feature branches, we need to control the resources that are being updated in our **Cloud Infrastructure**. The develop **Cluster** has a type of deploy through **Helm**, which creates a release according to the name of the project in **git**. After some time, some feature environments must be excluded in order to keep the **namespaces** clean.

![Alt text](docs/images/HELM.png?raw=true "Helm")

## Pre-Requisites

**Tools**
:---:
**Python**
**Helm**
**Docker**
**docker-compose**

## Containers

It's set at [docker-compose.yml](docker-compose.yml) all the **Containers** required for the application execution.

**Container** | **Description** | **Dockerfile**
:---: | :---: | :---:
cleanup | **Alpine Python Container with helm** | [Dockerfile](Dockerfile)

## Structure

**Components** | **Description** | **Tool**
:---: | :---: | :---:
python | **Languague to create a script that removes all old helm releases** | [Python](https://www.python.org/)
helm | **Charts help you define, install, and upgrade even the most complex Kubernetes application** | [Helm](https://helm.sh/docs/)
docker | **Docker aims create, test and implement applications in a separate environment from the original machine, called a container** | [Docker](https://docs.docker.com/)

## Running pip

The **pip** is a command line program. When you install **pip**, a **pip** command is added to your system, which can be run from the command prompt as follows:

```bash
$ pip <pip arguments>
```

If you cannot run the pip command directly (possibly because the location where it was installed isn't on your operating systems **PATH**) then you can run **pip** via the **Python** interpreter:

```bash
$ python -m pip <pip arguments>
```

On **Windows**, the py launcher can be used:

```bash
$ py -m pip <pip arguments>
```

## Installing Packages

### Pip

The **pip** supports installing from **PyPI**, version control, local projects, and directly from distribution files.

The most common scenario is to install from **PyPI** using Requirement specifiers.

```bash
$ pip install SomePackage            # latest version
$ pip install SomePackage==1.0.4     # specific version
$ pip install somePackage>=1.0.4     # minimum version
```

### Pipenv

**Pipenv** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the **Python** world. **Windows** is a firsts-class citizen, in our world.

It automatically creates and manages a **virtualenv** for your projects, as well as adds/removes packages from your **Pipfile** as you install/uninstall packages. It also generates the ever-important **Pipfile.lock**, which is used to produce deterministic builds.

#### Installation

```bash
$ pip install pipenv
```

#### Create a TOML Spec Pipfile

You can build the **Pipfile** to specifying:

* Versions of a Package.
* Versions of **Python**.
* Basic configurations.

#### Pipenv Workflow

Clone/create project repository:

```bash
$ cd myproject
```

Install from **Pipfile**, if there is one:

```bash
$ pipenv install
```

Install from **Pipfile** dev:

```bash
$ pipenv install --dev
```

## Requirement File

**Requirement File** are files containing a list of items to be installed using **pip** install like so:

```bash
$ pip install -r requirements.txt
```

Logically, a **Requirement File** is just a list of **pip** install arguments placed in a file. Note that you should not rely on the items in the file being installed by **pip** in any particular order.

## Environment variables

**Name**  |  **Description**
:---:  |  :---:
**LOG_PATH**  |  Just the Log Path
**LOG_FILE**  |  Just the Log File
**LOG_LEVEL**  |  Just the Log Level
**LOGGER**  |  Just the Logger name
**NAMESPACE**  |  Kubernetes specific namespace
**ALL_NAMESPACES**  |  Kubernetes all namespaces
**KUBECONFIG**  |  Kubeconfig Cluster path
**KUBECONFIG_CLUSTER**  | Kubeconfig content of your Cluster
**HELM_RELEASE_FILTER_DAYS**  |  Quantity in days from the current date to be used in the filter of helm releases to delete

## Docker

### Building

Additional steps for the developer to build the project after some code changes.

To **Build** the image:

```
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
```

or

```
docker image build -t <IMAGE_NAME> . (This context)
```

Explain:

* **IMAGE_NAME**:
    * Image **Name/Tag**.
* **PATH_DOCKERFILE**:
    * **Dockerfile** location.
    * Where is the full path to **Dockerfile** located?
* **PATH_CONTEXT_DOCKERFILE**:
    * **Dockerfile** context.
    * Where is the **Dockerfile**?

#### Run the Container with the image

* Running the **Container** in **Detached mode**/**Background**:

```
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME>
```

* Running the **Container** in **Interactive mode**:

```
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME>
```

### Basic Commands

* Windows

```
winpty docker.exe run -it --rm <IMAGE_NAME> <COMMAND>
```

* Showing all local images:

```
docker images
```

or

```
docker image ls
```

* Showing all Active or Inactive **Containers**:

```
docker ps -a
```

* Showing all Active **Containers**:

```
docker ps
```

* Entering an Active **Container**:

```
docker exec -it <CONTAINER_ID> <COMMAND>
```

## Usage

<kbd>python ./main.py --help</kbd> - Helper

## Params

```bash
usage: main.py [-h] [-n <namespace>] [-all] [-kcp <kubeconfig>] [-hrfd <days>] [-lp <logpath>] [-lf <logfile>]

Helm Cleanup

optional arguments:
  -h, --help            show this help message and exit
  -n <namespace>, --namespace <namespace>
                        Kubernetes get specific namespace
  -all, --allnamespaces
                        Kubernetes get all namespaces
  -kcp <kubeconfig>, --kubeconfig_path <kubeconfig>
                        Just the Kubeconfig path
  -hrfd <days>, --helm_release_filter_days <days>
                        Helm release creation days to delete
  -lp <logpath>, --logpath <logpath>
                        Custom Log path name
  -lf <logfile>, --logfile <logfile>
                        Custom Log file name
```

## Built with

- [Alpine](https://alpinelinux.org/)
- [Python](https://www.python.org/)
- [Helm](https://helm.sh/docs/)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## How to contribute

1. Make a **Fork**.

2. Follow the project organization.

3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.

4. Make the **Commit**.

5. Open a **Pull Request**.

6. Wait for your pull request to be accepted.. 🚀

Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

## Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

## Contacts

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

---

* **Email**: luccapsm@gmail.com
* **Linkedin**: www.linkedin.com/in/lucca-pessoa-4abb71138/

---

[![Facebook](https://github.frapsoft.com/social/facebook.png)](https://www.facebook.com/lucca.pessoa.9)
[![Github](https://github.frapsoft.com/social/github.png)](https://github.com/lpmatos)

## Versioning

- [CHANGELOG](CHANGELOG.md)

## Project Status

* In production
