import twitchScraper
import mkRand

def main():
    
	
	
	j = 0
	f = open('integer.out', 'w')
	while j < 200:
		val = 0
		vals = []
		#i = 0
		#while i < 8:
		twitchData = twitchScraper.collectData()
		print(twitchData)

		randomVal = mkRand.get1bitlen(twitchData)
		#print(randomVal)
		#f.write(randomVal)

		vals.append(randomVal)
		#i += 1

		#print(vals)
		#finalVal = mkRand.getInt(vals)
		#print(finalVal)

		f.write(str(val))
		j += 1

if __name__ == "__main__":
    main()
