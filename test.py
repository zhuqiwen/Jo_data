from numpy.random import beta
import matplotlib.pyplot as plt

plt.style.use('bmh')


def plot_beta_hist(a, b):
    plt.hist(beta(a, b, size=10000), histtype="stepfilled",
             bins=25, alpha=0.8, normed=True)
    return

plot_beta_hist(10, 10)
plot_beta_hist(20, 20)
plot_beta_hist(50, 12)
plot_beta_hist(6, 55)

plt.show()