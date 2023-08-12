import numpy
import scipy.ndimage
import matplotlib.pyplot


def main():
  sigma = 24 
  width = 400
  height = 300
  max_blob_r = 250
  number_of_frames = 360 
  area = width * height
  rng = numpy.random.default_rng()
  blobs_xy = rng.choice(area, (height // 2, 2), replace=False) / area
  blobs_xy[:,0] = blobs_xy[:,0] * width
  blobs_xy[:,1] = blobs_xy[:,1] * height
  blobs_r = rng.integers((max_blob_r // 2, max_blob_r), size=(height // 2, 1)) / max_blob_r
  grid_xy = numpy.indices((width, height))
  random_xy = rng.random((number_of_frames, height // 2, 2))
  random_xy[:,:,0] = (sigma // 4) * numpy.cos(7 * random_xy[:,:,0])
  random_xy[:,:,1] = (sigma // 4) * numpy.sin(7 * random_xy[:,:,1])
  xy = numpy.zeros(random_xy.shape)
  for blob in range(height // 2):
    scale = numpy.clip(1 / (blobs_r[blob] + 1e-10), 1, 16)
    xy[:,blob,0] = scale * scipy.ndimage.gaussian_filter(random_xy[:,blob,0], sigma=sigma)
    xy[:,blob,1] = scale * scipy.ndimage.gaussian_filter(random_xy[:,blob,1], sigma=sigma)

  fig, ax = matplotlib.pyplot.subplots()
  for frame in range(number_of_frames):
    grid_color = numpy.zeros((width, height))
    for blob in range(height // 2):
      blobs_xy[blob,0] += xy[frame,blob,0] 
      blobs_xy[blob,1] += xy[frame,blob,1]
      if blobs_xy[blob,0] > width + blobs_r[blob]: blobs_xy[blob,0] = -blobs_r[blob]
      if blobs_xy[blob,1] > height + blobs_r[blob]: blobs_xy[blob,1] = -blobs_r[blob]
      d = numpy.sqrt(numpy.square(blobs_xy[blob,0] - grid_xy[0,...]) + numpy.square(blobs_xy[blob,1] - grid_xy[1,...]))
      grid_color += blobs_r[blob] / (d + 1)
    grid_color = numpy.where(grid_color <= 0.5, 1 - (1 - grid_color) / (2*grid_color), grid_color / (2*(1 - grid_color)))
    grid_color = numpy.clip(numpy.square(grid_color), 0, 1)
    ax.clear()
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.scatter(grid_xy[0,...], grid_xy[1,...], s=1, marker="s", c=grid_color, cmap="viridis", antialiased=True)
    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=height, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()