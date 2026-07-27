from scipy.stats import linregress

def run_regression(data):

    clean_data = data[["Signal", "FutureReturn"]].dropna()

    regression = linregress(
        clean_data["Signal"],
        clean_data["FutureReturn"]
    )

    return regression