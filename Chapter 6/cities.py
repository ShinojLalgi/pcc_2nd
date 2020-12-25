cites = {
    'mumbai'        :       {
                            'state' : 'maharashtra',
                            'country' : 'india',
                            'language' : 'marathi, hindi'                
                            },
    'new york city' :       {
                            'state' : 'new york',
                            'country' : 'unitied states of america',
                            'language' : 'american english'
                            },
    'london'        :       {
                            'state' : 'united kingdom',
                            'country' : 'england',
                            'language' : 'british english'
                            }
}


for key, value in cites.items():
    print(f"{key.title()}:")
    for key, value in value.items():
        print(f"--{key.title()} : {value.title()}")
    print()