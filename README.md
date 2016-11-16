# Galaxy
A simple Galactic model with a leapfrog integrator 

This repository contains 5 files:

  galaxy.py
  This is the file you run, in which everything is set up with "standard" values

  orbit.py
  This is the script that is called by galaxy that calls the integrator and saves the data, 
  doesn't need to be a seperete file but I prefer it this way

  potential.py
  Contains the gravitational potential. It is a symmetric potential with three parts: A Miyamoto & Nagai (1975) Disk and
  a Plummer (1911) Halo and Bulge, the values are of course newer

  leapfrog.py
  Contains a simple leapfrog integrator.

  orbcheck.py
  Has a few standard plots that checks that everything is ok.
  
You are free to do as you wish with this code, no assignment is given. Maybe you can learn a thing or two, if you do, you can
include it in your report (Perhaps a rotation curve, perhaps something else?). I will not view it in a negative way if
nothing from this is included in your report, but it could be a bonus if you include something.

/Giorgi
