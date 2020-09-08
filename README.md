# alluxio-worker Python api


## Dependencies

* Python 3.6 or later
* alluxio
* docker
* kubernetes
* pytest


```build docker image
cd Dockerfile
docker build -t alluxio-worker .
```__

```run alluxio_worker app
python3 app.py
```

## Code Style

Follow [pep8](https://www.python.org/dev/peps/pep-0008/) for source code style,
except the restriction for line width.

Follow [Google style](http://www.sphinx-doc.org/en/stable/ext/example_google.html)
for docstrings.

## Unit Tests

Unit tests are in `alluxio_worker/tests` directory, they can be run under the `alluxio_worker` directory by

```bash
pytest
```

See the test coverage report by

```bash
pytest --cov .
```

## Integration Tests

Integration tests are under the `tests` directory, see `tests/README.md` for more details.
