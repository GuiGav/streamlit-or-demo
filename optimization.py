import dataclasses

from ortools.linear_solver import pywraplp


@dataclasses.dataclass
class LinearOptimizationProblem:
	x_min: float
	x_max: float
	y_min: float
	y_max: float
	min_constraint: float
	max_constraint: float
	x_coef_constraint: float
	y_coef_constraint: float
	x_coef_objective: float
	y_coef_objective: float


def optimize(problem: LinearOptimizationProblem):
	solver = pywraplp.Solver.CreateSolver('GLOP')
	x = solver.NumVar(problem.x_min, problem.x_max, 'x')
	y = solver.NumVar(problem.y_min, problem.y_max, 'y')

	ct = solver.Constraint(problem.min_constraint, problem.max_constraint, 'ct')
	ct.SetCoefficient(x, problem.x_coef_constraint)
	ct.SetCoefficient(y, problem.y_coef_constraint)

	objective = solver.Objective()
	objective.SetCoefficient(x, problem.x_coef_objective)
	objective.SetCoefficient(y, problem.y_coef_objective)
	objective.SetMaximization()

	solver.Solve()
	return x.solution_value(), y.solution_value(), objective.Value()
