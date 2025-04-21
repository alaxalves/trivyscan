# trivyscan

**trivyscan** is a Python package that simplifies security scanning of Docker images using [Trivy](https://trivy.dev/latest/). It bundles the Trivy binary, so you don’t need to install Trivy separately.

## 🔍 Overview

[Trivy](https://trivy.dev/latest/?utm_source=chatgpt.com) is a comprehensive open-source vulnerability scanner for containers and other artifacts, capable of detecting CVEs and misconfigurations across code repositories, container images, file systems, and more.

**trivyscan** provides a Python wrapper to interact with Trivy programmatically, enabling integration with your own tools or CI/CD pipelines.

## ⚙️ Installation

Install via pip:

```bash
pip install trivyscan
```

## 🚀 Usage

Basic usage example:

```python
from trivyscan import TrivyScan

scanner = TrivyScan()
scanner.scan_image('your-image-name:tag')
```

This will run a security scan on the specified Docker image.

## 📁 Project Structure

- `trivyscan/`: Core module containing the logic to run Trivy
- `test/`: Unit tests for the package
- `setup.py`: Package installation configuration
- `requirements.txt`: List of dependencies

## 🧪 Running Tests

Run the tests using:

```bash
python -m unittest discover test
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

For more information, visit the official repository: [https://github.com/alaxalves/trivyscan](https://github.com/alaxalves/trivyscan)
