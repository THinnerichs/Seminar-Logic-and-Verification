## -*- encoding: utf-8 -*-
## This file (presentation.sagetex.sage) was *autogenerated* from presentation.tex with sagetex.sty version 2012/01/16 v2.3.3-69dcb0eb93de.
import sagetex
_st_ = sagetex.SageTeXProcessor('presentation', version='2012/01/16 v2.3.3-69dcb0eb93de', version_check=True)
_st_.blockbegin()
try:
try:
 _st_.inline(0, latex(f(x)))
except:
 _st_.goboom(196)
try:
 _st_.inline(1, latex(diff(f, x, 2)(x)))
except:
 _st_.goboom(196)
try:
 _st_.plot(0, format='notprovided', _p_=plot(f, -1, 1))
except:
 _st_.goboom(196)
_st_.endofdoc()
