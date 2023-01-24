from ortools.linear_solver import pywraplp


def optimize(x_min, x_max, y_min, y_max, min_constraint, max_constraint, x_coef, y_coef, a, b):
	solver = pywraplp.Solver.CreateSolver('GLOP')
	x = solver.NumVar(x_min, x_max, 'x')
	y = solver.NumVar(y_min, y_max, 'y')

	ct = solver.Constraint(min_constraint, max_constraint, 'ct')
	ct.SetCoefficient(x, x_coef)
	ct.SetCoefficient(y, y_coef)

	objective = solver.Objective()
	objective.SetCoefficient(x, a)
	objective.SetCoefficient(y, b)
	objective.SetMaximization()

	solver.Solve()
	return x.solution_value(), y.solution_value(), objective.Value()
