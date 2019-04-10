#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `menu_backend` package."""

import unittest
from click.testing import CliRunner
from menu_backend import cli


class test_menu_backend(unittest.TestCase):
    """Tests for `menu_backend` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        """Test the CLI."""
        cli.main()
        runner = CliRunner()
        result = runner.invoke(cli.cli)
        assert result.exit_code == 0
        assert "managedb" in result.output
        assert "startwebservice" in result.output
        assert '--help  Show this message and exit.' in result.output