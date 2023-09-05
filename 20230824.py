import numpy
import matplotlib.pyplot

def main():
  max_length = 30 
  w, h = 400, 300
  num_frames = 150
  num_wormys = 200 
  rng = numpy.random.default_rng()
  cmap = matplotlib.cm.get_cmap("jet")
  markers = ["+", "x", "."]
  wormys = [{"t_0":0, "t_1":0, "x_offset":-3*w*rng.random(), "color":cmap(rng.random())[:3], "row":h*rng.random(), "length":int(max_length*rng.random()+3), "marker":rng.choice(markers)} for _ in range(num_wormys)]
  frames = numpy.arange(0, num_frames, 1)
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    for wormy in wormys:
      if frame%wormy["length"] == (wormy["length"]-1):
        wormy["t_0"] += 8*(wormy["length"]-1)
        continue
      wormy["t_1"] = wormy["t_0"] + 8*(frame%wormy["length"])
      x = numpy.linspace(wormy["t_0"], wormy["t_1"], frame%wormy["length"]+1)
      y = wormy["row"]*numpy.ones((len(x),))
      matplotlib.pyplot.scatter(x + wormy["x_offset"], y, s=64, color=wormy["color"], marker=wormy["marker"])
    ax.set_xlim(0,w)
    ax.set_ylim(0,h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()