import pandas as pd

date = pd.DataFrame({
    "Program": ["P1", "P1", "P2", "P2"],
    "Disciplina": ["A", "B", "A", "B"],
    "Promovati": [9, 80, 20, 1],
    "Total": [10, 100, 100, 10]
})

date["Rata"] = date["Promovati"] / date["Total"]

print("Rate pe fiecare program:")
print(date)

global_rate = date.groupby("Disciplina")[["Promovati", "Total"]].sum()

global_rate["Rata"] = (
    global_rate["Promovati"] / global_rate["Total"]
)

print("\nRate globale:")
print(global_rate)