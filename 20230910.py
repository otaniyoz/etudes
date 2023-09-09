import math
import numpy
import scipy.ndimage
import matplotlib.pyplot

def main():
  w, h = 320, 320
  num_frames = 300
  rng = numpy.random.default_rng()
  cmap = matplotlib.cm.get_cmap("turbo")
  x = numpy.linspace(0.2*w,0.8*w,100)
  y = numpy.linspace(0.4*h,0.5*h,100)
  frames = numpy.arange(0, num_frames, 1)
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    ax.text(0.18*w,0.55*h,"Etudes",size=49,color=(0.95,0.95,0.98)) 
    for iy in y:
      ax.scatter(x, iy*numpy.ones(x.shape), c=cmap((numpy.sin(2*math.pi*(x/(0.6*w) + frame/num_frames))+1)/2), s=1, marker="s")
    ax.set_xlim(0,w)
    ax.set_ylim(0,h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()
