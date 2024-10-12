import pulp

model = pulp.LpProblem("Виробництво напоїв", pulp.LpMaximize)

limonad = pulp.LpVariable('Лимонад', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Фруктовий сік', lowBound=0, cat='Integer')

model += limonad + fruit_juice, "Загальна кількість продукції"

model += 2 * limonad + 1 * fruit_juice <= 100, "Обмеження на воду"
model += 1 * limonad <= 50, "Обмеження на цукор"
model += 1 * limonad <= 30, "Обмеження на лимонний сік"
model += 2 * fruit_juice <= 40, "Обмеження на фруктове пюре"

model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Опт. кількість лимонаду: {limonad.varValue}")
print(f"Опт. кількість соку: {fruit_juice.varValue}")
print(f"Загальна кількість продукції: {limonad.varValue + fruit_juice.varValue}")