text = input("File name: ")
text = text.strip().lower()

if text.endswith(".jpg") or text.endswith(".jpeg"):
    print("image/jpeg")
elif text.endswith(".png"):
    print("image/png")
elif text.endswith(".pdf"):
    print("application/pdf")
elif text.endswith(".txt"):
    print("text/plain")
elif text.endswith(".zip"):
    print("application/zip")
elif text.endswith(".gif"):
    print("image/gif")
else:
    print("application/octet-stream")
