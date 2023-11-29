filename = input()
file = open(filename, "r")
no_of_requests_more_than_5000 = 0
total_bytes = 0
for log in file.readlines():
    words = log.split()
    bytesSent = int(words[-1])
    if bytesSent > 5000:
        no_of_requests_more_than_5000 += 1
        total_bytes += bytesSent

result_file = open("bytes_" + filename, "w")
result_file.write(str(no_of_requests_more_than_5000))
result_file.write("\n")
result_file.write(str(total_bytes))
result_file.close()
file.close()

