# ompat 2024 
# See README 

# Start Timer
import time
start = time.time()

# Import packages
import wikipedia 

# Pull text from wikipedia 
wiki = wikipedia.page("Python (Programming Language)")
text = wiki.content
content_list = list(wiki.content)

print("Number of Characters in List is : ", len(content_list))

frequency = {}

for item in content_list:
    if item in frequency:   
        frequency[item] += 1

    else:
        frequency[item] = 1

print(frequency)

# End Timer
end = time.time()
print("Done!")
print(end - start, "Sec")

