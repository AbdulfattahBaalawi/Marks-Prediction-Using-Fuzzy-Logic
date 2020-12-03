import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

study = ctrl.Antecedent(np.arange(0, 100, 1), 'study')
difficulty = ctrl.Antecedent(np.arange(0, 100, 1), 'difficulty')

degree = ctrl.Consequent(np.arange(0, 100, 1), 'degree')

study.automf(3, 'quant')
difficulty.automf(3, 'quant')
degree.automf(5, 'quant')

degree_rule1 = ctrl.Rule(difficulty['low'] & study['high'], degree['higher'])
degree_rule2 = ctrl.Rule(difficulty['low'] & study['average'], degree['high'])
degree_rule3 = ctrl.Rule(difficulty['low'] & study['low'], degree['average'])

degree_rule4 = ctrl.Rule(difficulty['average'] & study['high'], degree['high'])
degree_rule5 = ctrl.Rule(difficulty['average'] & study['average'], degree['average'])
degree_rule6 = ctrl.Rule(difficulty['average'] & study['low'], degree['low'])

degree_rule7 = ctrl.Rule(difficulty['high'] & study['high'], degree['high'])
degree_rule8 = ctrl.Rule(difficulty['high'] & study['average'], degree['low'])
degree_rule9 = ctrl.Rule(difficulty['high'] & study['low'], degree['lower'])

degree_ctrl = ctrl.ControlSystem(
    [degree_rule1, degree_rule2, degree_rule3, degree_rule4, degree_rule5, degree_rule6, degree_rule7, degree_rule8, degree_rule9])
degree_sim = ctrl.ControlSystemSimulation(degree_ctrl)

degree_sim.input['difficulty'] = 85
degree_sim.input['study'] = 60

degree_sim.compute()
degree.view(sim=degree_sim)

print(degree_sim.output)
plt.show()