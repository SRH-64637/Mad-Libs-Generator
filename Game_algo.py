with open("story.txt", "r") as f:
    story = f.read()
print(story)

starting_point = -1
words = {}

for i, char in enumerate(story):
    if char == "(":
        starting_point = i

    elif char == ")" and starting_point != -1:
        placeholder = story[starting_point: i+1]
        if placeholder not in words:
            words[placeholder] = None
        starting_point = -1

for key,value in words.items():
    words[key] = input(f"Enter a word for {key}: ")
    story = story.replace(key, words[key])

print(story)


        
