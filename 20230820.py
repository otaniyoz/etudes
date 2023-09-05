import math
import numpy
import scipy.ndimage
import matplotlib.pyplot

def main():
  a = 20
  sigma = 1.4
  num_frames = 300 
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames) 
  cmap = matplotlib.cm.get_cmap("afmhot")

  f = scipy.ndimage.gaussian_filter(rng.random((a,a,a)), sigma)
  x, y, z = numpy.indices(numpy.array(f.shape) + 1).astype(float)
  t = scipy.ndimage.gaussian_filter(rng.random((num_frames, *y.shape)), sigma)
  rgb = cmap(f)[...,:3]
  rgb = numpy.where(rgb <= 0.5, 1 - (1 - rgb) / (2*rgb + 1e-12), rgb / (2*(1 - rgb) + 1e-12))
  rgb = numpy.clip(rgb, 0, 1)

  fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection":"3d", "facecolor":(0,0,0)})
  for frame in frames:
    frac = frame / num_frames
    a_max_f = math.floor(frac*a)+1
    a_max = a_max_f 
    deg = 360*frac

    f2 = f[:-a_max_f,:-a_max_f,:-a_max_f]
    rgb2 = rgb[:-a_max_f,:-a_max_f,:-a_max_f]
    t2 = t[:,:-a_max,:-a_max,:-a_max]
    x2 = x[:-a_max,:-a_max,:-a_max]
    y2 = y[:-a_max,:-a_max,:-a_max]
    z2 = z[:-a_max,:-a_max,:-a_max]

    f2 = numpy.roll(f2, frame)
    off = 4*numpy.sin(t2[frame,...]*frac) 
    x2 += off
    y2 += off
    z2 += off

    ax.clear()
    ax.axis("off")
    ax.view_init(elev=30, azim=360*frac)
    if a_max < a: ax.voxels(x2, y2, z2, filled=f2, facecolors=rgb2)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()
