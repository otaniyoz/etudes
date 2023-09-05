import numpy
import matplotlib
import matplotlib.pyplot

def main():
  r = 8
  n = 720 
  frames = 360 
  circle = numpy.linspace(0, 2*numpy.pi, 2*n)
  rng = numpy.random.default_rng()
  rads = rng.choice(circle, n)
  v = numpy.zeros((3,2,n))
  vi = r * rng.random((2,n))
  a = rng.random((2,n))
  vi[1,:] /= 2
  a[0,:] *= 2
  a[1,:] /= 2
  a = numpy.clip(a, 0.05, 0.5)

  cmap_keys = numpy.linspace(0, 1, n)
  cmap = matplotlib.cm.get_cmap("jet")
  c = numpy.clip(rng.random((n,4)), 0, 0.75)

  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0, 0, 0))
  for frame in range(frames):
    ax.clear()
    ax.axis("off")
    ax.set_xlim(-r, r)
    ax.set_ylim(-r, r)
    ax.set_aspect("equal")
    off = numpy.clip(vi[0,:] / r / 100, 0, 1)
    c_shift = int(n * frame / frames) 
    c[...,:3] = cmap(numpy.roll(cmap_keys, c_shift))[:,:3]
    v[0,0,:] = vi[0,:] * numpy.cos(rads - off) 
    v[0,1,:] = vi[0,:] * numpy.sin(rads - off) 
    v[1,0,:] = vi[1,:] * numpy.cos(rads) 
    v[1,1,:] = vi[1,:] * numpy.sin(rads)
    v[2,0,:] = vi[0,:] * numpy.cos(rads + off) 
    v[2,1,:] = vi[0,:] * numpy.sin(rads + off)
    for i in range(n):
      ax.add_patch(matplotlib.pyplot.Polygon(v[...,i], color=c[i,...]))
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)
    vi += a
    mask = vi[1,:] > r
    vi[1,:][mask] = 0
    vi[0,:][mask] = r * rng.random(len(vi[1,:][mask])) 

if __name__ == "__main__":
  main()