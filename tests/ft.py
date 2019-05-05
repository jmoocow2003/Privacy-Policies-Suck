import fastText

def main():
    model = fastText.train_supervised('..\Data\Gerard.txt')
    print(model.predict("These tools collect information sent by your device or our Service, including the web pages you visit, add-ons, and other information that assists us in improving the Service."))

main()