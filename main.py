#-*- coding: utf-8 -*-
import Project
import Student
import functions
from student_list import json_student_list


if __name__ == "__main__":

    student_list = functions.create_student_list(json_student_list)
    
    project_name = str(input('Le nom de votre projet : '))
    project_skill = str(input('La compétence du projet : '))

    for student in student_list:
        print(student.display_student())
        student.change_student_score()
        print("Note : {0}".format(student.score))
        print('\n------')

    project_distribution = str(input('La répartition souhaitée (Hm pour Homogène, Ht pour hétérogène) : '))


    while(project_distribution.lower() != 'hm' and project_distribution.lower() != 'ht'):
        print('Erreur de saisie, indiquez "hm" pour une répartition homogène et "ht" pour une répartition hétèrogène des groupes')
        project_distribution = str(input('La répartition souhaitée (Hm pour Homogène, Ht pour hétérogène) : '))

    try:
        project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))
        while (project_group_size > 5 or project_group_size < 2) and (type(project_group_size) != int):
            print('Erreur de saisie, veuillez indiquez un nombre entier compris entre 1 et 5.')
            project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))
            
    except ValueError:
        print('Erreur de saisie, veuillez indiquez un nombre entier compris entre 1 et 5.')
        project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))

    # project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))
    new_project = Project.Project(project_name, project_skill, project_distribution, project_group_size)
    print(new_project.display_project())


    if project_distribution.lower() == "hm":
        print('------------')
        for student in functions.generate_homogeneous_list(student_list, project_group_size):
            print(student)
        print('------------')
    elif project_distribution.lower() == "ht":
        print('------------')
        for student in functions.generate_heterogeneous_list(student_list, project_group_size):
            print(student)
        print('------------')


