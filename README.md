# niceplotlib

Mods to [`matplotlib`](https://matplotlib.org/) to make it play nicely with LaTeX documents.


## Installation

To install via [pip](https://pip.pypa.io/) on the command line, do:

```bash
python -m pip install git+https://github.com/eringrant/niceplotlib
```

The dependency can also be added to a `requirements.txt` or `environment.yml` file as:

```yaml
niceplotlib @ git+https://github.com/eringrant/niceplotlib
```

## Usage

The package sets text and color defaults for `matplotlib` plots to be used in LaTeX documents.
The package also includes utilies for [sizing plots](#sizing-plots).
See ["Saving plots"](#saving-plots) for recommendations on saving plots.

### Sizing plots

#### Determining the target plot width from TeX

First, determine text or column width of your target TeX document.
Add the statement `\showthe\textwidth` (`\showthe\columnwidth` for two-column format) 
to your document:

```
\documentclass{report}
\begin{document}

...

\showthe\textwidth

...

\end{document}
```

Then compile the document; the output will give something like:

```bash
> 345.0pt.
l.5 \showthe\textwidth
```

Use `345` as the width passed to `npl.set_size`.

#### Using `niceplotlib.set_size` to size `matplotlib` plots

Pass the TeX document width determined 
[above](#determining-the-target-plot-width-from-tex) to `npl.set_size` as the 
`figsize` when creating a `matplotlib` plot. A minimal example is:

```python
import niceplotlib as npl
import numpy as np

# Plot
x = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(1, 1, figsize=npl.set_size(width))
ax.plot(x, np.sin(x))
ax.set_xlim(0, 2 * np.pi)
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$\sin (\theta)$')
```

### Saving plots

Plots should be saved in a vector format to prevent pixelation. Use either PDF:

```python
fig.savefig('example.pdf', format='pdf', bbox_inches='tight')
```

Or SVG:

```python
fig.savefig('example.svg', format='svg', bbox_inches='tight')
```



## References

This package is heavily inspired by Jack Walton's post on "[Plot publication-quality figures with matplotlib and LaTeX](https://jwalton.info/Embed-Publication-Matplotlib-Latex/)."
