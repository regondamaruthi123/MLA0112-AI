disease(fever,viral_fever).
disease(cough,cold).
disease(headache,migraine).

diagnose(S,D):-
    disease(S,D).