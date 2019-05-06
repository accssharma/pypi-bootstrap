# PYPI Bootstrap

### Requirements:

i) PYPI credentials (username and password): register to `pypi.org` (and `test.pypi.org` if desired)

ii) Valid project name unique to both github and pypi (github remote is added as ssh based url)

iii) Absolutely empty github project (without .gitignore and LICENSE at first) repository created using the above project name.

iv) At the least, have `setuptools` (used to generate source and build distributions) and `twine` (used to upload distributions to pypi) packages installed.

#### 1. Create pypi package

```bash
$ ./generate-pypi-pkg </absolute/path/to/project/demo> <github_username>

Eg.
$ ./generate-pypi-pkg /home/asharma/projects/pypidemo accssharma
```

#### 2. Generate and publish package

Instructions also included in the generated README.md (view generic version 
[here](https://github.com/accssharma/pypi-bootstrap/blob/master/pypi-project/README.md)) inside the created project.

From inside the generated project:

```bash
# create source and build distribution
$ make distribution

# upload distribution, and go to your pypi account to verify the upload
$ make upload

# clean local builds before running pip install from the pypiserver
$ make clean

# pip install (beware of the cache)
$ make pip-install
```

Finally, verify installation by running the entrypoint command or check the package list using `pip freeze`.

If anything goes wrong, restart from the beginning!

#### 3. If 2. goes as expected, save changes to Github.

Navigate to /path/to/pypi/demo project, and push your changes to your previously created empty github repository.

Note that the created project already reference to the remote (provided that you used the same project name when creating a repo.)

```bash
# see the project name and entrypoint reference changes
$ git show
$ git log

# if you've your new changes
$ git add <file1> <file2>

$ git commit --amend
$ git push -u origin master

```

Inside the generated project:
- `README.md` - installation and detail information for github.
- `PYPI_README.md` - used to generate PYPI homepage detail information.
- `{package_dir}/version.py` - file to update package version.
- Recommended - update `LICENSE` as per your requirement (default is `MIT`)

