# libcerf

**libcerf** is a self-contained numeric library that provides an efficient and accurate implementation of complex error functions, along with Dawson, Faddeeva, and Voigt functions.

## Accuracy

By construction, it is expected that the relative accuracy is generally better than 1E-13. This has been confirmed by comparison with high-precision Maple computations and with a *long double* computation using Fourier transform representation and double-exponential transform.

## Copyright and Citation

Copyright (C) [Steven G. Johnson](http:*math.mit.edu/~stevenj), Massachusetts Institute of Technology, 2012; [Joachim Wuttke](http:*www.fz-juelich.de/SharedDocs/Personen/JCNS/EN/Wuttke_J.html), Forschungszentrum Jülich, 2013.

License: [MIT License](http://opensource.org/licenses/MIT)

When using libcerf in scientific work, please cite as follows:
  * S. G. Johnson, A. Cervellino, J. Wuttke: libcerf, numeric library for complex error functions, version [...], http://apps.jcns.fz-juelich.de/libcerf

Please send bug reports to the authors, or submit them through the Gitlab issue tracker.
