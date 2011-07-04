""" Tests """

# matplotlib will open windows during testing unless you do the following
import matplotlib
matplotlib.use("AGG") 

import data
import models
import graphics

class TestClass:
    def setUp(self):
        pass

    def test_data(self):
        assert len(data.all) > 0, 'Should have some rows of data'

    def test_linear_model(self):
        vars = models.linear()
        assert 'beta' in vars

    def test_graphics(self):
        graphics.plot_all_data()

if __name__ == '__main__':
    import nose
    nose.run()
