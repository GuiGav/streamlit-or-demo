import numpy as np
from matplotlib import pyplot as plt

from optimization import LinearOptimizationProblem


def plot_optimization_problem(problem: LinearOptimizationProblem, x_solution: float, y_solution: float):
	fig, ax = plt.subplots()

	x_plot = np.arange(problem.x_min, problem.x_max+0.1, 0.1)
	y_min_constraint = (problem.min_constraint - problem.x_coef_constraint * x_plot) / problem.y_coef_constraint
	y1 = np.clip(y_min_constraint, problem.y_min, problem.y_max)
	y_max_constraint = (problem.max_constraint - problem.x_coef_constraint * x_plot) / problem.y_coef_constraint
	y2 = np.clip(y_max_constraint, problem.y_min, problem.y_max)
	# Fill optimization area
	ax.fill_between(x_plot, y1, y2, color="blue")

	# Plot optimal point
	ax.plot(x_solution, y_solution, 'x', color='red')
	return fig
