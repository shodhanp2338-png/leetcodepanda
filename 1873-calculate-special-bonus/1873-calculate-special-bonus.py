import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[
        (employees['employee_id'] % 2 == 0) |
        (employees['name'].str.startswith('M')),
        'salary'
    ] = 0

    employees_bonus = employees[['employee_id', 'salary']].rename(
        columns={'salary': 'bonus'}
    )

    return employees_bonus.sort_values('employee_id')
