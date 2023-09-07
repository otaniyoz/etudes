import numpy
import matplotlib.pyplot
import matplotlib.font_manager
matplotlib.font_manager._rebuild()

def main():
  fs = 64
  s1 = "ETUDES"
  s2 = "INCODE"
  w, h = 320, 320
  num_frames = 300
  r = (1,0,0,0.65)
  g = (0,1,0,0.65)
  b = (0,0,1,0.65)
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  off = 0.2*h*rng.random((len(s1)+len(s2),3))
  matplotlib.rcParams["font.family"] = "IBM Plex Mono"
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    frac = frame/num_frames
    for i, c in enumerate(s1):
      ax.text(fs*i, 0.6*h + off[i,0]*(1 - frac), c, size=fs, color=r)
      ax.text(fs*i, 0.6*h + off[i,1]*(1 - frac), c, size=fs, color=g)
      ax.text(fs*i, 0.6*h + off[i,2]*(1 - frac), c, size=fs, color=b)
    for i, c in enumerate(s2):
      if i < 2:
        ax.text(fs*i, 0.35*h + off[len(s1)+i,1]*(frac - 1), c, size=fs, color=g)
        ax.text(fs*i, 0.35*h + off[len(s1)+i,2]*(frac - 1), c, size=fs, color=b)
        ax.text(fs*i, 0.35*h + off[len(s1)+i,0]*(frac - 1), c, size=fs, color=r)
      else:
        ax.text(fs*i, 0.35*h + off[len(s1)+i,2]*(frac - 1), c, size=fs, color=b)
        ax.text(fs*i, 0.35*h + off[len(s1)+i,0]*(frac - 1), c, size=fs, color=r)
        ax.text(fs*i, 0.35*h + off[len(s1)+i,1]*(frac - 1), c, size=fs, color=g)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()
