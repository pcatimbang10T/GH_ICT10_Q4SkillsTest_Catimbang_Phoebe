from pyscript import document
import numpy as np
import matplotlib.pyplot as plt

months = []
absences = []

def displaying(e):
    month = document.getElementById("month").value
    absence_input = document.getElementById("absences").value

    # Check input
    if not absence_input:
        document.getElementById("output").innerText = "Please enter absences."
        return

    # Force whole number (removes decimals)
    absence = int(float(absence_input))

    # Save data
    months.append(month)
    absences.append(absence)

    # Plot graph
    plt.clf()
    plt.plot(months, absences, marker="o")
    plt.title("Monthly Attendance")
    plt.xlabel("Month")
    plt.ylabel("Absences (Whole Numbers Only)")
    plt.grid()
    plt.show()

    document.getElementById("output").innerText = f"{month}: {absence} absences recorded"