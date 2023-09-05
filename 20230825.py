import numpy
import matplotlib.pyplot
import matplotlib.font_manager
# matplotlib.font_manager._rebuild()

def main():
  s = "IN CODE"
  s1 = s
  w, h = 400, 300
  num_frames = 300
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  char_map = {"I":"1", "O":"0", "E":"3", "N":"#", "C":"@", "D":"%", " ":"_"}
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    if frame > 29 and frame % 30 == 0: 
      s1 = s
      chars = [s[i] for i in rng.choice(list(range(len(s))), size=rng.integers(3), replace=False)]
      for c in chars: s1 = s1.replace(c, char_map[c])
    matplotlib.rcParams["font.monospace"] = "IBM Plex Mono"
    matplotlib.rcParams["font.family"] = "monospace"
    ax.text(0.1*w, 0.1*h, s1, size=48, color=(0.7,0.2,0.25))
    matplotlib.rcParams["font.cursive"] = "Caveat"
    matplotlib.rcParams["font.family"] = "cursive"
    ax.text(0.1*w, 0.28*h, "Etudes", size=64, color=(0.95,0.95,0.98))
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()