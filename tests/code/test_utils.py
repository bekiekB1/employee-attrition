import json
import tempfile
from pathlib import Path

import pytest

from emply_attr.utils import save_dict


@pytest.fixture
def temp_file_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir, "test.json")


def test_save_dict(temp_file_path):
    # Create test data
    data = {"key1": "value1", "key2": "value2"}
    save_dict(data, temp_file_path)

    assert temp_file_path.exists()

    with open(temp_file_path, "r") as file:
        saved_data = json.load(file)
    assert saved_data == data


def test_save_dict_sortkeys(temp_file_path):
    data = {"b": 2, "a": 1}

    save_dict(data, temp_file_path, sortkeys=True)

    assert temp_file_path.exists()
    with open(temp_file_path, "r") as file:
        saved_data = json.load(file)
    assert list(saved_data.keys()) == sorted(data.keys())
