import sys
import unittest
import yaml

sys.path.append('./plugins')
from code_runner import CodeRunner  # NOQA


class TestBashRunner(unittest.TestCase):
    def setUp(self):
        self.code_runner = CodeRunner('odanado/os-command-injection')
        self.source_code = "echo 'Hello World!'"
        self.config = yaml.load(open('./run_ymls/bash.yml'))

    def test_run(self):
        stdout, _, _ = self.code_runner.run(self.source_code, **self.config)
        self.assertEqual(stdout, 'Hello World!')


class TestPython3Runner(unittest.TestCase):
    def setUp(self):
        self.code_runner = CodeRunner('odanado/os-command-injection')
        self.source_code = """
import sys
print('Hello World!', file=sys.stdout)
print('stderr', file=sys.stderr)
        """
        self.config = yaml.load(open('./run_ymls/python3.yml'))

    def test_run(self):
        stdout, stderr, _ = \
            self.code_runner.run(self.source_code, **self.config)
        self.assertEqual(stdout, 'Hello World!')
        self.assertEqual(stderr, 'stderr')
