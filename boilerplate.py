import math
import numpy
import scipy.ndimage
import matplotlib.pyplot

def main():
  w, h = 400, 300
  num_frames = 300
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    ax.set_xlim(0,w)
    ax.set_ylim(0,h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()