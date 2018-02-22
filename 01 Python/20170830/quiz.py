#process
def get_int(answer, lo=None, hi=None):
    while True:
        try:                                                                        #pass empty answers
            val = int(input(answer))
            if (lo is None or lo <= val) and (hi is None or val <= hi):             #check input 
                return val
        except ValueError:
            pass
        
def ask(question, options, correct_answer, right_points=1, wrong_points=0):
    print(question)                                                                
    for i, opt in enumerate(options, 1):                                            #count answers for one question
        print("{} {}".format(i, opt))                                               #print questions and answers
    ans = get_int("", 1, len(options))                                              #check answer
    return right_points if ans == correct_answer else wrong_points                  #points

#input
print("Jede Frage bringt dir einen Punkt:\n")
total = (
      ask("Wer würde die NPD wählen?",                                       ["John F. Kennedy", "Martin Luther", "Abraham Lincoln"],              2)
    + ask("Was ist 2*3*6*8*3?",                                              ["864", "1,392", "1,568"],                                            1)
    + ask("Was ist die Antwort auf alle Fragen?",                            ["42", "1588", "88"],                                                 1)
    + ask("Wieso war Merkel auf der Gamescom?",                              ["verirrt", "Erschließung des Neulands", "Eröffnung"],                3)
    + ask("Was darf man nie vergessen?",                                     ["Smartphone", "Handtuch", "Geldbeutel"],                             2) 
    + ask("Was ist der Hauptgrund, die Partei zu wählen",                    ["Parteiführer", "Plakate", "Bier"],                                  3)
    + ask("Welches Betriebssystem ist kein optimales Betriebssystem?",       ["Windows", "Linux", "macOS"],                                        1)
)

#output
if i == total:
    print("TOLL")
print("Du hast {} Fragen korrekt beantwortet, deine Punktzahl beträgt {} Punkte.".format(total, total))
