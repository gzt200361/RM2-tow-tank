UNH RM2 tow tank experiment
===========================

This is a repository for data and processing code from the UNH RM2 tow tank
experiment.


## Getting started

We recommend using the
[Anaconda Python distribution](http://continuum.io/downloads)
(Python 3.5) since it includes most dependencies. The remaining
can be installed by executing

    pip install progressbar33 pxl>=0.0.9 wget

After installing all dependencies, execute `python plot.py` to generate
figures from the experiment.


## Downloading raw data

By design, raw data will be downloaded automatically as needed by various
processing functions. However, it is possible to download all raw data (~10 GB)
by executing

    python Scripts/download.py


## Turbine model specs

|      | Full-scale | Model (1:6) |
|------|------------|-------------|
| Diameter (m)  | 6.450 | 1.075 |
| Height (m)    | 4.840 | 0.8067 |
| Blade root chord (m) | 0.4000 | 0.06667 |
| Blade tip chord (m)  | 0.2400 | 0.04000 |
| Blade profile | NACA 0021 | NACA 0021 |
| Blade mount | 1/2 chord | 1/2 chord |
| Blade pitch (deg.) | 0.0 | 0.0 |
| Strut profile | NACA 0021 | NACA 0021 |
| Strut chord (m) | 0.3600 | 0.06000 |
| Shaft diameter (m) | 0.2540 or 0.4160 | 0.06350 |


## Test matrix sections

Processed data is stored as CSV in the `Data/Processed` directory. One file is
generated per test matrix section, the descriptions for which are given below:

| Name | Description |
|------|-------------|
| `Perf-{speed}` | Performance curve at `{speed}` m/s tow speed, performed for (0.4, 0.6, 0.8, 1.0, 1.2) m/s. |
| `Perf-{speed}-b` | Second performance curve at `{speed}` m/s. |
| `Perf-1.0-covers` | Performance curve at 1.0 m/s tow speed with cylindrical strut covers. |
| `Perf-1.0-no-blades-covers` | Performance curve at 1.0 m/s with no blades and cylindrical strut covers. |
| `Perf-1.0-no-blades` | Performance curve at 1.0 m/s with no blades. |
| `Perf-tsr_0` | Performance at 3.1 tip speed ratio for multiple speeds. |
| `Perf-tsr_0-b` | Second set of runs with identical parameters as `Perf-tsr_0`. |
| `Strut-torque-covers` | Measuring torque from cylindrical struts (no towing). |
| `Strut-torque` | Measuring torque from NACA 0021 struts (no towing). |
| `Tare-drag` | Drag on the turbine mounting frame with the turbine removed. |
| `Tare-torque` | Measurements of friction torque in shaft bearings. |
| `Wake-{speed}-{z/H}` | Cross-stream wake profile at 1 m downstream (x/D = 0.93), 3.1 tip speed ratio, `{speed}` m/s tow speed, and `{z/H}` vertical location. |


## How to cite

Please cite

```bibtex
@Misc{Bachant2016-RM2-data,
  Title                    = {{UNH} {RM2} tow tank experiment: Reduced dataset and processing code},
  Author                   = {Peter Bachant and Martin Wosnik and Budi Gunawan and Vincent Neary},
  HowPublished             = {fig\textbf{share}. http://dx.doi.org/10.6084/m9.figshare.1373899},
  Year                     = {2016},
  Doi                      = {10.6084/m9.figshare.1373899},
}
```


## Publications

Bachant, P., Wosnik, M., Gunawan, B., and Neary, V. S. (2016) [Experimental Study of a Reference Model Vertical-Axis Cross-Flow Turbine](https://drive.google.com/file/d/0BwMVIAlxIxfZS29xNjk0OGpHbzQ/view?usp=sharing), Submitted to _PLOS ONE_


## Resources

* The test plan document is available from http://dx.doi.org/10.6084/m9.figshare.1373884
* Turbine manufacturing drawings and 3-D models are
available from http://dx.doi.org/10.6084/m9.figshare.1373870


## License

Code licensed under the MIT license. See `LICENSE` for details.
All other materials licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
Creative Commons Attribution 4.0 International License</a>.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" />
</a>
