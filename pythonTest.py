def decode(message_file):
  file_text = open(message_file)
  words = dict(map(str.split, file_text))
  file_text.close()

  send_back = []
  count = i = 1
  while i <= len(words):
    send_back.append(words[str(i)])
    count += 1
    i += count
  return send_back

process = "C:/Users/gamer/Downloads/coding_qual_input.txt"
print(decode(process))