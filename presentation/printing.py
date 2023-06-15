import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree


def trim(x, y, percent=10):
    current_x = x
    x_lower, x_upper = np.percentile(current_x, [percent, 100-percent])
    mask = (current_x >= x_lower) & (current_x <= x_upper)
    x_clean = current_x[mask]
    y_clean = y[mask]
    return y_clean, x_clean


def scatter_2d_dataset(x: np.ndarray,
                       y: np.ndarray,
                       naming: list,
                       title: str = "",
                       alpha: float = 1,
                       trim_percent: float = 0,
                       hide_ticking=False,
                       estimator=None) -> None:

    titles = naming
    cmap = plt.cm.get_cmap('jet')
    num_colors = len(naming)
    colors = [cmap(i / num_colors) for i in range(num_colors)]

    fig, ax = plt.subplots(1, x.shape[1], sharey=True)
    fig.set_figwidth(15)
    fig.suptitle(title)

    ax[0].set_ylabel("MedHouseVal in 100.000$")

    clean = []
    for i in range(x.shape[1]):
        clean.append(trim(x[:, i], y, trim_percent))
    if estimator is not None:
        data = np.concatenate([tup[1].reshape((-1, 1))
                              for tup in clean], axis=1)
        print(data)
        y_pred = estimator.predict(data)

    for i in range(x.shape[1]):
        lowest = round(np.min(clean[i][1]), 2)
        mean = round(np.mean(clean[i][1]), 2)
        highest = round(np.max(clean[i][1]), 2)
        if estimator is not None:
            ax[i].scatter(data[:, i], y_pred,
                          color="black", s=0.1, alpha=alpha)

        if not hide_ticking:
            ax[i].set_xticks([lowest, mean, highest], rotation=45)
            ax[i].tick_params(axis='x', labelrotation=45)
        ax[i].set_title(titles[i])
        ax[i].scatter(x=clean[i][1], y=clean[i][0],
                      color=colors[i], s=0.1, alpha=alpha)
    plt.show()


def hist_2d_dataset(x: np.ndarray,
                    y: np.ndarray,
                    naming: list,
                    title: str = "",
                    trim_percent: float = 0,
                    bins=10,
                    hide_ticking=False) -> None:
    titles = naming

    fig, ax = plt.subplots(1, x.shape[1], sharey=True)
    fig.set_figwidth(15)
    fig.suptitle(title)
    ax[0].set_ylabel("MedHouseVal in 100.000$")
    for i in range(x.shape[1]):
        y_clean, x_clean = trim(x[:, i], y, trim_percent)
        lowest = round(np.min(x_clean), 2)
        mean = round(np.mean(x_clean), 2)
        highest = round(np.max(x_clean), 2)
        if not hide_ticking:
            ax[i].set_xticks([lowest, mean, highest], rotation=45)
            ax[i].tick_params(axis='x', labelrotation=45)
        ax[i].set_title(titles[i])
        ax[i].hist2d(x_clean, y_clean, bins=bins, density=True, cmap="jet")


def map_plot(data: pd.DataFrame):

    data.plot(
        kind="scatter",
        x="Longitude",
        y="Latitude",
        alpha=0.3,
        s=data["Population"] / 100,
        label="Population",
        figsize=(10, 7),
        c="MedHouseVal",
        cmap=plt.get_cmap("jet"),
        colorbar=True,
    )
    plt.scatter(x=[-118], y=[34], marker=",", label="Los Angeles",
                s=100, c="white")
    plt.scatter(x=[-122], y=[37], marker="^", label="San Francisco",
                s=100, c="white")
    plt.legend()
    plt.show()


def highlight_desc(desc: pd.DataFrame):
    pass


def highlight_corr(corr: pd.DataFrame):
    return "background-color: red" if abs(corr) > 0.7 else None


def lin_plot(x, y, y_pred, x_test):
    cmap = plt.cm.get_cmap('jet')
    num_colors = 8
    colors = [cmap(i / num_colors) for i in range(num_colors)]
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=x[:, 0], y=y, color=colors[3], s=0.1, alpha=0.5)
    ax.set_xlabel("MeanInc")
    ax.set_ylabel("MedHouseVal")
    ax.plot(x_test, y_pred, color=colors[7],  alpha=1, linewidth=2)
    plt.show()


def plot_prescaled_tree(x, y, params, feature_names):
    regr_pre = DecisionTreeRegressor(**params)
    x_train_pre, x_test_pre, y_train_pre, y_test_pre = train_test_split(
        x, y, test_size=0.2)
    regr_pre.fit(x_train_pre, y_train_pre)
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(20, 10)
    plot_tree(regr_pre,
              max_depth=2,
              feature_names=feature_names,
              rounded=True,
              ax=ax,
              proportion=True
              )
    plt.show()
