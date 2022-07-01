
import profiniy_calculator as pc

racial_slurs = {
    ('hate', 'X') : 1,
    ('Y', 'back', 'country') : 2,
    ('D', 'love' ,'E') : 1.5,
    ('M', 'G', 'love') : 1,
    ('X', 'go', 'C') : 2.5
}

path = "resouces/sampleTweets.csv"

def profinity_checker(racial_slurs, path):

    profin_cal = pc.Profinity_calculator(racial_slurs)

    csv = profin_cal.read_csv(path)

    profin_score = profin_cal.profin_calculator(csv)

    profin_ranks = profin_cal.profin_ranker(profin_score)

    profin_cal.print_results(csv,profin_ranks)


profinity_checker(racial_slurs, path)