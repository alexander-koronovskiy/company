import hashlib

columns = ["name", "algorithm", "hash_sum"]
files = []

# read info about files
with open("sum_file.csv") as config:
    for row in [line.split() for line in config]:
        files.append(dict(zip(columns, row)))

# check hash sum
for file in files:
    status = "FAIL"
    content = ""
    try:
        with open(file["name"]) as f:
            content += f.read()
            if file["algorithm"] in hashlib.algorithms_available:
                if int(hashlib.sha1(content.encode("utf-8")).hexdigest(), 16) == int(
                    file["hash_sum"], 16
                ):
                    status = "OK"
    except FileNotFoundError:
        status = "NOT FOUND"
    finally:
        print(file["name"], status)
