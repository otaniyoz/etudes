import math
import numpy
import scipy.ndimage
import matplotlib.pyplot
import matplotlib.patheffects

def main():
  w = 320
  step = 8 
  num_frames = 300
  TWOPI = 2*math.pi
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  cmap = matplotlib.cm.get_cmap("prism")
  r = numpy.arange(1, w, step)
  tc = (0.98,0.98,0.95)
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect(1)
    frac = frame/num_frames
    t = ax.text(-0.95*w, -0.1*w, "Etudes", color=(*tc,rng.random()), weight="bold", size=60, zorder=-12, path_effects=[matplotlib.patheffects.withStroke(linewidth=1, foreground=(*tc,0.3*rng.random())), matplotlib.patheffects.withStroke(linewidth=2, foreground=(*tc,0.2*rng.random())), matplotlib.patheffects.withStroke(linewidth=3, foreground=(*tc,0.1*rng.random()))])
    for ri in r:
      cap = 2*ri
      c = cmap(ri/w)[:3]
      t = numpy.linspace(0, TWOPI, cap)
      off = step*math.sin(TWOPI*(ri/w+frac))
      x = ri*numpy.cos(t) + off 
      y = ri*numpy.sin(t) + off
      rgba = numpy.zeros((len(x),4))
      rgba[:,0] = c[0]
      rgba[:,1] = c[1]
      rgba[:,2] = c[2]
      a = rng.random((len(x),))
      rgba[:,3] = scipy.ndimage.gaussian_filter(a,2.4)
      ax.scatter(x, y, s=2*a, c=rgba, marker="o", antialiased=True, zorder=12)
    ax.set_xlim(-1.1*w,1.1*w)
    ax.set_ylim(-1.1*w,1.1*w)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()