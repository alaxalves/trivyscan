import subprocess
import os
from pathlib import Path

INSTALL_DIR = os.path.join(Path.cwd(), "bin")
TRIVY_BIN = os.path.join(INSTALL_DIR, "trivy")
TRIVY_VERSION = "0.59.1"

def get_bin():
    """Returns the path to the Trivy binary, extracting it if necessary."""
    if not os.path.exists(TRIVY_BIN):
        raise FileNotFoundError("Trivy binary not found in package. Ensure it is included in the installation.")
    return TRIVY_BIN

def scan(docker_image, cache_dir="cache/", output_file="scan-results.json"):
    """
    Runs a Trivy security scan on a Docker image using the included Trivy binary.
    
    :param docker_image: Docker image full name with tag
    :param cache_dir: Directory to store Trivy cache
    :param output_file: Path to save the scan results
    """
    trivy_path = get_bin()

    trivy_cmd = [
        trivy_path, "image",
        "--exit-code", "0",
        "--format", "json",
        "-o", output_file,
        "--timeout", "12m0s",
        "--cache-dir", cache_dir,
        "--severity", "HIGH,CRITICAL",
        docker_image
    ]
    
    print("Running Trivy scan...")
    subprocess.run(trivy_cmd, check=True)
    print("Scan complete! JSON report saved.")
