import twitchScraper
import mkRand

def main():
    
	i = 0
	vals = []
	while i < 8:
	    twitchData = twitchScraper.collectData()
	    print(twitchData)

	    randomVal = mkRand.get4bitlen(twitchData)
	    print(randomVal)

	    vals.append(randomVal)
	    i += 1

	print(vals)
	finalVal = mkRand.getInt(vals)
	print(finalVal)
if __name__ == "__main__":
    main()