import math
import numpy
import scipy.ndimage
import matplotlib.pyplot

def main():
  n = int(10e2)
  num_frames = 180
  w, h = 320, 320
  TWO_PI = 2*math.pi
  rng = numpy.random.default_rng()
  frames = numpy.arange(0, num_frames, 1)
  cmap = matplotlib.cm.get_cmap("coolwarm")
  s = TWO_PI*rng.random((n,)) + 1
  a = rng.random((n,))
  c = cmap(2*a-0.5)
  c[:,3] = a**2
  c[:,:3] = numpy.where(c[:,:3] <= 0.5, 1 - (1 - c[:,:3]) / (2*c[:,:3]), c[:,:3]/(2*(1 - c[:,:3])))
  c[:,:3] = numpy.clip(numpy.square(c[:,:3]+1), 0, 1)
  x = 2*w*(2*rng.random((n,))-1)
  y = 2*h*(2*rng.random((n,))-1)
  sigma = 24 
  area = w * h
  max_blob_r = 250
  blobs_xy = rng.choice(area, (h//2, 2), replace=False) / area
  blobs_xy[:,0] = 2*w*blobs_xy[:,0] - w
  blobs_xy[:,1] = 2*h*blobs_xy[:,1] -h
  blobs_r = rng.integers((max_blob_r//2, max_blob_r), size=(h//2, 1)) / max_blob_r
  grid_xy = numpy.indices((2*w, 2*h))-w
  random_xy = rng.random((h//2, 2))
  random_xy[:,0] = (sigma//4) * numpy.cos(TWO_PI*random_xy[:,0])
  random_xy[:,1] = (sigma//4) * numpy.sin(TWO_PI*random_xy[:,1])
  xy = numpy.zeros(random_xy.shape)
  for blob in range(h//2):
    scale = numpy.clip(1 / (blobs_r[blob] + 1e-10), 1, 16)
    xy[blob,0] = scale * scipy.ndimage.gaussian_filter(random_xy[blob,0], sigma=sigma)
    xy[blob,1] = scale * scipy.ndimage.gaussian_filter(random_xy[blob,1], sigma=sigma)
  grid_color = numpy.zeros((2*w, 2*h))
  for blob in range(h//2):
    blobs_xy[blob,0] += xy[blob,0] 
    blobs_xy[blob,1] += xy[blob,1]
    if blobs_xy[blob,0] > w + blobs_r[blob]: blobs_xy[blob,0] = -blobs_r[blob]
    if blobs_xy[blob,1] > h + blobs_r[blob]: blobs_xy[blob,1] = -blobs_r[blob]
    d = numpy.sqrt(numpy.square(blobs_xy[blob,0] - grid_xy[0,...]) + numpy.square(blobs_xy[blob,1] - grid_xy[1,...]))
    grid_color += blobs_r[blob] / (d + 1)
  grid_color = numpy.where(grid_color <= 0.5, 1 - (1 - grid_color) / (2*grid_color), grid_color / (2*(1 - grid_color)))
  grid_color = numpy.clip(numpy.square(grid_color-0.75), 0, 0.25)
  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0,0,0))
  ax.scatter(grid_xy[0,...], grid_xy[1,...], s=1, marker="s", c=grid_color, alpha=0.15, cmap="twilight_shifted", antialiased=True, zorder=-12)
  for frame in frames:
    ax.axis("off")
    ax.set_aspect(1)
    ax.set_xlim(-w,w)
    ax.set_ylim(-h,h)
    frac = frame/num_frames
    rad = TWO_PI*frac/4
    T = numpy.array([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
    xy_r = T@numpy.array([x, y])
    ax.scatter(xy_r[0,:], xy_r[1,:], s=s, c=c, antialiased=True, zorder=12)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()