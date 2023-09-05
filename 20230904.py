import math
import numpy
import matplotlib.pyplot

def main():
  n = 64
  a = 320
  num_frames = 300
  rng = numpy.random.default_rng()
  cmap = matplotlib.cm.get_cmap("magma")
  frames = numpy.arange(0, num_frames, 1)
  fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection":"3d"})
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.view_init(elev=0, azim=0)

    rad = 2 * math.pi * frame / num_frames / 8 
    scl = (math.cos(rad) + 1) / 8 

    for i in numpy.arange(-2*a, 2*a, 80):
      for k in numpy.arange(-2*a, 2*a, 270):
        ax.text(x=-a, y=k+i//10, z=i, s="Etudes ", size=32, weight="bold", color=cmap(math.cos(2*math.pi*((i+k+4*a)/(8*a)+frame/num_frames))), zorder=-12) 

    r = numpy.linspace(0, math.pi, n)
    p = numpy.linspace(0, 2*math.pi, n) + rad 
    R, P = numpy.meshgrid(r, p)
    X1, Y1 = R*numpy.cos(P), R*numpy.sin(P)
    Z1 = ((R**2 - 1)**2)
    ax.plot_surface(a//2*X1+a//2, a//2*Y1+a//2, a//2*Z1+a//2, color="black", edgecolor="white", antialiased=True, zorder=12)

    r = numpy.linspace(0, math.pi, n)
    p = numpy.linspace(0, 2*math.pi, n) - rad 
    X2 = numpy.outer(numpy.cos(p), numpy.sin(r))
    Y2 = numpy.outer(numpy.sin(p), numpy.sin(r))
    Z2 = numpy.outer(numpy.ones(p.size), numpy.cos(r))
    ax.plot_surface(a//2*X2-a//2, a//2*Y2-a, a//2*Z2-a, color="black", edgecolor="white", antialiased=True, zorder=12)
    
    ax.set_xlim(-a/2, a/2)
    ax.set_ylim(-a/2, a/2)
    ax.set_zlim(-a/2, a/2)
    ax.set_facecolor((0,0,0))
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()
