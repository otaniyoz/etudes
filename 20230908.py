import math
import numpy
import matplotlib.pyplot
import matplotlib.font_manager
matplotlib.font_manager._rebuild()

def main():
  r = 100
  s1 = "ETUDES"
  w, h = 320, 320
  num_frames = 300
  bg = (0.95,0.95,0.98)
  t = numpy.linspace(0,2*math.pi,len(s1)+1)
  x = r*numpy.cos(t) + w//2 - 32 
  y = r*numpy.sin(t) + h//2 - 16 
  rng = numpy.random.default_rng()
  off = 360*rng.random((len(s1),))
  frames = numpy.arange(0, num_frames, 1)
  matplotlib.rcParams["font.family"] = "Raleway"
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor(bg)
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    frac = frame/num_frames
    for i, c in enumerate(s1):
      ax.text(x[i], y[i], c, size=48, color=bg, weight="bold", rotation=off[i]*(frame/num_frames+1),zorder=12)
    ax.scatter(w//2,h//2,s=5*r**2,color="black",zorder=-12)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()
