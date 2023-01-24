import numpy as np
from matplotlib import pyplot as plt


def plot_optimization_problem(x_min, x_max, y_min, y_max, min_constraint, max_constraint, x_coef, y_coef,x_solution, y_solution):
	fig, ax = plt.subplots()

	x_plot = np.arange(x_min, x_max+0.1, 0.1)
	y_min_constraint = (min_constraint - x_coef * x_plot)/y_coef
	y1 = np.clip(y_min_constraint, y_min, y_max)
	y_max_constraint = (max_constraint - x_coef * x_plot)/y_coef
	y2 = np.clip(y_max_constraint, y_min, y_max)
	# Fill optimization area
	ax.fill_between(x_plot, y1, y2, color="blue")

	# Plot optimal point
	ax.plot(x_solution, y_solution, 'x', color='red')
	return fig
