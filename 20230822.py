import math
import numpy
import matplotlib.pyplot
import matplotlib.patheffects

def main():
  w, h = 300, 320
  num_frames = 300 
  frames = numpy.arange(0, num_frames)
  cmap = matplotlib.cm.get_cmap("jet")
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    frac = frame / num_frames
    f = 1 - frac
    ax.text(0.2*w, 0.5*h, "Etudes", color=cmap(0.5)[:3], weight="bold", size=42)
    for i in numpy.linspace(1, 0, 15):
      c = cmap(math.sin(2*math.pi*frac)+i+0.5)[:3]
      glow = [matplotlib.patheffects.withStroke(linewidth=1, foreground=(*c,(1-i)/3)), matplotlib.patheffects.withStroke(linewidth=2, foreground=(*c,(1-i)/4)), matplotlib.patheffects.withStroke(linewidth=3, foreground=(*c,(1-i)/5))]
      ax.text(0.2*w*(1-i), 0.5*h*(1-0.05*i), "Etudes", color=(*c,0.05*i), weight="bold", size=32*i + 42, path_effects=glow)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=320, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()