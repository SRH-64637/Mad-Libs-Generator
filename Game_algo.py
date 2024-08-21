with open("story.txt", "r") as f:
    story = f.read()

multiple_resp = {
    "(adjective)":story.count("(adjective)"),
    "(noun)":story.count("(noun)"),
    "(plural nouns)":story.count("(plural nouns)"),
    "(verb)": story.count("(verb)")
    }
starting_point = -1
last_index = 0
words = {}
new_story = ""


# multiple_resp stores the placeholders that occurs more than once and needs multiple distinct response

for i, char in enumerate(story):
    if char == "(":
        starting_point = i 

    elif char == ")" and starting_point != -1:
        placeholder = story[starting_point: i+1].lower() # "(noun)"

        if placeholder in multiple_resp.keys():
            response = input(f"Enter a word for {placeholder} (More {multiple_resp[placeholder]} To Go): ")
            multiple_resp[placeholder] = multiple_resp[placeholder]-1
            new_story += story[last_index:starting_point] + response
            last_index = i + 1
        else:
            if placeholder not in words:
                words[placeholder] = None

        starting_point = -1

# Append the remaining part of the story after the last placeholder
new_story += story[last_index:]

for key,value in words.items():
    words[key] = input(f"Enter a word for {key}: ")
    new_story = new_story.replace(key, words[key])

print(new_story)


        
