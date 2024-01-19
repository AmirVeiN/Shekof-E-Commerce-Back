import csv
from models import Product


def importData(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Product.objects.create(
                id = row[0],
                Type = row[1],
                ProductId = row[2],
                Name = row[3],
                InPublished = row[4],
                IsSpecial = row[5],
                IsVisible = row[6],
                ShortDescription = row[7],
                Description = row[8],
                InStock = row[13],
                StockCount = row[14],
                Weight = row[18],
                Height = row[19],
                Wide = row[20],
                Loudly = row[21],
                Price = row[25],
                Categry = row[26],
                SimCard = row[27],
                Image = row[29],
                Skill1 = row[39],
                Skill2 = row[40],
                Skill3 = row[41],
                Skill4 = row[42],
                Skill5 = row[43],
                Skill6 = row[44],
                Skill7 = row[45],
                Skill8 = row[46],
                Skill9 = row[47],
                Skill10 = row[48],
                Skill11 = row[49],
                Skill12 = row[50],
                Skill13 = row[51],
                Skill14 = row[52],
                Skill15 = row[53],
                Skill16 = row[54],
                Skill17 = row[55],
                Skill18 = row[56],
                Skill19 = row[57],
                Skill20 = row[58],
            )

if __name__ == '__main__':
    csv_file_path = '/data.csv'
    importData(csv_file_path)