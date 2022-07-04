
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Code API Challenge Bankaya Python developer vacancy
  </h3>

  <p align="center">
    Bankaya vacancy application code challenge on technical test
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#test">Test</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#folder-organization">Folder Organization</a></li>
    <li><a href="#architecture-explain">Architecture Explain on Ms</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project 🤔

LONG PROJECT DESCRIPTION

Microservice to request from [API Daily cat facts!](https://alexwohlbruck.github.io/cat-facts/docs/) 
data to and endpoint builded on this microservice application to implement the endpoint request to
[Fact endpoint](https://github.com/alexwohlbruck/cat-facts/blob/master/docs/endpoints/facts.md)
### Built With 🧰

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python 3.10.5](https://www.python.org/downloads/release/python-310/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Library Dependencies injection](../dependencies/dev/requirements.txt) 
* [Envs constants to run microservice](../docs/install(env_file_constants))

<!-- GETTING STARTED -->
## Getting Started 🚀

To run the microservice on local environment, you need:

### Prerequisites ✔️

This is an example of how to list things you need to use the software and how to install them.

* pyenv

  ```sh
  brew install pyenv
  ```

* Create virtual environment

  ```sh
  pyenv virtualenv 3.10.5 my-env
  ```

* Activate virtual environment

  ```sh
  pyenv activate my-env
  ```

* Environment variables required
  - Please looking for the [Envs constants reference](../docs/install/README.md))

### Installation 💻

Steps to run app

1. Get a free API Key at [api_challenge_bankaya](https://github.com/jorgeMorfinezM/api_challenge_bankaya)
2. Clone the repo
   ```sh
   git clone https://github.com/jorgeMorfinezM/api_challenge_bankaya.git
   ```
3. Install project dependencies
   ```sh
   pip install -r dependencies/dev/requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage 🏃

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation (API Documentation)](../docs/api/cat_facts_openapi.yml)_

## Test ✅

Use this space to show us how to run your application tests. Example:

```
pytest tests -vv
```

<!-- FOLDER ORGANIZATION -->
## Folder Organization 📁

- k8s-deployments: Folder with neccessary files to deploy your application
- src: Source project
- tests: Unit test codes


<!-- ARCHITECTURE EXPLAIN -->
## Architecture Explain
![Architecture Microservice Design Diagram](../api_challenge_bankaya/docs/architecture_diagram/domaindrivendesign_n-layered_architecture.png)

Make with ❤️ by Jorge Morfinez Mojica
