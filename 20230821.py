import numpy
import scipy.ndimage
import matplotlib.pyplot

def main():
  n = 18 
  m = 64  
  size = 320 
  s = "Etudes"
  num_frames = 300
  TWOPI = 2*numpy.pi
  frame_size = 0.5*size
  r = numpy.linspace(size, 0, m)
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  rad = numpy.linspace(0, TWOPI, n)
  cmap = matplotlib.cm.get_cmap("jet")
  rgb = cmap(frames)[...,:3]
  scl = numpy.linspace(24, 0, m)

  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0, 0, 0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-frame_size, frame_size)
    ax.set_ylim(-frame_size, frame_size)
    ax.text(-0.8*frame_size, -0.1*frame_size, s, weight="bold", size=55, color=(0.98,0.98,0.95), bbox={"facecolor":(0,0,0)})
    frac = TWOPI*frame/num_frames
    for i in range(m):
      o = scl[i]*numpy.sin(TWOPI*(r[i] + i/m + frac))*frame/num_frames
      xi = r[i]*numpy.cos(rad + frac) + o
      yi = r[i]*numpy.sin(rad + frac) + o
      ax.scatter(xi, yi, edgecolor=None, facecolor=rgb[frame], marker="o", s=128, antialiased=True)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()