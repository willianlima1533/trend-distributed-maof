import unittest
from packages.core import Engine, Orchestrator

class TestRuntime(unittest.TestCase):
    def test_engine_start(self):
        engine = Engine(orchestrator=Orchestrator(id='default'))
        engine.start()
        self.assertIsNotNone(engine.orchestrator)

    def test_engine_stop(self):
        engine = Engine(orchestrator=Orchestrator(id='default'))
        engine.stop()
        self.assertIsNotNone(engine.orchestrator)

if __name__ == '__main__':
    unittest.main()