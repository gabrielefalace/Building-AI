countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    tot_fishers = sum(fishers)

    #P(country|fisher) = fishers_country / fishers_total

    #probs = map(lambda (i, el): fishers[i]/tot_fishers, enumerate(populations))
    probs = [fishers[i]/tot_fishers for i in range(0, len(countries))]

    index = 0
    maxi = probs[0]
    for i, e in enumerate(probs):
        if e > maxi:
            maxi = e
            index = i

    guess = countries[index]
    biggest = maxi * 100
    return (guess, biggest)

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
