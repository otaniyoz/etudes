import math
import numpy
import itertools
import matplotlib.pyplot

def main():
  n = 4
  w, h = 400, 300
  num_frames = 300
  rng = numpy.random.default_rng()
  rr = rng.integers(4,20,(2*n,n,n))
  off = 0.1*w*(2*rng.random((2*n,n,n))-1)
  frames = numpy.arange(0, num_frames, 1)
  fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection":"3d"})
  ax.set_facecolor((0,0,0))
  for frame in frames:
    ax.clear()
    ax.axis("off")
    ax.view_init(-360*frame/num_frames,360*frame/num_frames)
    for ii, i in enumerate(numpy.linspace(-5*w,5*w,2*n)):
      for ij, j in enumerate(numpy.linspace(-1.5*w,1.5*h,n)):
        for ik, k in enumerate(numpy.linspace(-1.5*w,1.5*w,n)):
          r = [-rr[ii,ij,ik],rr[ii,ij,ik]]
          for s, e in itertools.combinations(numpy.array(list(itertools.product(r,r,r))), 2):
            if numpy.sum(numpy.abs(s-e)) == r[1]-r[0]:
              x, y, z = zip(s,e)
              x = numpy.array(x)
              y = numpy.array(y)
              z = numpy.array(z) 
              ax.plot3D(x+i+w*(math.sin(2*math.pi*frame/num_frames)+1)/2 + off[ii,ij,ik], y+j+off[ii,ij,ik], z+k+off[ii,ij,ik], color="red") 
    ax.set_xlim(0,w)
    ax.set_ylim(0,w)
    ax.set_zlim(0,h)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=100, bbox_inches="tight", pad_inches=0.0)


if __name__ == "__main__":
  main()
