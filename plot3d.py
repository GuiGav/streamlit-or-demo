import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from optimization import LinearOptimizationProblem, Point3D
from matplotlib import cm


def plot_optimization_problem(problem: LinearOptimizationProblem, solution: Point3D):
	x_plot = np.arange(problem.x_min, problem.x_max+0.1, 0.1)
	y_plot = np.arange(problem.y_min, problem.y_max+0.1, 0.1)
	X, Y = np.meshgrid(x_plot, y_plot)
	Z = X * problem.x_coef_objective + Y * problem.y_coef_objective

	df = pd.DataFrame({'x': X.flatten(), 'y': Y.flatten(), 'z': Z.flatten()})
	df["constraint_value"] = df['x']*problem.x_coef_constraint + df['y']*problem.y_coef_constraint
	df = df[(df["constraint_value"] > problem.min_constraint) & (df["constraint_value"]<problem.max_constraint)]

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	# 3D plot
	ax.plot_trisurf(df.x, df.y, df.z, cmap=cm.jet, linewidth=0.2)
	ax.scatter(solution.x, solution.y, solution.z, marker="x")

	# 2D projection
	y_min_constraint = (problem.min_constraint - problem.x_coef_constraint * x_plot) / problem.y_coef_constraint
	y1 = np.clip(y_min_constraint, problem.y_min, problem.y_max)
	y_max_constraint = (problem.max_constraint - problem.x_coef_constraint * x_plot) / problem.y_coef_constraint
	y2 = np.clip(y_max_constraint, problem.y_min, problem.y_max)
	# Fill optimization area
	ax.add_collection3d(ax.fill_between(x_plot, y1, y2, color="grey", alpha=0.5), zs=0, zdir='z')

	return fig
