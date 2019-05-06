# Publish your project to the main PYPI server:

Build source (and/or wheel distribution using setup tools)

Optionally: `$make clean`

```bash
$ make distribution
```

Upload to the main pypi server using `twine`:

```bash
$ make upload
```

Install package using the main PYPI server (beware of caching problem)

```bash
$ make pip-install
```

OR

```bash
$ pip install YOUR_PROJECT_NAME==CURRENT_VERSION
```

### Installation verification

Finally, verify installation using the exposed entry point:

```bash
$ YOUR_PROJECT_ENTRYPOINT --version
```

Should print something like:

```
Package: YOUR_PROJECT_NAME
Version: x.x.x
```

## Using test server
Push to test server: `--repository-url https://test.pypi.org/legacy`, then:

```
$ pip install -i https://test.pypi.org/simple/ YOUR_PROJECT_NAME
```

WARNING: Since the packages are not upto date in the test server, or may not even exist in the first place, pay extra attention to your dependencies when testing with test pypi server.


## Notes
- Read version information to be used appropriately in a source distribution.
  - environment variable approach isn't a very good idea
  - [A few good suggestions here.](https://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package)

# License
> UPDATE
