import twitchScraper
import mkRand

def main():
    
	j = 0
	f = open('randomData.out', 'a')
	while j < 50:
		vals = []
		i = 0
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

		f.write(finalVal)
		j += 1

if __name__ == "__main__":
    main()