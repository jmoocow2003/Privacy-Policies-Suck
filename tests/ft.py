import fastText

def main():
    print("foo")
    model = fastText.train_supervised('..\Data\Gerard.txt')
    print(model.predict("this is a sentence"))

main()