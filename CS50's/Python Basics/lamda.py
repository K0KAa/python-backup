people =[
    {
        "name":"Kushal", "house":"London"
    },
    {
        "name":"KOKAA", "house":"India"
    },
    {
        "name":"Kanchan", "house":"Canada"
    }
]

people.sort(key=lambda people: people["name"])

print(people)

