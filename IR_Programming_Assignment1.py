import re
import PortersAlgorithm
# Initialization
input_data = open("28.txt", "r")
stop_words = open("stop_words.txt", "r")
result = []
stop_words_list = []
# Tokenization & Lowercasing
for word in input_data.read().split():  # Split words by space
    temp = re.sub('[^a-zA-Z0-9]', "", word.lower())  # Covert words to lowercase and remove punctuations
    if temp not in result:
        result.append(temp)  # add the tokens into the result array
# Stemming using Porter's algorithm
p = PortersAlgorithm.PorterStemmer()  # Create a object to process Porter's algorithm
for i in range(0, len(result)):
    temp = p.stem(result[i], 0, len(result[i])-1)  # Call the build-in method for stemming
    if len(temp) > 3:  # if the length of word which process the Porter's algorithm is bigger than 3, replace it
        result[i] = temp
# Stop word array
for word in stop_words:
    stop_words_list.append(word.strip())
# Save the result as a txt file
output_file = open("Output.txt", "w")
for i in result:
    if i not in stop_words_list:  # Add the result without stop words
        output_file.write("%s\n" % i)
input_data.close()
stop_words.close()
output_file.close()



