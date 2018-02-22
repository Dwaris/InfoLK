#input
a = int(input("Jahre der Bervölerungsentwicklung: "))

g_0_14  = 12.3
g_15_49 = 39.1
g_50_64 = 15.5
g_65    = 16.3
#process

for i in range(a):
    h1 = (g_0_14*0.93)+(g_15_49*0.02) 
    h2 = (g_0_14*0.066)+(g_15_49*0.97)
    h3 = (g_15_49*0.029)+(g_50_64*0.925)
    h4 = (g_50_64*0.066)+(g_65*0.972)

    g_0_14  = h1
    g_15_49 = h2
    g_50_64 = h3
    g_65    = h4
#output
print("Es gibt {} Millionen  0-14 Jährige\nEs gibt {} Millionen 15-49 Jährige\nEs gibt {} Millionen 50-64 Jährige\nEs gibt {} Millionen ü. 65 Jährige\n".format(round(g_0_14, 1), round(g_15_49, 1), round(g_50_64, 1), round(g_65, 1)))
