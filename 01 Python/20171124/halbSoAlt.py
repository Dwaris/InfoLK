from kalender import *

geburtsDatum = (19, 10, 1978)
heutigesDatum = (29, 11, 2017)

alterInTagen = anzahlTage(geburtsDatum, heutigesDatum)
datumHalbSoAlt = datumNachTagen(geburtsDatum, alterInTagen // 2)

print(datumHalbSoAlt)
