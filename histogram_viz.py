"""
Sample script: histogram and basic data visualizations.

Generates synthetic data and saves a multi-panel figure to histogram_viz.png.
Run: python histogram_viz.py
"""

import sys

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    rng = np.random.default_rng(42)

    # Synthetic datasets
    exam_scores = rng.normal(loc=72, scale=12, size=500)
    exam_scores = np.clip(exam_scores, 0, 100)

    daily_steps = rng.gamma(shape=5.0, scale=1500, size=300)

    categories = ["Reading", "Exercise", "Coding", "Social"]
    hours_per_week = [6, 4, 12, 8]

    x = rng.uniform(0, 10, size=80)
    y = 2.5 * x + rng.normal(0, 3, size=80)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Sample Histogram & Visualizations", fontsize=14, fontweight="bold")

    # 1. Histogram
    axes[0, 0].hist(exam_scores, bins=20, color="#4C72B0", edgecolor="white", alpha=0.9)
    axes[0, 0].set_title("Exam Score Distribution")
    axes[0, 0].set_xlabel("Score")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].axvline(exam_scores.mean(), color="crimson", linestyle="--", label=f"Mean: {exam_scores.mean():.1f}")
    axes[0, 0].legend()

    # 2. Bar chart
    bars = axes[0, 1].bar(categories, hours_per_week, color=["#55A868", "#C44E52", "#8172B2", "#CCB974"])
    axes[0, 1].set_title("Weekly Activity Hours")
    axes[0, 1].set_ylabel("Hours")
    for bar, value in zip(bars, hours_per_week):
        axes[0, 1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2, str(value), ha="center", fontsize=9)

    # 3. Scatter plot with trend line
    axes[1, 0].scatter(x, y, alpha=0.7, color="#4C72B0", edgecolors="white", linewidth=0.5)
    coeffs = np.polyfit(x, y, 1)
    trend_x = np.linspace(x.min(), x.max(), 100)
    axes[1, 0].plot(trend_x, np.polyval(coeffs, trend_x), color="crimson", linewidth=2, label="Trend")
    axes[1, 0].set_title("Scatter Plot with Trend Line")
    axes[1, 0].set_xlabel("X")
    axes[1, 0].set_ylabel("Y")
    axes[1, 0].legend()

    # 4. Box plot (another way to visualize distributions)
    axes[1, 1].boxplot([daily_steps, exam_scores * 100], tick_labels=["Daily Steps", "Scores × 100"], patch_artist=True,
                       boxprops=dict(facecolor="#55A868", alpha=0.7))
    axes[1, 1].set_title("Distribution Comparison (Box Plot)")
    axes[1, 1].set_ylabel("Value")

    plt.tight_layout()
    output_path = "histogram_viz.png"
    plt.savefig(output_path, dpi=150)
    print(f"Saved figure to {output_path}")

    # Pass --show to open an interactive plot window
    if "--show" in sys.argv:
        plt.show()


if __name__ == "__main__":
    main()
