from summa import summarizer

text = "You don't have to create an account to use some of our service features, such as searching and viewing public Twitter profiles or watching a broadcast on Periscope's website. If you do choose to create an account, you must provide us with some personal data so that we can provide our services to you. On Twitter this includes a display name (for example, 'Twitter Moments'), a username (for example, @TwitterMoments), a password, and an email address or phone number. Your display name and username are always public, but you can use either your real name or a pseudonym. "
print(summarizer.summarize(text))