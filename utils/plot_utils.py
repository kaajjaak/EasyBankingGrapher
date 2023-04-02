import matplotlib.pyplot as plt


def _configure_plot(xlabel, ylabel, title, rotation):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.xticks(rotation=rotation)

    plt.tight_layout()


def plot_line_chart(x, y, xlabel='X-Axis', ylabel='Y-Axis', title='Line Chart', rotation=45, save_file=None):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, 'o-', markersize=5)

    _configure_plot(xlabel, ylabel, title, rotation)

    if save_file:
        plt.savefig(save_file)

    plt.show()


def plot_bar_chart(x, y, xlabel='X-Axis', ylabel='Y-Axis', title='Bar Chart', rotation=45, save_file=None):
    plt.figure(figsize=(12, 6))
    plt.bar(x, y)

    _configure_plot(xlabel, ylabel, title, rotation)

    if save_file:
        plt.savefig(save_file)

    plt.show()


def plot_pie_chart(sizes, labels, title, save_file=None):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title(title)

    # Display the total amounts in the legend
    total_amounts = [f"{label}: {amount:.2f}" for label, amount in zip(labels, sizes)]
    ax.legend(total_amounts, title="Total Amounts", loc="lower left", bbox_to_anchor=(-0.15, 0.8))

    if save_file:
        plt.savefig(save_file)

    plt.show()
