class FormatData:
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    
    def prepare(self, raw_date):
        result = ""
        for item in raw_date:
            new_line = ",".join(
                (
                    item["name"],
                    item["surname"],
                    item["occupation"]
                )
            )
            result += f"{new_line}\n"
        return result
    

    def write_file(self, filename):
        with open(filename, "w", encoding="UTF8") as f:
            f.write(self.data)


data = [
    {
        "name": "Sherlock",
        "surname": "Holms",
        "occupation": "private detective"
    },
    {
        "name": "John",
        "surname": "Watson",
        "occupation": "doctor"
    }
]

exporter = FormatData(data)
exporter.write_file("out.csv")