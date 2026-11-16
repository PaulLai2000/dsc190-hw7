import marimo

__generated_with = "0.10.0"
app = marimo.App()


@app.cell
def __():
    import matplotlib.pyplot as plt
    import pandas as pd
    return plt, pd


@app.cell
def __(pd):
    df = pd.read_csv("data/features/events.csv")
    return (df,)


@app.cell
def __(df, plt):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["duration_minutes"], bins=30, edgecolor="black", color="skyblue")
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    plt.gca()
    return ax, fig


if __name__ == "__main__":
    app.run()
