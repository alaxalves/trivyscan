import os
import pytest
from unittest.mock import patch
from trivyscan import get_bin
from pathlib import Path


@patch("os.path.exists", return_value=True)
def test_get_bin(mock_exists):
    """Test get_bin returns the correct path when the binary exists."""
    expected_path = os.path.join(Path.cwd(), "bin", "trivy")
    assert get_bin() == expected_path
    mock_exists.assert_called_once_with(os.path.join(Path.cwd(), "bin", "trivy"))

@patch("os.path.exists", return_value=False)
def test_get_bin_not_found(mock_exists):
    """Test get_bin raises FileNotFoundError when the binary does not exist."""
    with pytest.raises(FileNotFoundError, match="Trivy binary not found in package"):
        get_bin()
    mock_exists.assert_called_once()