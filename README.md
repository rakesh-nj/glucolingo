# Contributing to Glucolingo

Thank you for considering contributing to [Your Project Name]! This guide will help you understand how to get involved, report issues, and submit contributions to the project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
   - [Reporting Issues](#reporting-issues)
   - [Suggesting Enhancements](#suggesting-enhancements)
   - [Submitting Code Changes](#submitting-code-changes)
3. [Development Setup](#development-setup)
   - [Fork the Repository](#fork-the-repository)
   - [Setting Up the Environment](#setting-up-the-environment)
   - [Running Tests](#running-tests)
4. [Coding Guidelines](#coding-guidelines)
5. [Style Guide](#style-guide)
6. [Documentation](#documentation)
7. [Community and Support](#community-and-support)
8. [License](#license)

## Code of Conduct

Please read and follow our [Code of Conduct](link_to_code_of_conduct) to ensure a welcoming and inclusive environment for everyone.

## How to Contribute

### Reporting Issues

If you encounter any bugs, have questions, or have feature requests, please open an issue in our [GitHub Issues](link_to_issues). When reporting an issue, include:

- A clear and descriptive title.
- A detailed description of the problem.
- Steps to reproduce the issue, if applicable.
- Any relevant logs, screenshots, or files.

### Suggesting Enhancements

We welcome suggestions for new features and improvements. Please open an issue with:

- A clear and descriptive title.
- A detailed description of the enhancement.
- Why it would be useful.
- Any potential drawbacks.

### Submitting Code Changes

1. **Check for Existing Issues**: Look for existing issues that cover your idea. If one exists, comment on it and mention your plan to contribute.
2. **Fork the Repository**: Fork the repo and create a new branch for your changes.
3. **Make Changes**: Implement your changes, following our coding and style guidelines.
4. **Write Tests**: Add tests to ensure your changes work as expected.
5. **Create a Pull Request**: Submit a pull request with a clear description of your changes, referencing any related issues.




## Contribution Guide 
#### 1. Fork and Clone the repository
- [Fork the repository ](https://github.com/rakesh-nj/glucolingo/fork) 
- Clone the forked repo 
`git clone <forked_repo_url>`
  
#### 2. Create and activate virtual environment
```bash
  cd glucolingo
```
```bash
  python -m venv myenv
```
#### 3. Activate Virtual Environment
  - Windows OS
```bash
  myenv\Scripts\activate
```
  - Linux/mac OS
```bash
  source myenv/bin/activate
  ```
#### 4. Install dependencies
  ```bash
pip install -r requirements.txt
```
#### 5. Start server
```bash
python manage.py runserver
```
