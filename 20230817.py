import math
import numpy
import matplotlib
import scipy.ndimage
import matplotlib.pyplot

def sng(w):
  w = numpy.where(w < 0, -1, w)
  w = numpy.where(w == 0, 0, w)
  w = numpy.where(w > 0, 1, w)
  return w

def get_rotation_matrix(rad):
  return numpy.array([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])

def main():
  a = 16 
  b = 16
  m = 12 
  k = 0.1 
  sigma = 25 
  n = int(10e2)
  TWOPI = 2 * math.pi
  PI180 = math.pi / 180
  number_of_frames = 605 
  width, height = 464, 464 

  cmap = matplotlib.cm.get_cmap("cool")
  cmap_keys = numpy.linspace(0, 1, m)
  ks = numpy.linspace(2, 1, m)
  alphas = numpy.linspace(0.005, 1, a)
  t = numpy.linspace(0, width, n)
  x = numpy.zeros((n, m))
  y = numpy.zeros((n, m))
  cost = numpy.cos(t)
  sint = numpy.sin(t)
  Ax = numpy.abs(cost)
  Ay = numpy.abs(sint)
  Bx = sng(cost)
  By = sng(sint)

  rng = numpy.random.default_rng()
  random_xy = (width // 2) * rng.random((number_of_frames, 2))
  random_xy[:,0] = (sigma // 4) * numpy.cos(TWOPI * random_xy[:,0])
  random_xy[:,1] = (sigma // 4) * numpy.sin(TWOPI * random_xy[:,1])

  xy = numpy.zeros(random_xy.shape)
  xy[:,0] = width // 2 - a // 2 * scipy.ndimage.gaussian_filter(random_xy[:,0], sigma=sigma)
  xy[:,1] = height // 2 - b // 8 * scipy.ndimage.gaussian_filter(random_xy[:,1], sigma=sigma)

  fig, ax = matplotlib.pyplot.subplots()
  fig.set_facecolor((0, 0, 0))
  for frame in range(number_of_frames):
    ax.clear()
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-2 * width, 2 * width)
    ax.set_ylim(-1.5 * height, 1.5 * height)

    c_shift = int(m * math.sin(math.pi / 4 * frame / number_of_frames))
    c = cmap(numpy.roll(cmap_keys, c_shift))[:,:3]
    for i, k in enumerate(ks):
      p = 2 / k
      x[:,i] = Ax**p * (a * i + k / (i + 1)) * Bx + xy[frame,0] 
      y[:,i] = Ay**p * (b * i + k / (i + 1)) * By + xy[frame,1]
      rad = frame * (PI180 + k / (8 * math.sin(frame * PI180) + 24))
      T = get_rotation_matrix(rad)
      _xy = T@numpy.array([x[:,i], y[:,i]])

      for alpha in alphas:
        ax.plot(_xy[0,:], _xy[1,:], antialiased=True, color=c[i], alpha=alpha, linewidth=2/alpha)

    matplotlib.pyplot.savefig(f"frames/{frame:03d}.png", dpi=300, bbox_inches="tight", pad_inches=0.0)

if __name__ == "__main__":
  main()
