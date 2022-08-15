import os
from pathlib import Path

import pytest

from fast_sqlalchemy.config.yaml import Configuration
from dotenv import load_dotenv

root_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def config_test():
    return Configuration(os.path.join(root_dir, "test_cfg_dir"))

def test_get_yaml_config(config_test):
    config_test.load_config()
    assert config_test["db"].get() == "test_db"
def test_yaml_config_with_env(config_test):
    config_test.load_config(os.path.join(root_dir, ".env"))
    assert config_test["env_key"].get() == "var_foo.bar"
