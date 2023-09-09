Etudes are small pieces of code with minimal dependecies that create self‑contained creative animations.

There are no strict rules to etudes, but here are some guidelines:
* code should be short and moderately optimized
* use of dependecies and off‑the‑shelf solutions should be minimal
* final result should be a sequence of frames that doesn’t require additional creative processing
* animation shouldn’t last more than five seconds and weigh more than a few mbs

Etudes are different from code golfing: they should not optimise for shorter code‑length at the cost of clarity and performance. They are also different from creative coding: etudes should try to maintain a healthy balance between code quality & performance and artistic vision.

I think, with these loose constraints, etudes are a healthier and a more enjoyable alternative to coding exercises and interview questions.

## Usage
### Etudes 20230722...20230909
These etudes assume a certain structure to folder. Specifically, there should a folder named `frames` on the level at which you execute the code. Paths are hardcoded, so if you want to change anything, you need to respect original conventions or update them.

These etudes were made using Python's numpy, matplotlib, scipy, and some standard libraries; they should run on any more or less recent version of Python, but I haven't done any tests to prove this claim. With dependecies sorted out, you should be able to run the code like so `python 20230722.py`.

Executing any of these etudes should create n-frames saved as `.png`s in `frames/`. These frames can be later animated with a tool like `ffmpeg`.

Some notes:
* These pieces of code should be readable, so read it before executing. Usually, etudes take around five minutes to make, hence are prone to bugs and mistakes.
* Some etudes use specific fonts. If you don't have these fonts installed on your system and available to matplotlib, matplotlib should default to stylistically closest available font. In general, all of the specific fonts should be available on google fonts.  
* Sometimes matplotlib is having a hard time finding some fonts, so I force rebuild font-cache. Depending on your setup this can take a while. As with the previous point, it is not necessary.
