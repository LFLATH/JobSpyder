from indeed import indeedScrape
#job_title = input("What is the job title you are applying for? As one word please. IE Software Developer = softwaredeveloper ")
#location = input("What is the location you are searching for your job? If it is remote, say remote! ")
#radius = input("How far from this location are you willing to travel? Please put the number in miles ")
#experience = input("What level is your experience? Options are Entry, Mid, or Senior ")


scrape = indeedScrape("softwaredeveloper", "Atlanta", "30", "Entry")
scrape.scrape()

