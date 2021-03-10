class Student():
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

    def display_student(self):
        return("Nom : {0} \nPrenom : {1} \nNote : {2} \n------".format(self.last_name, self.first_name, self.score))

    def change_student_score(self):
        """ Modification ou non de la note de l'étudiant sur la compétence projet et enregistrement de la nouvelle valeur. 
        """
        new_score_choice = str(input('Voulez-vous changer la note de {0} ?(Y/N)'.format(self.first_name)))
        if(new_score_choice.lower() == 'y'):
                try:
                    new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
                    if new_score >= 1 and new_score <= 5 :
                        self.score = new_score
                        print('Changement de la note effectué.')
                    else:
                        while (new_score < 1 or new_score > 5) :
                            print('Veuillez indiquer un entier compris entre 1 et 5')
                            new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
                except ValueError:
                    print('Veuillez indiquer un entier compris entre 1 et 5')
                    new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
        elif(new_score_choice.lower() != ('n' and '')):
                print('Erreur de saisie, veuillez tapez \'y\' pour modifier la note ou \'n\' pour passer')
                new_score_choice = str(input('Voulez-vous changer la note de {0} ?(Y/N)'.format(self.first_name)))