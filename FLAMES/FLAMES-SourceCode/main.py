from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI
import random


def calc(name1, name2):
    n1 = list(name1.lower())
    n2 = list(name2.lower())
    if len(n1) > len(n2):
        tem = n2
        n2 = n1
        n1 = tem
    ln1 = len(n1)
    ln2 = len(n2)
    for i in range(ln1):
        for j in range(ln2):
            if (n1[i] == n2[j]):
                n1[i] = '-'
                n2[j] = '-'
    count = 0
    for i in n1:
        if (i != '-'):
            count += 1
    for i in n2:
        if (i != '-'):
            count += 1
    res = 'o'
    if (count == 3 or count == 5 or count == 14 or count == 16 or count == 18 or count == 21 or count == 23):
        res = "FRIEND"

    elif (count == 10 or count == 19):
        res = "LOVER"

    elif (count == 8 or count == 12 or count == 13):
        res = "AFFECTIONATE"

    elif (count == 11 or count == 6 or count == 26 or count == 15):
        res = "MARRAGE"

    elif (
            count == 2 or count == 4 or count == 7 or count == 9 or count == 20 or count == 22 or count == 24 or count == 25):
        res = "ENEMY"

    elif (count == 1 or count == 17):
        res = "SISTER"

    else:
        res = "TOO LONG NAMES"

    friendship = [
        "Friendship is born at that moment when one person says to another: ‘What! You too? I thought I was the only one",
        "Nothing makes the earth seem so spacious as to have friends at a distance; they make the latitudes and longitudes.",
        "I would rather walk with a friend in the dark, than alone in the light.",
        "Friendship is the hardest thing in the world to explain. It’s not something you learn in school. But if you haven’t learned the meaning of friendship, you really haven’t learned anything.",
        "A friend is one that knows you as you are, understands where you have been, accepts what you have become, and still, gently allows you to grow.",
        "Find a group of people who challenge and inspire you; spend a lot of time with them, and it will change your life.",
        "A friend is one that knows you as you are, understands where you have been, accepts what you have become, and still, gently allows you to grow.",
        "Sweet is the memory of distant friends! Like the mellow rays of the departing sun, it falls tenderly, yet sadly, on the heart.",
        "Anybody can sympathise with the sufferings of a friend, but it requires a very fine nature to sympathise with a friend’s success.",
        "Don’t walk behind me; I may not lead. Don’t walk in front of me; I may not follow. Just walk beside me and be my friend.",
        "A true friend never gets in your way unless you happen to be going down."]
    love = ["Love is like heaven, but it can hurt like hell.",
            "Love is not a feeling, it’s an ability.",
            "One of the hardest things in life is having words in your heart that you can’t utter.",
            "One word frees us of all the weight and pain of life — that word is love.",
            "Life without love is like a tree without blossoms or fruit.",
            "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart.",
            "It's better to have loved and lost than never to have loved at all.",
            "You know you're in love when you can't fall asleep because reality is finally better than your dreams.",
            "Love recognizes no barriers. It jumps hurdles, leaps fences, penetrates walls to arrive at its destination full of hope.",
            "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
            "All you need is love. But a little chocolate now and then doesn’t hurt."]
    affection = ["Affection reproaches, but does not denounce. ",
                 "Any love or happiness given to anyone always comes back. Unfortunately we expect it from the same person.",
                 "Love is one of the strongest feelings one can ever have. It comes over you all of a sudden and totally absorbs before you manage to realize the fact.",
                 "Never regret anything you have done with a sincere affection; nothing is lost that is born of the heart.",
                 "We become what we behold.",
                 "Affection should not be too sharp eyed, and love is not made by magnifying glasses.",
                 "The hardest of all is learning to be a well of affection, and not a fountain; to show them we love them not when we feel like it, but when they do",
                 "Affection expressed physically made friendship so complete and binding.",
                 "Affection is like the noonday sun; it does not need the presence of another to be manifest.",
                 "Real living is living for others.",
                 "There is no power greater than true affection."]
    marrage = ["The great marriages are partnerships. It can’t be a great marriage without being a partnership.",
               "Husband and wife relationships are like the relationship of Tom and Jerry. Though they are teasing and fighting, but can’t live without each other.",
               "A husband and wife may disagree on many things but they must absolutely agree on this: to never, ever give up.",
               "A successful marriage requires falling in love many times, always with the same person.",
               "A great marriage is not when the ‘perfect couple’ comes together. It is when an imperfect couple learns to enjoy their differences.",
               "Never marry the one you can live with, marry the one you cannot live without.",
               "A good marriage is one which allows for change and growth in the individuals and in the way they express their love.",
               "Marriage is not about age; it’s about finding the right person.",
               "Experts on romance say for a happy marriage there has to be more than a passionate love. For a lasting union, they insist, there must be a genuine liking for each other. Which, in my book, is a good definition for friendship.",
               "True love stands by each other’s side on good days and stands closer on bad days.",
               "Love is not weakness. It is strong. Only the sacrament of marriage can contain it."]

    enemy = ["Always forgive your enemies; nothing annoys them so much.",
             "Now, now my good man, this is no time to be making enemies",
             "Always forgive your enemies; nothing annoys them so much.",
             "I ask you to judge me by the enemies I have made.",
             "We do not merely destroy our enemies.",
             "Now, now my good man, this is no time to be making enemies",
             "Always forgive your enemies; nothing annoys them so much.",
             "We do not merely destroy our enemies.",
             "I ask you to judge me by the enemies I have made.",
             "Now, now my good man, this is no time to be making enemies",
             "Now, now my good man, this is no time to be making enemies"]

    sister = [
        "Having a sister is like having a best friend you can’t get rid of. You know whatever you do, they’ll still be there.",
        "I could never love anyone as I love my sisters.",
        "A sister can be seen as someone who is both ourselves and very much not ourselves—a special kind of double.",
        "Acquaintances were always on their best behavior, but sisters loved each other enough to say anything.",
        "Sisters make the best friends in the world.",
        "Is solace anywhere more comforting than that in the arms of a sister?",
        "In the cookies of life, sisters are the chocolate chips.",
        "Sisters function as safety nets in a chaotic world simply by being there for each other.",
        "Sweet is the voice of a sister in the season of sorrow.",
        "There is no place for secrets in sisterhood.",
        "A sister is both your mirror—and your opposite."]

    rand = random.randrange(0, 10)
    if (res == 'FRIEND'):
        quote = friendship[rand]
    elif (res == 'LOVER'):
        quote = love[rand]
    elif (res == 'AFFECTIONATE'):
        quote = affection[rand]
    elif (res == 'MARRAGE'):
        quote = marrage[rand]
    elif (res == 'ENEMY'):
        quote = enemy[rand]
    elif (res == 'SISTER'):
        quote = sister[rand]
    else:
        quote = "Try, shorter version of names"

    return ([res, quote])


app=Flask(__name__)
ui=FlaskUI(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result/<val>")
def result(val):
    p='<h1>'+val.strip('>').strip('<')+'<h1>'
    na,na2=p.split("_")
    result,quote=calc(na,na2)
    return render_template("result.html",result=result,quote=quote)

if __name__=="__main__":
    ui.run()

