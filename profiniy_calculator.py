import csv
import re

class Profinity_calculator:
    profin_words = {}
    def __init__(self, profin_words):
        self.profin_words = profin_words

    def read_csv(self, path):
        csv_list = []
        if path != None and '.csv' == path[-4:]:
            with open(path, mode ='r')as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    csv_list.append(line)
        return csv_list[1:]


    def pattern_matching(self, words, index, sentence):
        if words == None or len(words) == 0 or index == None or str(index).isnumeric() == False or sentence == None:
            return 0
        search_list = re.split(words[index], sentence)[1:]
        if search_list == []:
            return 0
        index += 1
        if len(words) == index:
            return 1
        for sentence in search_list:
            if self.pattern_matching(words, index, sentence) == 1:
                return 1
        return 0


    def profin_calculator(self, csv):
        if csv == [] or csv == None:
            return 0
        scores = []
        for row in csv:
            score = 0
            for words, profin_score in self.profin_words.items():
                if self.pattern_matching(words, 0, row[1]) == 1:
                    score += profin_score
            scores.append(score)

        return scores

    def profin_ranker(self, scores):
        remarks = []
        if scores == None:
            return  remarks
        for score in scores:
            if score == 0:
                remarks.append('None')
            if score > 0 and score <= 1:
                remarks.append('Low')
            if score > 1 and score <= 2:
                remarks.append('Moderate')
            if score > 2:
                remarks.append('Extreme')
        return remarks

    def print_results(self, csv, rank):
        print('User', '\t', 'Tweet', '\t', 'rank')
        for i in range(0,len(csv)):
            print(csv[i][0], '\t', csv[i][1], '\t', rank[i])




