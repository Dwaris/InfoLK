from xml.dom.minidom import *
doc = parse("limericks.svg")
k = doc
kLimerick = k.getElementsByTagName('tspan')
i=0
for k in kLimerick:
    if i%5 != 0:
        print(k.lastChild.nodeValue)
    if i%5 == 0 and i != 0:
        print("H")
    i +=1
