import unittest
import os
import sys

def run():
    import test_graph
    import test_mst
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(test_graph)
    suite.addTests(loader.loadTestsFromModule(test_mst))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

if __name__ == "__main__":
    try:
        sys.path.insert(0, os.path.abspath(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), '../lib')))

        run()

    except KeyboardInterrupt:
        sys.exit(0)
    
    sys.exit(0)
