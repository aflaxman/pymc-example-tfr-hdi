""" Tests """

# matplotlib will open windows during testing unless you do the following
import matplotlib
matplotlib.use("AGG") 

import models

class TestClass:
    def setUp(self):
        pass

    def test_data(self):
        import data
        assert len(data.all_data) > 0, 'Should have some rows of data'
