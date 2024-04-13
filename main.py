# TEAM (zimbabwe)
import requests
from bs4 import BeautifulSoup
import numpy as np

class Solution:
    unused_main_url = 'https://www.filgoal.com/teams/234/matches-results'
    def __init__(self , pageNumber, teamNumber):
        self.pageNumber = pageNumber
        self.teamNumber = teamNumber
        self.main_url = f'https://www.filgoal.com/teams/{teamNumber}/matches?isResults=true&pageNumber={self.pageNumber}' #constant
        self.golas_scored = np.array([])  
        self.goals_conceded = np.array([])
        self.all_match = [] # list to store match
        self.all_goals_scored = []
        self.all_goals_conserned = []
    
    def load_data (self):
        self.store_match_in_list()
    
    
    def store_match_in_list(self):
        for i in range(1,self.pageNumber+1):
            response = requests.get(f'https://www.filgoal.com/teams/{self.teamNumber}/matches?isResults=true&pageNumber={i}')
            assert response.status_code == 200
            soup = BeautifulSoup(response.text , 'html.parser')
            match_container = soup.find('div' , {'id':'team-match-list'})
            match_card = match_container.find_all('div' , {'class' : 'cin_cntnr'})
            self.all_match.extend(match_card)
        
    
    def get_request (self):
        response = requests.get(self.main_url)
        assert response.status_code == 200
        soup = BeautifulSoup(response.text , 'html.parser')
        return soup
    
    def get_all_match_in_page (self):
        soup = self.get_request()
        match_container = soup.find('div' , {'id':'team-match-list'})
        match_card = match_container.find_all('div' , {'class' : 'cin_cntnr'})
        return match_card

    def get_goals_scored_from_list(self):
        if len(self.all_match) != 0:
            for i in range(len(self.all_match)):
                goal_scored = self.all_match[i].find('div', {'class': 'c-i-next'}).find('div', {'class': 'f'}).find('b').text.strip()
                if goal_scored != '-':
                    try:
                        goal_scored = int(goal_scored)
                        self.all_goals_scored.append(goal_scored)
                    except ValueError:
                        pass
        return self.all_goals_scored
      
    def get_goals_conserned_from_list(self):
        if len(self.all_match) != 0:
            for i in range(len(self.all_match)):
                goal_conceded = self.all_match[i].find('div', {'class': 'c-i-next'}).find('div', {'class': 's'}).find('b').text.strip()
                if goal_conceded != '-':
                    try:
                        goal_conceded = int(goal_conceded)
                        self.all_goals_conserned.append(goal_conceded)
                    except ValueError:
                        pass
        return self.all_goals_conserned

    def get_goals_scored (self):
        soup = self.get_all_match_in_page()
        for i in range(len(soup)):
            goal_scored = soup[i].find('div' , {'class' : 'c-i-next'}).find('div' , {'class':'f'}).find('b').text.strip()
            if goal_scored != '-' and isinstance(goal_scored , int): # check if match is played yet
                #self.golas_scored.append(int(goal_scored))
                self.golas_scored = np.append(self.golas_scored , int(goal_scored))
        
        return self.golas_scored
    
    def get_goals_conceded (self):
        soup = self.get_all_match_in_page()
        for i in range(len(soup)):
            goal_conceded = soup[i].find('div' , {'class' : 'c-i-next'}).find('div' , {'class':'s'}).find('b').text.strip()
            if goal_conceded != '-' and isinstance(goal_conceded , int): #cehck if match played yet
                # self.goals_conceded.append(int(goal_conceded))
                self.goals_conceded = np.append(self.goals_conceded , int(goal_conceded))
        return self.goals_conceded




#MAIN
fetch = Solution(10 , 13) #get Last 10 match or Get last match from page 10 && TEAM NUMBER

# use this code for get last 10 match
print('_____LAST 10 Match_____')
fetch.load_data()
golas_scored_list = fetch.get_goals_scored_from_list()
golas_conceded_list = fetch.get_goals_conserned_from_list()

print('AVG Goals LIST SCORED ' , np.mean(golas_scored_list))
print('AVG Goals LIST conserned ' , np.mean(golas_conceded_list))

# print(golas_scored_list)
# print(golas_conceded_list)


# print('\n\n_____LAST Page Match_____')
# Sfetch = Solution(10 , 13)
# goals_scored = Sfetch.get_goals_scored()
# goals_conceded = Sfetch.get_goals_conceded()
# print('AVG GOLAS SCORED ',np.mean(goals_scored))
# print('AVG GOLAS CONSERNED ',np.mean(goals_conceded))
# print('______')

# #print(goals_scored)
# # print(goals_conceded)





