import matplotlib.pyplot as plt
import seaborn as sns

class CustomPlot():

    def __init__(self,X,y):
        self.X = X
        self.y = y
        self.run_plots()

    def run_plots(self):
        pass

    def scatter(self):
        pass

    def reg(self):
        pass

    def kde(self):
        pass


class NormalPlots(CustomPlot):

    def run_plots(self):
        self.scatter()
        self.reg()
        self.kde()

    def scatter(self):
        sns.scatterplot(x=self.X,y=self.y)

    def reg(self):
        sns.regplot(x=self.X,y=self.y)

    def kde(self):
        sns.kdeplot(self.X,self.y)

class SpecialPlot(CustomPlot):

    def run_plots(self):
        g = sns.jointplot(x=self.X,y=self.y, kind="kde", color="m")
        g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
        g.ax_joint.collections[0].set_alpha(0)
        g.set_axis_labels("$X$", "$Y$");   

class JointPlot(CustomPlot):

    def run_plots(self):
        self.scatter()
        self.reg()
        self.kde()

    def scatter(self):
        sns.jointplot(x=self.X, y=self.y, kind="scatter")

    def reg(self):
        sns.jointplot(x=self.X,y=self.y,kind='reg')

    def kde(self):
        sns.jointplot(x=self.X,y=self.y,kind="kde")