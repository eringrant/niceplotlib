"""Mods to `matplotlib` to make it play nicely with LaTeX documents."""
__version__ = "1.0.0"

import matplotlib.pyplot as plt


plt.style.use("seaborn-colorblind")
tex_fonts = {
  # Use LaTeX to write all text.
  "text.usetex": True,
  "font.family": "times",
  # Use system fonts when rendering SVGs.
  "svg.fonttype": "none",
  # Use 10pt font in plots to match 10pt font in document.
  "axes.labelsize": 10,
  "font.size": 10,
  # Make the legend/label fonts a little smaller.
  "legend.fontsize": 8,
  "xtick.labelsize": 8,
  "ytick.labelsize": 8,
  # Decrease lineweidths to match thinner TeX lettering.
  "axes.linewidth": 0.1,
  "lines.linewidth": 0.5,
}
plt.rcParams.update(tex_fonts)


def set_size(
  width: float,
  ratio: float = (5**0.5 - 1) / 2,
  fraction: float = 1,
  subplots: tuple[int, int] = (1, 1),
) -> tuple[float, float]:
  """Set figure dimensions to avoid scaling in LaTeX.

  Sourced from https://jwalton.info/Embed-Publication-Matplotlib-Latex/.

  Args:
    width: Document textwidth or columnwidth in pts.
    fraction: Fraction of `width` for figure to occupy.
    subplots: The number of rows and columns of subplots.

  Returns:
    fig_dim: `matplotlib`-compatible figure dimensions in inches.
  """
  # Width of figure (in pts).
  fig_width_pt = width * fraction

  # Convert from pt to inches.
  inches_per_pt = 1 / 72.27

  # Figure width in inches.
  fig_width_in = fig_width_pt * inches_per_pt

  # Figure height in inches.
  fig_height_in = fig_width_in * ratio * (subplots[0] / subplots[1])

  return fig_width_in, fig_height_in
