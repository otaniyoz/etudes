import numpy
import scipy.ndimage
import matplotlib.pyplot
import matplotlib.patheffects
import matplotlib.font_manager

def main():
  s = "Etudes"
  t = 16 
  fps = 30 
  frame = 0
  sigma = 0.42
  fontsize = 32
  w, h = 400, 300
  xy = [[x, 150] for x in numpy.linspace(0.2 * w, 0.75 * w, 6)]

  stop_list = []
  font_manager = matplotlib.font_manager.FontManager()
  available_fonts = [[f.__dict__["name"], int(f.__dict__["weight"])] for f in font_manager.__dict__["ttflist"] if f.__dict__["name"] not in stop_list]
  glow = [matplotlib.patheffects.withStroke(linewidth=1, foreground=(0.98,0.98,0.95,0.5)), matplotlib.patheffects.withStroke(linewidth=2, foreground=(0.98,0.98,0.95,0.2)), matplotlib.patheffects.withStroke(linewidth=3, foreground=(0.98,0.98,0.95,0.1))]

  rng = numpy.random.default_rng()
  fonts = rng.choice(available_fonts, size=(6, t))
  off = 2 * (2 * rng.random((2, t, 6)) - 1)
  x, y = numpy.indices((w, h))
  back = numpy.zeros((w, h))

  noise = rng.choice([0, 1], p=[0.3, 0.7], size=(w, h, t, fps))
  for ti in range(t):
    for fi in range(fps):
      noise[:,:,ti,fi] = scipy.ndimage.gaussian_filter(noise[:,:,ti,fi], sigma=sigma)

  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0, 0, 0))
  for ti in range(t):    
    ax.clear()
    ax.axis("off")
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")

    for i, l in enumerate(s):
      print(fonts[i,ti])
      matplotlib.rcParams["font.family"] = fonts[i,ti][0]
      ax.text(xy[i][0] + off[0,ti,i], xy[i][1] + off[1,ti,i], l, fontsize=fontsize, weight=fonts[i,ti][1], color=(0.98, 0.98, 0.95), path_effects=glow)
    
    for fi in range(fps):
      if fi % (rng.integers(1,fps)) == 0:
        mask = 1 - noise[:,:,ti,fi] < 0.5
        color = numpy.zeros((len(x[mask]), 4))
        color[:,:2] = 0.98
        color[:,2] = 0.95
        color[:,3] = 0.5 * rng.random(len(x[mask])) 
        ax.scatter(w//2,h//2, color=(0,0,0), s=142048, marker="s")
        ax.scatter(x[mask], y[mask], c=color, s=1, marker="s", antialiased=False)
      matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)
      frame += 1

if __name__ == "__main__":
  main()
