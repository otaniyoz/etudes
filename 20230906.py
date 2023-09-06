import math
import numpy
import scipy.ndimage
import matplotlib.pyplot
import matplotlib.font_manager
matplotlib.font_manager._rebuild()

def main():
  s = "IN CODE"
  s1 = s
  w, h = 400, 300
  num_frames = 300
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  a, b, c = 0.5, numpy.linspace(0, 1, 100), 1 
  off = 10*scipy.ndimage.gaussian_filter(rng.random((num_frames, 100)), sigma=12.4)
  matplotlib.rcParams["font.family"] = "Raleway"
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    ax.text(0.1*w, 0.38*h, "ETUDES", size=64, color=(0.95,0.95,0.98))
    ax.text(0.1*w, 0.1*h, "IN C   DE", size=64, color=(0.95,0.95,0.98))
    theta = numpy.linspace(0, 7*math.pi, 100) + math.pi*frame/num_frames
    r = a + b * theta**(1/c) + off[frame] 
    x = r * numpy.cos(theta) + 0.52*w
    y = r * numpy.sin(theta) + 0.2*h
    ax.plot(x, y, color="orangered", lw=4, antialiased=True)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()