import models
import graphics

def linear_model_example():
    m = models.linear()
    graphics.plot_all_data()
    graphics.plot_linear_model(m)


def nonlinear_model_example():
    mn = fit(nonlinear())

    import graphics
    reload(graphics)
    reload(graphics.data)

    pl.clf()

    graphics.plot_all_data()
    graphics.plot_linear_model(ml)
    graphics.plot_nonlinear_model(mn)

    pl.show()


if __name__ == '__main__':
    linear_model_example()
