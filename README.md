# PYPI Bootstrap

Generate a minimal python package within a minute. Add and maintain your source code in github, and distribute your package to `pypi.org` when your code is ready.

### Requirements:

1. PYPI credentials (username and password): Register to `pypi.org` (and `test.pypi.org`, if desired)

2. Valid project name unique to both github and pypi (github remote is added as ssh style url)

3. Absolutely empty new github repository (without .gitignore and LICENSE at first) created with the same name as chosen in 2.

4. At the least, install the following two packages:
   - `setuptools` - used to generate source and build distributions
   - `twine` - used to upload distributions to pypi

### Create pypi package

```bash
$ ./generate-pypi-pkg </absolute/path/to/project/demo> <github_username>

Eg.
$ ./generate-pypi-pkg /home/asharma/projects/pypidemo accssharma
```

### Build and Distribute

Instructions are also included in the README.md file generated inside the created project. View generic version [here](https://github.com/accssharma/pypi-bootstrap/blob/master/pypi-project/README.md).

Here're the important `make` targets for installation and distribution available in the generated package's Makefile.

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

If anything goes wrong, clean up and restart from the beginning! It's strongly recommended to use fresh `virtualenv` environment(or your favorite package and enviornment management utilities) for testing, developing and distribution your package.

### Save changes to Github.

Navigate to your generated project, and push your changes to your previously created empty github repository.

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

