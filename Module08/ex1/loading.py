#!/usr/bin/env python3

import sys
from typing import Any


def check_dependencies() -> dict:
    results: dict = {}

    print("Checking dependencies:")
    try:
        import pandas
        results["pandas"] = pandas.__version__
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        results["pandas"] = None

    try:
        import numpy
        results["numpy"] = numpy.__version__
        print(f"[OK] numpy ({numpy.__version__}) - Numerical computation "
              "ready")
    except ImportError:
        results["numpy"] = None

    try:
        import matplotlib
        results["matplotlib"] = matplotlib.__version__
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization "
              "ready")
    except ImportError:
        results["matplotlib"] = None

    return results


def analyze_visualize_data() -> None:
    import pandas
    import numpy
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    try:
        # numpy data generation
        numpy.random.seed(10)
        data: Any = numpy.random.random((50, 3))

        # pandas dataframe creation
        df = pandas.DataFrame(data, columns=["A", "B", "C"])
    except Exception:
        print("Processing data points failed.")
    print("Processing 1000 data points...")

    # visualize df
    print("Generating visualization...")

    try:
        plt.title("Matrix Visualization")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.plot(df["A"])
        plt.plot(df["B"])
        plt.plot(df["C"])
        plt.savefig("matrix_analysis.png")
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception:
        print("\nAnalysis failed.")


if __name__ == "__main__":
    print("LOADING STATUS: Loading program...\n")

    deps: dict = check_dependencies()
    missing: list = [name for name, version in deps.items()
                     if version is None]

    if missing:
        print("Missing dependencies detected:")
        for dep in missing:
            print(f" -{dep}")
            print(f"    Install with pip: pip install {dep}")
            print(f"    Install with poetry: poetry add {dep}")
        print("or:")
        print("    Install with pip: pip install -r requirements.txt")
        print("    Install with poetry: poetry install\n")
        print("When using pip, please create a virtual "
              "environment\nusing the following instructions:")
        print(" python3 -m venv <name>")
        print(" source name/bin/activate")
        print("When using poetry, run:")
        print(" poetry run python loading.py")
        exit()

    if "pypoetry" in sys.executable:
        print("\nEnvironment detected: Poetry")
    elif "/bin/python" in sys.executable and "pypoetry" not in sys.executable:
        print("\nEnvironment detected: Pip")
    else:
        print("\nEnvironment detected: System")
    print(f"Python executable: {sys.executable}")

    analyze_visualize_data()
