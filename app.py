import streamlit as st

import plot
from optimization import optimize, LinearOptimizationProblem

st.title('Optimization demo')

st.write("### Variable constraint")
col_min, col_max = st.columns(2)
with col_max:
	x_max = st.number_input(label="X max", value=10)
	y_max = st.number_input(label="Y max", value=10)
with col_min:
	x_min = st.number_input(label="X min")
	y_min = st.number_input(label="Y min")

st.write("### Linear constraint : min_constraint < X * x_coef + Y * y_coef < max_constraint")
col_coef, col_constraint = st.columns(2)
with col_coef:
	x_coef = st.number_input(label="X coef", value=1)
	y_coef = st.number_input(label="Y coef", value=1)
with col_constraint:
	min_constraint = st.number_input(label="min constraint")
	max_constraint = st.number_input(label="max constraint", value=10)

st.write("### Objective function to maximize : a * x + b * y")
col_a, col_b = st.columns(2)
with col_a:
	a = st.number_input("a", value=1)
with col_b:
	b = st.number_input("b", value=1)

problem = LinearOptimizationProblem(x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max, min_constraint=min_constraint,
                                    max_constraint=max_constraint, x_coef_constraint=x_coef, y_coef_constraint=y_coef, x_coef_objective=a, y_coef_objective=b)
x_solution, y_solution, objective_value = optimize(problem)
st.write("### Optimization area")

fig = plot.plot_optimization_problem(problem=problem, x_solution=x_solution, y_solution=y_solution)
st.pyplot(fig)

st.write(f"""### Solution:
        Objective value ={objective_value}
        x = {x_solution}
        y = {y_solution}"""
         )
