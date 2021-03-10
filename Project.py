class Project():
    def __init__(self, project_name, project_skill, project_distribution, project_group_size):
        self.project_name = project_name
        self.project_skill = project_skill
        self.project_distribution = project_distribution
        self.project_group_size = project_group_size
        
    def display_project(self):
        return("Nom du projet : {0} \nCompétence associée : {1} \nNiveau des groupes : {2} \nTaille des groupes : {3} ------"
               .format(self.project_name, self.project_skill, self.project_distribution, self.project_group_size))


